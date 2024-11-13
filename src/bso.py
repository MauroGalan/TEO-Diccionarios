'''
@author: reinaqu
'''

def crear_dicc_titulos_anyos(bsos:list[tuple[str,int]])->dict[str, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los títulos y como valores los años
    :rtype: {str:int}
    '''
    res = {}
    for titulo,año in bsos:
        res[titulo] = año
    return res

def crear_dicc_titulos_anyos2(bsos:list[tuple[str,int]])->dict[str, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los títulos y como valores los años
    :rtype: {str:int}
    '''
    #Definir por comprensión
    return{titulo:año for titulo,año in bsos}

def crear_dicc_anyos_conteo_titulos (bsos:list[tuple[str,int]])->dict[int, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los años y como valores el número de títulos
          de ese año
    :rtype: {int:int}
    '''
    res = {}
    for titulo, año in bsos:
        if año not in res:
            res[año]=0
        res[año]+=1
    return res

#Es equivalente a lo siguiente, usando el counter que te cuenta por ti.
from collections import Counter
def crear_dicc_años_conteo_COUNTER(bsos):
    return Counter(año for titulo,año in bsos)

def crear_dicc_anyos_lista_titulos (bsos:list[tuple[str,int]])->dict[int, list[str]]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los años y como valores una lista con los títulos
          de ese año
    :rtype:{int:[str]}
    '''
    res={}
    for titulo,año in bsos:
        if año not in res:
            res[año] = []
        res[año].append(titulo)
    return res

#Tiene un tipo determinado inicializado el valor neutro, list = [], set = {}, int = 0...
from collections import defaultdict
def crear_dicc_años_lista_defaultdict(bsos):
    res= defaultdict(list)
    for titulo, año in bsos:
        res[año].append(titulo)
    return res

def crear_dicc_anyos_conteo_titulos_defaultdict (bsos:list[tuple[str,int]])->dict[int, int]:
    res = defaultdict(int)
    for titulo, año in bsos:
        res[año]+=1
    return res


def obtener_clave_mayor(dicc_bso:dict[str,int])->str:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: La clave con valor mayor, segun el orden natural
    :rtype: str
    '''
    pass

def obtener_valor_mayor(dicc_bso:dict[str,int])->int:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: El valor mayor, que en este caso es el año más reciente.
    :rtype: int
    '''
    pass

def obtener_nombre_mas_largo(dicc_bso:dict[str,int])->str:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: El nombre de la canción con más caracteres
    :rtype: str
    '''
    pass