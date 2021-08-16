import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.validar(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")

    def __str__(self):
        return self.format_cep()

    def validar(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        req = requests.get(url)
        dados = req.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
