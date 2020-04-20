
#Juego de adivinar
import random

intentosRealizados = 0 #Aca se guarda los intentos realizados por le jugador(se pone 0 porque todavia no se realizo ningun intento)

print('¡Hola! ¿Cómo te llamas?') #Al igual que el primer ejercicio imprime la frase
miNombre = input() #nombre del usuario

número = random.randint(1, 20) #me devuelve un numero aleatorio entre 1 y 2o y se almacena en la var numero
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:
    print('Intenta adivinar.') #Hay cuatro espacios delante de print.
    estimación = input()
    estimación = int(estimación)
    
    intentosRealizados = intentosRealizados + 1
    
    if estimación < número:
        print('Tu estimación es muy baja.') #Hay ocho espacios delante de print.
        
    if estimación > número:
        print('Tu estimación es muy alta.')
        
    if estimación == número:
        break #sale del bucle while instantaneamente
      
if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')
    
if estimación != número:
    número = str(número)
    print('Pues no. El número que estaba pensando era ' + número)

  

