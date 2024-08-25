
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

def esParentesisAbierto(string: str) -> bool:
    res: bool = False
    if (string == "("):
        res = True
    return res

def esParentesisCerrado(string: str) -> bool:
    res: bool = False
    if (string == ")"):
        res = True
    return res

def hayParentesis(s: list[str]) -> bool:
    for i in s:
        if (i == "("):
            return True
    return False

# Voy a suponer que, como se llamo a esta función, hay al menos un parentesis de abierto y 
# otro de cerrar
#
def buscarFormulaMasBasica(s: list[str]):
    res: list[str] = []
    dentroDeParentesis: bool = False
    for i in s:
        if (esParentesisAbierto(i)):
            dentroDeParentesis = True
        elif (esParentesisCerrado(i)):
            return res
        elif (dentroDeParentesis and esParentesisAbierto(i)):
            res = []
        elif (dentroDeParentesis):
            res.append(i)
    return res
        
def appendListOfStringsToListOfStrings(s: list[str], toConcatenate: list[str]) -> list[str]:
    for i in toConcatenate:
        s.append(i)
    
def reemplazarFormulaMasBasica(s: list[str], valorDeLaFormula: bool) -> list[str]:
    res: list[str] = []
    yaSeReemplazo: bool = False
    almacenDeFormulas: list[str] = []
    dentroDeParentesis: bool = False
    for i in s:
        if (yaSeReemplazo):
            res.append(i)
        elif (esParentesisAbierto(i)):
            if (len(almacenDeFormulas) != 0 and dentroDeParentesis):
                res.append("(")
                appendListOfStringsToListOfStrings(res, almacenDeFormulas)
                res.append(almacenDeFormulas)
            if (len(almacenDeFormulas) != 0):
                appendListOfStringsToListOfStrings(res, almacenDeFormulas)
            almacenDeFormulas = []
            dentroDeParentesis = True
        elif (esParentesisCerrado(i)):
            res.append(valorDeLaFormula)
            yaSeReemplazo = True
            almacenDeFormulas = []
        else:
            almacenDeFormulas.append(i)
        
    return res

def resolverFormula(s: list[str]):
    formula: list[str]
    
    while (hayParentesis(s)):
        s = reemplazarFormulaMasBasica(s, str(valorLogicoFormualaBasica(buscarFormulaMasBasica(s))))
        #resolverFormulasMasBasicas(s)
    return valorLogicoFormualaBasica(s)


def esOperacion(elemento: str):
    if (esAnd(elemento) or esOr(elemento) or esParentesisAbierto(elemento) or esParentesisCerrado(elemento) or esNegacion(elemento)):
        return True
    return False

#Devuelve la cantidad de variables que hay
def contarCantidadVariables(formula: list[str]):
    return len(variablesDeFormula(formula))


#Devuelve un set con todas las variables, sin repetir
def variablesDeFormula(formula: list[str]):
    variables = set()
    for elemento in formula:
        if (not esOperacion(elemento) and not esValorTrueOrFalse(elemento)):
            variables.add(elemento)
    return variables

def printFormula(formula: list[str]):
    for i in formula:
        print(i, end=" ")
    print()

def printValorVariables(valorVariables: str):
    for i in range(len(valorVariables)):
        print(valorVariables[i] + " ", end=" ")

def printArrayVariables(array_variables: list[str]): 
    for i in array_variables:
        print(i + " ", end= ' ')
# Diccionario con variables no puede tener como llaves, AND, -, OR (basicamente los operadores)
# Las llaves del diccionario solo tienen valores "True" o "False"
# Devuelve la formula, con los reemplazos sintacticos dichos en el diccionario
def instanciarVariables(formulaConVariables: list[str], diccionarioValorVariable: dict[str, str]) -> list[str]:
    res: list[str] = []
    for i in formulaConVariables:
        if i in diccionarioValorVariable:
            res.append(diccionarioValorVariable[i])
        else:
            res.append(i)
    return res

def evaluarFormulaConVariablesEnCiertaAsignacion(formulaConVariables: list[str], diccionarioValorVariable: dict[str, str]) -> bool:
    formula: list[str] = instanciarVariables(formulaConVariables, diccionarioValorVariable)
    return resolverFormula(formula)

def convertirSetEnArray(set: set[str]) -> list[str]:
    res: list[str] = []
    for i in set:
        res.append(i)
    return res

def evaluarConTodasLasPosibilidades(formulaConVariables: list[str]):
    variables_set: set[str] = variablesDeFormula(formulaConVariables)
    variables_array = convertirSetEnArray(variables_set)
    printArrayVariables(variables_array)
    printFormula(formulaConVariables)
    for i in range(pow(2, len(variables_array))):
        numero_en_binario = convertirNumeroDecimalEnBinario(i, len(variables_array))
        diccionario_variables = {}
        for index in range(len(numero_en_binario)):
            diccionario_variables[variables_array[index]] = convertir1y0EnTrueYFalse(numero_en_binario[index])
        printValorVariables(numero_en_binario)
        print(evaluarFormulaConVariablesEnCiertaAsignacion(formulaConVariables, diccionario_variables))
    return

def convertir1y0EnTrueYFalse(str: str) -> str:
    if (str == "0"):
        return "False"
    return "True"

def convertirNumeroDecimalEnBinario(num: int, cantidad_bits: int) -> str:
    res: str = ""
    if (num == 0):
        res = "0" * cantidad_bits
    else:
        while (num != 0):
            mod_2 = num % 2
            res = str(mod_2) + res
            num = (num -mod_2) // 2
        if (len(res) > cantidad_bits):
            return "ERROR. Overflow"
        else:
            cuanto_falta_para_llenar_bits = cantidad_bits - len(res)
            res = "0" * cuanto_falta_para_llenar_bits + res 
    return res

formulaVariables: list[str] = ["-", "(", "P", "OR", "Q", ")"]    
formula: list[str] = ["-", "True", "OR", "-", "(", "False", "AND", "-", "TRUE", ")"]

printFormula(formulaVariables)

evaluarConTodasLasPosibilidades(formulaVariables)
#print(convertirNumeroDecimalEnBinario(16, 5))