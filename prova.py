
a = 2
b = 2

#stampa la somma tra due variabili
def somma (a, b):
    print(a+b)

#stampa la moltiplicazioni tra due variabili
def moltiplica (a, b):
    print(a*b)

#stampa la divisione tra due variabili
def dividi (a, b):
    #si usa l'operatore di controllo IF per verificare se il risultato del confronto è falso o vero
    if (b==0):
        print ("Error")
    else :
        print(a/b)    

#stampa la sottrazione tra due variabili
def sottrai(a, b):
    print(a-b)

somma(a, b)
moltiplica(a, b)
sottrai(a, b)
dividi(a, b)