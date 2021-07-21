import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        return url.strip()

    def valida_url(self):
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError('Essa URL não é válida')

        if not self.url:
            raise ValueError('A URL está vazia')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        url_parametros = self.get_url_parametros()
        indice_parametro = url_parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = url_parametros.find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = url_parametros[indice_valor:]
        else:
            valor = url_parametros[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\nParâmetros: ' + self.get_url_parametros() + '\nURL Base: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == other

extrator_url = ExtratorURL('https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real')
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)
print(extrator_url)