# CREAR ESTRUCTURAS
mi_lista = [10, 20, 30]
mi_tupla = (100, 200, 300)
mi_set = {1, 2, 3}
mi_dict = {"nombre": "Ana", "edad": 40, "ciudad": "Santiago"}

print("Lista:", mi_lista)
print("Tupla:", mi_tupla)
print("Set:", mi_set)
print("Diccionario:", mi_dict)

print()

#LAS LISTAS SON MUTABLES Y ORDENADAS.
#LAS TUPLAS SON INMUTABLES Y ORDENADAS.
#LOS SETS SON MUTABLES, NO ORDENADOS Y SIN ELEMENTOS DUPLICADOS.
#LOS DICCIONARIO ALMACENAN PARES CLAVE-VALOR, SON MUTABLES Y ORDENADOS.

# ACCEDER A ELEMENTOS
print("Segundo elemento de la lista:", mi_lista[1])
print("Clave 'nombre' del diccionario:", mi_dict["nombre"])

print()

# POR QUÉ NO SE PUEDE ACCEDER  POR INDICE A UN SET? 
# R. PORQUE LOS SETS NO MANTIENEN UN ORDEN FIJO, LOS ELEMENTOS SE ALMACENAN  SEGUN SU VALOR HASH, 
#    NO EXISTE UNA POSICIÓN NUMERICA ESTABLE A LA CUAL REFERIRSE.

# CONTAR E ITERAR
print("Cantidad de elementos:")
print("  lista:", len(mi_lista))
print("  tupla:", len(mi_tupla))
print("  set:", len(mi_set))
print("  diccionario:", len(mi_dict))

print()

print("Iterando lista:")
for elem in mi_lista:
    print(" ", elem)

print("Iterando tupla:")
for elem in mi_tupla:
    print(" ", elem)

print("Iterando set:")
for elem in mi_set:
    print(" ", elem)

print("Iterando diccionario (clave -> valor):")
for clave, valor in mi_dict.items():
    print(f"  {clave} -> {valor}")

print()

# MODIFICAR ESTRUCTURAS
mi_lista.append(40)
print("Lista tras agregar 40:", mi_lista)

mi_set.add(4)
print("Set tras agregar 4:", mi_set)

mi_lista.remove(10)
print("Lista tras borrar 10:", mi_lista)

mi_dict["pais"] = "Chile"
print("Diccionario tras nueva clave:", mi_dict)

# INTENTA MODIFICAR TUPLA
try:
    mi_tupla[0] = 999
except TypeError as e:
    print(f"Error al modificar tupla: {e}")
    # LAS TUPLAS SON INMUTABLES, NO SE PUEDEN CAMBIAR, AGREGAR NI ELIMINAR ELEMENTOS UNA VEZ CREADAS.
   
