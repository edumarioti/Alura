from datetime import datetime, timedelta

class Datas_br:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        print(self.momento_cadastro)
    
    def __str__(self):
        return self.data_formatada() 
    
    def mes_cadastro(self):
        lista_mes = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_do_cadastro = lista_mes[self.momento_cadastro.month - 1]
        return mes_do_cadastro
    
    def dia_cadastro(self):
        lista_dia_da_semana = [
            "segunda", "terça", "quarta"
            "quinta", "sexta", "sabado"
        ]
        dia_do_cadastro = lista_dia_da_semana[self.momento_cadastro.weekday()]
        return dia_do_cadastro

    def data_formatada(self):
        data = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro