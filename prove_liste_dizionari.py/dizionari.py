dizionario = {"nome": "Pluto", "età": "100"}

dizionario["occhi"] = "Due"


for key in dizionario.keys():
    print(key)

for value in dizionario.values():
    print(value)

for key, value in dizionario.items():
    print(key + "-" + value)

for item in dizionario.items():
    print(item) 