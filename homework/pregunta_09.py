"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    count = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as data:
        for line in data:
            parts = line.strip().split("\t")
            col5 = parts[4]

            pairs = col5.split(",")

            keysInRegistry = set()

            for pair in pairs:
                key, value = pair.split(":")
                keysInRegistry.add(key)

            for key in keysInRegistry:
                if key not in count:
                    count[key] = 0
                count[key] += 1

    return count