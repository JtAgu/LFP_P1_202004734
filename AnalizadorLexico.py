from Token import Token
from Error import Error
import re

class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []

    def analizar(self, codigo_fuente):
        self.listaTokens = []
        self.listaErrores = []

        #inicializar atributos
        linea = 1
        columna = 1
        buffer = ''
        centinela = '#'
        estado = 0
        separador=4
        
        
        #automata
        i = 0

        while i< len(codigo_fuente):
            c = codigo_fuente[i]

            if estado == 0:
                if c==" ":
                    columna += 1

                elif c == '=':
                    buffer += c
                    i += 1
                    c = codigo_fuente[i]
                    if c==">":
                        buffer += c
                        self.listaTokens.append(Token(buffer, 'FLECHA', linea, columna))    
                        buffer = ''
                        columna += 1
                    else: 
                        self.listaTokens.append(Token(buffer, 'IGUAL', linea, columna))    
                        buffer = ''
                        columna += 1
                        i-=1
                    
                elif c == '(':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'ParentesisA', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ')':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'ParentesisC', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '{':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'LlaveA', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '}':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'LlaveC', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ';':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'PUNTO_COMA', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ',':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'COMA', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ':':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'DOS_PUNTOS', linea, columna))
                    buffer = ''
                    columna += 1
                                  
                elif re.search('\d', c):
                    buffer += c
                    columna += 1
                    estado = 2
                    
                elif re.search('[a-z]', c):
                    buffer += c
                    columna += 1
                    estado = 3
                
                elif c == '\'' or c == '"':
                    columna += 1
                    estado = 1
                elif c == '\n':
                    linea += 1
                    columna = 1
                elif c == '\t':
                    columna += 1
                elif c == '\r':
                    pass
                elif c == centinela:
                    print('Se aceptó la cadena!')
                    break
                else:
                    buffer += c
                    self.listaErrores.append(Error('Caracter ' + buffer + ' no reconocido en el lenguaje.', 'Léxico', linea, columna))
                    buffer = ''
                    columna += 1
            elif estado == 2:
                if re.search('\d', c):
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, 'ENTERO', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 1:
                if c == '\'' or c == '"':
                    self.listaTokens.append(Token(buffer, 'CADENA', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1

            elif estado == 3:
                if re.search('[a-z]', c):
                    buffer += c
                    columna += 1
                else:
                    if buffer == 'replist':
                        self.listaTokens.append(Token(buffer, 'REPLIST', linea, columna))
                    elif buffer == 'nombre':
                        self.listaTokens.append(Token(buffer, 'NOMBRE', linea, columna))
                    elif buffer == 'artista':
                        self.listaTokens.append(Token(buffer, 'ARTISTA', linea, columna))
                    elif buffer == 'ruta':
                        self.listaTokens.append(Token(buffer, 'RUTA', linea, columna))
                    elif buffer == 'genero':
                        self.listaTokens.append(Token(buffer, 'GENERO', linea, columna))
                    elif buffer == 'repetir':
                        self.listaTokens.append(Token(buffer, 'REPETIR', linea, columna))
                    elif buffer == 'anio':
                        self.listaTokens.append(Token(buffer, 'ANIO', linea, columna))
                    else:
                        self.listaErrores.append(Error('Caracter ' + buffer + ' no reconocido en el lenguaje.', 'Léxico', linea, columna))
                        
                    buffer = ''
                    i -= 1
                    columna += 1
                    estado = 0
            
            i += 1

    def impTokens(self):
        print("LISTA DE TOKENS")
        for t in self.listaTokens:
            t.impToken()

    def impErrores(self):
        if len(self.listaErrores) == 0:
            print('No hubo errores')
        else:
            print("LISTA DE ERRORES")
            for e in self.listaErrores:
                e.impError()