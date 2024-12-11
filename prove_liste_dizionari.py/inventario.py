felpa1={"nere collo alto": "disponibile", "XL": "tre", "L":"otto", "M":"nove","S": "due"}
felpa2={"bianca con cappuccio":"disponibile", "XL": "due", "L":"quattro", "M":"sette","S": "una"}
pantalone1={"baggy":"disponibile",  "XL": "uno", "L":"sette", "M":"dodici","S": "quindici"}

felpa2["XXL"]="dieci"
felpa1["XL"]="sei"
del felpa1["XL"]

for items  in felpa1.items():
    print(items)


  
