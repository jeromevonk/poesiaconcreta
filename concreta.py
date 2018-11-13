# Lista de palavras retirada de: https://alcor.concordia.ca/~vjorge/Palavras-Cruzadas/Lista-de-Palavras.txt

import random

# Faça uma lista com as palavras do arquivo
with open("palavras.txt") as file:
    palavras = [line.strip() for line in file]
    print("->Temos uma lista com", len(palavras), "palavras")
    
    poema = "";
    # Numero de linhas do poema
    for i in range(0, random.randint(3, 4)):
        for j in range(0, random.randint(2, 5)):
            poema += palavras[random.randint(1, len(palavras))] + ' ';
        poema += '\n'
        
        
    print("\nAcabou de ser criado o mais novo poema concreto brasileiro:\n\n")
    print(poema)
