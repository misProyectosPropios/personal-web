
# Va a recibir un string con TRUE's o FALSE's y va a decir si es verdadero o falso
# Los básicos: AND, OR, NOT, PARENTESIS
# Cada variable tiene que estar separada con un valor lógico
# Primero sin variables

# prod valorLogico (s: list[str]) -> bool {
#   requiere: {s tiene solamente "True", "False", "OR", "AND", "-"}
#   requiere: {el primer elemento es True, False or -}
#   requiere: {despues de un -, debe haber un True or False}
#   asegura: {res devuelve tras hacer el valor logico de la frase}
#
# }
def valorLogicoFormualaBasica(s: list[str]) -> bool:
    res: bool = True
    s = sacarNegacionFormulaBasica(s)
    negarRes: bool = False
    andRes: bool = False
    orRes: bool = False
    for i in s:
        if (esAnd(i)):
            andRes = True
        elif (esOr(i)):
            orRes = True
        elif (esValorTrueOrFalse(i)):
            if (andRes):
                res = res and convertirStringToBool(i)
                andRes = False
            elif (orRes):
                res = res or convertirStringToBool(i)
                orRes = False  
            else:
                res = convertirStringToBool(i)
    return res

def sacarNegacionFormulaBasica(s: list[str]) -> list[str]:
    res: list[str] = []
    valorBoleano: bool = False
    negarRes: bool = False
    for i in s:
        if (esNegacion(i)):
            negarRes = True
        elif (esValorTrueOrFalse(i)):
            if (negarRes):
                valorBoleano = convertirStringToBool(i)
                valorBoleano = not valorBoleano
                negarRes = False
            else: 
                valorBoleano = convertirStringToBool(i)
            res.append(str(valorBoleano))
        else:
            res.append(i)
    return res

def convertirStringToBool(string: str) -> bool:
    res: bool = False
    if (string == "True"):
        res = True
    return res

def esNegacion(string: str) -> bool: 
    res: bool = False
    if (string == "-"):
        res = True
    return res

def esAnd(string: str) -> bool: 
    res: bool = False
    if (string == "AND"):
        res = True
    return res

def esOr(string: str) -> bool: 
    res: bool = False
    if (string == "OR"):
        res = True
    return res

def esValorTrueOrFalse(string: str) -> bool: 
    res: bool = False
    if (string == "True" or string== "False"):
        res = True
    return res

print(valorLogicoFormualaBasica(["-", "True", "AND", "False",]))