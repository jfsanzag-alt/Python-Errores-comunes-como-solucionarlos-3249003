lista_elementos = ["abc", "def", "ghi", "jkl"]
print(lista_elementos[0])
# print(lista_elementos[4])

dict_elementos = {
	"nombre": "Ana",
	"edad": 25
}
print(dict_elementos["apellido"] if "apellido" in dict_elementos.keys() else None)
for elem in dict_elementos:
  print(elem if elem in dict_elementos.keys() else None)

