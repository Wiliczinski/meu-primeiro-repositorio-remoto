valor = input("Base do triangulo: ")
base = float(valor)

altura = float(input("Altura do triangulo: "))

area = base * altura / 2

print ("A area vale ", area)

area2 = round(area,0) #arredendonda para 2 casas
print("A area vale " + str(area2))