magazzino = {"Edile": {"Cemento": 255., "Calcestruzzo": 135., "Intonaco": 200.},
                 "Pittura": {"Pennelli S": 34, "Pennelli M": 44, "Pennelli L": 67, "secchi": 224}}
 
def visualizza():
    for item in magazzino.items():
        print(item)
    

def elimina():
    del magazzino[input("inserisci il prodotto da eliminare:\t")]
    print(magazzino)
def aggiungi():
    magazzino[input("insereisci il prodotto da aggiungere:\t")] = (input("inserisci il valore"))
def aggiorna():

    p1 = (input("in quale categoria vuoi operare"))    
    p2 = (input("inserisci il prodotto da aggiornare"))
    p3 = (input("inserisci il valore"))


    if p1 in magazzino and p2 in magazzino[p1]:
        magazzino[p2] = p3
    else:
        print("Campo non trovato")

    








































print("ciao\t")
print("digita il numero relativo all opzione preferita")
print("MENù:")

print("1: visualizza i prodotti")
print("2: aggiungi un prodotto")
print("3: aggiorna le quantità dei prodotti")
print("4: rimuovi i prodotti")
print("5: accedi alla gestione degli ordini")
print("6: esci")

def scelta_menù():
    a=int(input("cosa vuoi fare"))
    if (a == 1):
        visualizza()
    elif (a == 2):
        aggiungi()
    elif (a == 3):
        aggiorna()
    elif (a == 4):
        elimina()
    else:
        print("errore, riprova")

scelta_menù()
        
    

    
   