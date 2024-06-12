
def volume(comprimento, altura, largura):
    if (comprimento <= 0) or (largura <= 0) or (altura <= 0):
        return 'nenhum dos valores pode ser 0 ou negativo'
    return (comprimento * altura * largura) / 1000

def potencia(volume, temp_desejada, temp_ambiente):
    return round(volume * 0.05 * (temp_desejada - temp_ambiente), 2)

def filtragem_hora(volume):
    return volume * 2
