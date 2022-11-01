rodas = 4
peso = 6001
pessoas = 9

if rodas < 2:
    print("Sem Categoria")
elif rodas >= 2 and rodas <=3:
    print("Categoria A")

elif rodas == 4 and pessoas <= 8 and peso <= 3500:
    print("Categoria B")

elif rodas >= 4 and peso > 3500 and peso <= 6000 and pessoas <= 8:
    print("Categoria C")

elif rodas >= 4 and pessoas > 8 and peso <= 6000:
    print("Categoria D")

else:
    print("Categoria E")