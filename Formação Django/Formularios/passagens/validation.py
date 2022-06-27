def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não pode ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """ Verifica se há algum caracter numérico no campo informado"""
    if any(char.isdigit() for char in valor_campo):
            lista_de_erros[nome_campo] = 'Não inclua números neste campo'

def data_de_volta_menor_que_data_de_ida(data_ida, data_volta, lista_de_erros):
    """Verifica se a data de volta é menor que a de ida"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser menor que a data de ida'

def data_de_ida_menor_que_data_de_hoje(data_ida, data_pesquisa, lista_de_erros):
    """Veririfca se data de ida é menor que a data de hoje"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que a data da pesquisa'