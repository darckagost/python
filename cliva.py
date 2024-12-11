#param:str
#calcola il totale ivato
#return:void
def calc_iva (a):
#controlla che il parametro non corrisponda a 0 
  if (a==0):
    print("Errore,importo non valido:\t")
#esegue il calcolo dell'iva
  else :
    print (f"Totale ivato :/\t{(a*22/100)+a}")
#param=none
#ti chiede di inserire l'input,
#converte l'input da stringa a numerico con la virgola
#esegue la funzione calc_iva
#return:void
def iva22 ():
     print("Inserisci l'imponibile:\t")
     a =float(input())   
     calc_iva(a)


iva22 ()    


