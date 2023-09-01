#Ejercicio 1
palabra_encriptada =""
abc="abcdefghijklmnñopqrstuvwxyz"
corrimiento=int(input("Ingrese los lugares a correr: "))
palabra=""
for i in range(5):
  palabra = input("Ingrese el mensaje a encriptar: ").lower()
  for letra in palabra:
    if (letra in abc):
      indice = abc.find(letra)
      indice_encriptado = (indice+corrimiento)%27
      palabra_encriptada += abc[indice_encriptado]
    else:
      palabra_encriptada += letra


  print(palabra_encriptada)

#Ejercicio 2
total_pares=0
total_impares=0

while True:
    num=int(input('Ingrese un número entero positivo (ingrese 0 para salir): '))
    
    if num == 0:
        break
    
    if num <0:
        print('Ingrese un número positivo')
        continue

    num_temp = num
    while num_temp>0:
        digito=num_temp % 10
        if digito%2 == 0:
            total_pares+=1
        else:
            total_impares+=1
        num_temp//=10


print('La cantidad de numeros pares ingresados es de: ', total_pares)
print('La cantidad de numeros impares ingresados es de: ', total_impares)