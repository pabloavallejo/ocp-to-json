import re

noticia= "Este 19 de noviembre seremos testigos del último eclipse lunar de este 2021. Pero además, en esta oportunidad tendrá un condimento extra: será el eclipse de Luna más largo del siglo."

buscar = "eclasdfipse"

if re.search(buscar,noticia) is not None:
    
    print("informacion localizada")

else:
    print("no se ha encontrado la noticia")



lista_nombres= ['Ana Gomez',
                'Maria Guzman',
                'Sandra Lopez',
                'Santiago Gomez']

#for elemento in lista_nombres:
   # if re.findall('^Sandra', elemento): # ^ se utiliza como comodin para el inicio
   #     print(elemento)

for elemento2 in lista_nombres:
    if re.findall('Lopez$', elemento2): # $ se utiliza como comodin que finalicen
        print(elemento2)


objetos = [ 'hombres',
            'mujeres',
            'mascotas',
            'niños',
            'niñas',
            'camión',
            'camion',
            'caramelo',
            'abuelo',
            'Na5',
            'Na1',
            'Na2']

for elemento3 in objetos:
    if re.findall('niñ[ao]s', elemento3):
        print(elemento3)

for elemento4 in objetos:
    if re.findall('^[a-f]',elemento4):
        print(elemento4 + ' - elemento4')

for elemento5 in objetos:
    if re.findall('Na[0-3]', elemento5): # ^ representan la negativa a los valores a mostrar
        print(elemento5 + ' - Objeto5')

for elemento6 in objetos:
    if re.match('.....elo', elemento6, re.IGNORECASE): # el . se usa como comodin
        print ('palabras encontradas ' + elemento6)
    else:
        print('no se encontro la palabra buscada ' + elemento6)