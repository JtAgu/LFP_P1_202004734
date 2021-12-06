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
        centinela = '*'
        estado = 0
        separador=4
        codigo_fuente += "@@@@"+centinela
        codigo_fuente=codigo_fuente.replace(" ","")
        #automata
        i = 0

        while i< len(codigo_fuente):
            c = codigo_fuente[i]
            

            if estado == 0:
                if c == '=':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'igual', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '[':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'CorcheteA', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ']':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'CorcheteC', linea, columna))
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
                    self.listaTokens.append(Token(buffer, 'puntocoma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '@':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'arroba', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ' ':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'espacio', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ',':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'coma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '#':
                    buffer += c
                    columna += 1
                    estado = 1
                                  
                elif re.search('\d', c):
                    buffer += c
                    columna += 1
                    estado = 2
                    
                elif re.search('[A-Z]', c):
                    buffer += c
                    columna += 1
                    estado = 3
                
                elif c == '\'' or c == '"':
                    buffer += c
                    columna += 1
                    estado = 4
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
            elif estado == 1:
                if c == ']':
                    self.listaTokens.append(Token(buffer, 'color', linea, columna))
                    self.listaTokens.append(Token(']', 'CorcheteC', (linea+1), columna))
                    buffer = ''
                    columna += 1
                    estado = 0
                else:
                    buffer += c
                    columna += 1
            elif estado == 2:
                if re.search('\d', c):
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, 'entero', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 4:
                if c == '\'' or c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'nombre', linea, columna))
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
                if re.search('[A-Z]', c):
                    buffer += c
                    columna += 1
                else:
                    if buffer == 'TITULO':
                        self.listaTokens.append(Token(buffer, 'TITULO', linea, columna))
                    elif buffer == 'ANCHO':
                        self.listaTokens.append(Token(buffer, 'ANCHO', linea, columna))
                    elif buffer == 'ALTO':
                        self.listaTokens.append(Token(buffer, 'ALTO', linea, columna))
                    elif buffer == 'FILAS':
                        self.listaTokens.append(Token(buffer, 'FILAS', linea, columna))
                    elif buffer == 'COLUMNAS':
                        self.listaTokens.append(Token(buffer, 'COLUMNAS', linea, columna))
                    elif buffer == 'CELDAS':
                        self.listaTokens.append(Token(buffer, 'CELDAS', linea, columna))
                    elif buffer == 'FILTROS':
                        self.listaTokens.append(Token(buffer, 'FILTROS', linea, columna))
                    elif buffer == 'MIRRORY' or buffer == 'DOUBLEMIRROR' or buffer == 'MIRRORX':
                        self.listaTokens.append(Token(buffer, 'FILTRO', linea, columna))
                    elif buffer == 'TRUE' or buffer == 'FALSE':
                        self.listaTokens.append(Token(buffer, 'colorear', linea, columna))
                        
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