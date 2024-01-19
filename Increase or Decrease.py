#utile généralement pour des soldes, mais aussi pour d'autres occasions, permet de faire une agmentation ou une réduction d'une donnée par rapport à un pourcentage que vous déterminerez
a=3
while a!=1 and a!=2 and a!=0:
    print("Tapez 1 pour une augmentation\nTapez 2 pour une diminution\nTapez 0 pour annuler")
    a=int(input("Tapez ici : "))

if a==1:
    b=float(input("La donnée à augmenter : "))
    c=float(input("Le pourcentage d'augmentation : "))
    b=b+b*c/100
    print("Après augmentation, nous obtenons ",b)

if a==2:
    b=float(input("La donnée à diminuer : "))
    c=float(input("Le pourcentage de diminution : "))
    b=b-(b*c/100)
    print("Après diminution, nous obtenons ",b)
