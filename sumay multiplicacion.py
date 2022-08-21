primernumero=int(input("Ingrese el primer numero"))
segundonumero=int(input("Ingrese el segundo numero"))
tercernumero=int(input("Ingrese el tercer numero"))
if primernumero>0:
    consolidado=primernumero+segundonumero+tercernumero
else:
    consolidado=(-primernumero)*segundonumero*tercernumero
print("El resultado es",consolidado)