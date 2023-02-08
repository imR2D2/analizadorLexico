import jiji.lex as lex

tokens = (
    'NUMERO',
    'IGUAL',    
    'INCREMENTO',
    'DECREMENTO',
    'MAYORQUE', 
    'MENORQUE',
    'DIFERENTEDE',
    'MENORIGUAL', 
    'MAYORIGUAL',
    'COMA',
    'DOSPUNTOS',
    'LPARENT',
    'RPARENT',
)

#Valores reservados
reserved = {
    'for':'PARA',
}

#Juntamos los tokens con los reservados, los hacemos tipo lista a los dos y de la lista de reservados ocupamos los values, no el key
tokens = list(tokens) + list(reserved.values())

#Se pone la t para indicarle que es un token de suma y le damos su caracteristica

#Necesitamos escapar el simbolo para poderlo usar como una expresion regular con "\" antes de la operacion que le asignamos
#r es para que tome los caracteres especiales como un string
#Se le pone la \ cuando ese simbolo tiene otro uso en las expresiones regulares, para que no de error y haga un cierto tipo de expresion

t_IGUAL = r'='
t_INCREMENTO = r'\++'
t_DECREMENTO = r'--'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_DIFERENTEDE = r'!='
t_MENORIGUAL = r'>=' 
t_MAYORIGUAL = r'<='
t_COMA = r'\,'
t_DOSPUNTOS = r':'
t_LPARENT = r'\('
t_RPARENT = r'\)'

                                                        
def t_NUMERO(t):
    #Identificar numero compuesto por uno digito
    #r'\d'
    #Identificar numero compuesto por otros digitos, por ejemplo el 70-1, evaluara el 70 junto y no separado
    r'\d+'
    #Convierte el digito a entero una vez que se evalua
    t.value = int(t.value)
    return t

def t_ID(t):
    #Que puede comenzar con letras o _
    r'[a-zA-Z_] [a-zA-Z0-9_]*'
    #Hacemos una validacion, que nos regresa lo de reserved, y si no existe o no lo encuentra sera un ID
    t.type = reserved.get(t.value, 'ID      ')
    return t

def t_error(t):
    #Estara esperando un string y el otro es lo que estas esperando que no sabra que tipo de token es
    print("Token desconocido: '%s'" % t.value)
    #Si hay un error brinca al siguiente token
    t.lexer.skip(1)

#Ignorar si hay un espacio en blanco y una tabulacion, por ejemplo en 12 = 12, sin esto no podria hacer con espacios, buscaria todo junto
t_ignore = ' \t\n'

#Objeto dentro del modulo lex, manda a llamar al constructor del lexico
lexer = lex.lex()

#Expresion que separare por tokens o evaluare
listaTxt = open('data.txt', 'r')
data = listaTxt.read()

#Revisa cada uno de los tokens en la t_NUMERO, uno por uno
lexer.input(data)

#Evalua cada uno de los tokens mientras haya tokens dentro el token, si no hay nada por iterar rompe el ciclo
while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)

'''
RESULTADO////////////////////
Primero entrega el tipo de dato, despues el dato que encontro en la data,
despues cuantas veces se repite y finalmente la posicion en la que se encuentra
dentro de la data.

LexToken(NUMERO, 7, 1, 0)
'''
