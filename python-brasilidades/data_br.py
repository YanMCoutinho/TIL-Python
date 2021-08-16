from datetime import datetime

class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = ["janeiro", "fevereiro", "março",
                        "abril", "maio", "junho", "julho"
                        , "agosto", "setembro", "outubro",
                        "novembro", "dezembro"]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_cadastro(self):
        dia_semana = self.momento_cadastro.weekday()
        print(dia_semana)
        dias_da_semana = [
            "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"
        ]
        return dias_da_semana[dia_semana]

    def format_data(self):
        formatacao = self.momento_cadastro.strftime("%d/%m/%y %H:%M")
        return formatacao

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro