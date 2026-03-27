import random

def gerar_cartela(numero_dezenas, numero_jogos):

    lista_jogos = []
    for i in range(numero_jogos):
        numeros = []
        for i in range(numero_dezenas):
            while True:
                numero_aleatorio = random.randint(1, 60)
                if numero_aleatorio in numeros:
                    continue
                else:
                    numeros.append(numero_aleatorio)
                    break
        numeros.sort()
        
        lista_jogos.append(numeros)
        
    return lista_jogos

            
        
print(gerar_cartela(6, 5))



    
    