

numeros = [1,2,3,4,5,6,7,8,9,10]

def mifunction(x):
    if x % 2 ==0 :
        return True
    return False

resultado = filter(mifunction,numeros)
print(list(resultado))


resultado2 = filter(lambda x: str(x).startswith("pep"), ["pepe", "pepito", "juan"])
print(list(resultado2))