import array as arr

v=arr.array("i",[1, 20, 30, 50])
def somma_tot():
    
    
    tot = 0
    for i in range (0, len(v)):
        tot+=v[i]
        return tot
    print (f"{tot}")

print(somma_tot())
