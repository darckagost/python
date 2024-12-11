def imp():
    print("inserisci totale ivato")
    a=float(input())

    if (a==0):
        print("errore  inserire un numero valido")
    else:
    
        print(f"imponibile :\t {a-((a*22)/100)}")

imp()            
