print("Funciones version 2")
print("Olave Cruz")
celulares=("iPhone","Xiaomi","LG")
razasdeperro=["roguaile","bulterie","buldo"]
#Set
set1 = (("José José", "Canciones interpretadas:", 34, "Edad:", 40, "Hombre"))
#Tupla
def verlista(telefonos):
    for uncelular in telefonos: print (uncelular)
#Lista
    def verlista2(perros): 
        for nombres in perros: print (nombres)

#Tupla
print("Imprime celulares en forma de Tupla")
verlista(celulares)
#Lista
print("Imprime razas de perros en forma de Lista")
verlista(razasdeperro)
#Set
print("Imprime los datos de una persona en forma de Set")
verlista(set1)
#Diccionario
print("Imprime un diccionario")
thisdict = {
  "Marca": "McLaren",
  "Modelo": "Senna",
  "Año de creación": 2019,
  "Presente": "Sigue a la venta"
}
print(thisdict)
print("Celulares es de tipo",type(celulares))
print("Arriba escribe el tipo, en este caso, tupla, de los celulares")
