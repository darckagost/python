#con utilizzo di variabile e la keyword input()

def somma ():
    print("somma")
    #chiede ad utente di inserire il valore di a
    print("inserisci il valore di a:\t")
    #prende in input un valore inserito dall'utente e lo trasforma (int) tramite cast in intero
    a = int(input())
    print("inserisci il valore di b:\t")
    b = int(input())
    print(f"risultato della somma:\t {a+b}")


somma()    


def sottrazione ():
    print("sottrazione")
    #chiede ad utente di inserire il valore di a
    print("inserisci il valore di a:\t")
    #prende in input un valore inserito dall'utente e lo trasforma (int) tramite cast in intero
    a = int(input())
    print("inserisci il valore di b:\t")
    b = int(input())
    print(f"risultato della sottrazione:\t {a-b}")

sottrazione ()


def moltiplicazione ():
    print("moltiplicazione")
    #chiede ad utente di inserire il valore di a
    print("inserisci il valore di a:\t")
    #prende in input un valore inserito dall'utente e lo trasforma (int) tramite cast in intero
    a = int(input())
    print("inserisci il valore di b:\t")
    b = int(input())
    print(f"risultato della moltiplicazione:\t {a*b}")

moltiplicazione()


def divisione ():
    print("divisione")
    #chiede ad utente di inserire il valore di a
    print("inserisci il valore di a:\t")
    #prende in input un valore inserito dall'utente e lo trasforma (int) tramite cast in intero
    a = int(input())
    print("inserisci il valore di b:\t")
    b = int(input())
    if (a==0):
        print("error")
    if (b==0):
        print("error")
    else :
        print(f"\t{a/b}")

divisione ()        



