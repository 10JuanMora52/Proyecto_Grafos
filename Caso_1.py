import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Crear el grafo dirigido
G = nx.DiGraph()

#Convenciones
# Lista de materias con su índice
materias = [
    (1, "Inicio pregrado"),
    (2, "Precalculo"),
    (3, "Pensamiento matemático"),
    (4, "Programación de computadores"),
    (5, "Lógica TNC"),
    (6, "Análisis de textos"),
    (7, "Ética"),
    (8, "Cátedra rosarista"),
    (9, "Cálculo 1"),
    (10, "Física 1"),
    (11, "Algoritmos y estructura de datos"),
    (12, "Lógica para ciencias de la computación"),
    (13, "Escritura de textos"),
    (14, "Constitución política y cívica"),
    (15, "Electiva HM 1"),
    (16, "Cálculo 2"),
    (17, "Álgebra lineal"),
    (18, "Arquitectura del computador"),
    (19, "Cornerstone Project"),
    (20, "Ingeniería de datos"),
    (21, "Electiva HM 2"),
    (22, "Cálculo 3"),
    (23, "Optimización"),
    (24, "Probabilidad y estadística 1"),
    (25, "Teoría de grafos"),
    (26, "Variable compleja"),
    (27, "Ecuaciones diferenciales"),
    (28, "Análisis real"),
    (29, "Probabilidad y estadística 2"),
    (30, "Electiva de profundización 1"),
    (31, "Teoría de la computación"),
    (32, "Topología"),
    (33, "Math modeling"),
    (34, "Análisis estadístico de datos"),
    (35, "Electiva de profundización 2"),
    (36, "Redes de computadores"),
    (37, "Seminario de grado"),
    (38, "Electiva general 1"),
    (39, "Diseño y análisis de algoritmos"),
    (40, "Keystone project"),
    (41, "Álgebra abstracta"),
    (42, "Análisis numérico y computación"),
    (43, "Operating systems"),
    (44, "Electiva de profundización 3"),
    (45, "Trabajo de grado 1"),
    (46, "Electiva general 2"),
    (47, "Geometría"),
    (48, "Electiva de profundización 4"),
    (49, "Electiva de profundización 5"),
    (50, "Capsone project"),
    (51, "Trabajo de grado 2"),
    (52, "Grado"),
]

# Datos de asignaturas: (nombre, costo)
#Costos
costo_2023=475000
costo_2024=523000
costo_2025=576000
costo_2026=634000
costo_2027=698000

# Diccionario que asigna cada asignatura a un semestre
asignaturas = {
    #Fuente
    'X1,0':0,
    #Primer semestre
    'X2,1':1,
    'X3,1':1,
    'X4,1':1,
    'X5,1':1 ,
    'X6,1':1 ,
    'X7,1':1,
    'X8,1':1,
    #Segundo semestre
    'X9,2':2,
    'X10,2':2,
    'X11,2':2,
    'X12,2':2,
    'X13,2':2,
    'X14,2':2,
    'X15,2':2,
    #3er semestre
    'X16,3':3,
    'X17,3':3,
    'X18,3':3,
    'X19,3':3,
    'X20,3':3,
    'X21,3':3,
    #4to semestre
    'X22,4':4,
    'X23,4':4,
    'X24,4':4,
    'X25,4':4,
    #5to semestre
    'X20,5':5,
    'X31,5':5,
    'X26,5':5,
    'X27,5':5,
    'X28,5':5,
    'X29,5':5,
    'X30,5':5,
    #6to semestre
    'X40,6':6,
    'X20,6':6,
    'X39,6':6,
    'X31,6':6,
    'X32,6':6,
    'X33,6':6,
    'X34,6':6,
    'X35,6':6,
    'X36,6':6,
    'X37,6':6,
    'X38,6':6,
    #7mo semestre
    'X40,7':7,
    'X20,7':7,
    'X39,7':7,
    'X31,7':7,
    'X41,7':7,
    'X42,7':7,
    'X43,7':7,
    'X44,7':7,
    'X45,7':7,
    'X46,7':7,
    #8vo semestre
    'X50,8':8,
    'X40,8':8,
    'X20,8':8,
    'X39,8':8,
    'X31,8':8,
    'X47,8':8,
    'X48,8':8,
    'X49,8':8,
    'X51,8':8,
    #9no semestre
    'X50,9':9,
    'X40,9':9,
    'X39,9':9,
    'X47,9':9,
    'X48,9':9,
    'X49,9':9,
    'X51,9':9,
    #10mo semestre
    'X50,10':10,
    'X47,10':10,
    'X48,10':10,
    'X49,10':10,
    'X51,10':10,
    #11vosemestre
    'X52,11':11
}

asignatura_costo = {
    #Fuente
    'X1,0':0,
    #Primer semestre
    'X2,1':costo_2023*3,
    'X3,1':costo_2023*2,
    'X4,1':costo_2023*3,
    'X5,1':costo_2023*3,
    'X6,1':costo_2023*2,
    'X7,1':costo_2023*2,
    'X8,1':costo_2023*2,
    #Segundo semestre
    'X9,2':costo_2023*3,
    'X10,2':costo_2023*3,
    'X11,2':costo_2023*3,
    'X12,2':costo_2023*3,
    'X13,2':costo_2023*2,
    'X14,2':costo_2023*2,
    'X15,2':costo_2023*2,
    #3er semestre
    'X16,3':costo_2024*3,
    'X17,3':costo_2024*3,
    'X18,3':costo_2024*3,
    'X19,3':costo_2024*3,
    'X20,3':costo_2024*3,
    'X21,3':costo_2024*3,
    #4to semestre
    'X22,4':costo_2024*3,
    'X23,4':costo_2024*3,
    'X24,4':costo_2024*3,
    'X25,4':costo_2024*3,
    #5to semestre
    'X20,5':costo_2025*3,
    'X31,5':costo_2025*3,
    'X26,5':costo_2025*3,
    'X27,5':costo_2025*3,
    'X28,5':costo_2025*3,
    'X29,5':costo_2025*3,
    'X30,5':costo_2025*3,
    #6to semestre
    'X40,6':costo_2025*3,
    'X20,6':costo_2025*3,
    'X39,6':costo_2025*3,
    'X31,6':costo_2025*3,
    'X32,6':costo_2025*3,
    'X33,6':costo_2025*3,
    'X34,6':costo_2025*3,
    'X35,6':costo_2025*3,
    'X36,6':costo_2025*3,
    'X37,6':costo_2025*2,
    'X38,6':costo_2025*1,
    #7mo semestre
    'X40,7':costo_2026*3,
    'X20,7':costo_2026*3,
    'X39,7':costo_2026*3,
    'X31,7':costo_2026*3,
    'X41,7':costo_2026*3,
    'X42,7':costo_2026*3,
    'X43,7':costo_2026*3,
    'X44,7':costo_2026*3,
    'X45,7':costo_2026*4,
    'X46,7':costo_2026*2,
    #8vo semestre
    'X50,8':costo_2026*3,
    'X40,8':costo_2026*3,
    'X20,8':costo_2026*3,
    'X39,8':costo_2026*3,
    'X31,8':costo_2026*3,
    'X47,8':costo_2026*3,
    'X48,8':costo_2026*3,
    'X49,8':costo_2026*3,
    'X51,8':costo_2026*4,
    #9no semestre
    'X50,9':costo_2027*3,
    'X40,9':costo_2027*3,
    'X39,9':costo_2027*3,
    'X47,9':costo_2027*3,
    'X48,9':costo_2027*3,
    'X49,9':costo_2027*3,
    'X51,9':costo_2027*4,
    #10mo semestre
    'X50,10':costo_2027*3,
    'X47,10':costo_2027*3,
    'X48,10':costo_2027*3,
    'X49,10':costo_2027*3,
    'X51,10':costo_2027*4,
    #11vosemestre
    'X52,11':1532000
}

# Posición
pos = {
    #Fuente
    'X1,0': (0, 0),
    #Primer semestre
    'X2,1': (5, -3),
    'X3,1': (5, -6),
    'X4,1': (5, -9),
    'X5,1': (5, -12),
    'X6,1': (5, -15),
    'X7,1': (5, -18),
    'X8,1': (5, -21),
    #Segundo semestre
    'X9,2': (15, -3),
    'X10,2': (15, -6),
    'X11,2': (15, -9),
    'X12,2': (15, -12),
    'X13,2': (15, -15),
    'X14,2': (15, -18),
    'X15,2': (15, -21),
    #3er semestre
    'X16,3': (25, -3),
    'X17,3': (25, -6),
    'X18,3': (25, -9),
    'X19,3': (25, -12),
    'X20,3': (25, -15),
    'X21,3': (25, -18),
    #4to semestre
    'X22,4': (35, -3),
    'X23,4': (35, -6),
    'X24,4': (35, -9),
    'X25,4': (35, -12),
    #5to semestre
    'X20,5': (45, -3),
    'X31,5': (45, -6),
    'X26,5': (45, -9),
    'X27,5': (45, -12),
    'X28,5': (45, -15),
    'X29,5': (45, -18),
    'X30,5': (45, -3),
    #6to semestre
    'X40,6': (55, 0),
    'X20,6': (55, -3),
    'X39,6': (55, -6),
    'X31,6': (55, -9),
    'X32,6': (55, -12),
    'X33,6': (55, -15),
    'X34,6': (55, -18),
    'X35,6': (55, -21),
    'X36,6': (55, -24),
    'X37,6': (55, -27),
    'X38,6': (55, -30),
    #7mo semestre
    'X40,7': (65, 0),
    'X20,7': (65, -3),
    'X39,7': (65, -6),
    'X31,7': (65, -9),
    'X41,7': (65, -12),
    'X42,7': (65, -15),
    'X43,7': (65, -18),
    'X44,7': (65, -24),
    'X45,7': (65, -27),
    'X46,7': (65, -30),
    #8vo semestre
    'X50,8': (75, 0),
    'X40,8': (75, -3),
    'X20,8': (75, -6),
    'X39,8': (75, -9),
    'X31,8': (75, -12),
    'X47,8': (75, -15),
    'X48,8': (75, -18),
    'X49,8': (75, -21),
    'X51,8': (75, -24),
    #9no semestre
    'X50,9': (85, 0),
    'X40,9': (85, -3),
    'X39,9': (85, -6),
    'X47,9': (85, -9),
    'X48,9': (85, -12),
    'X49,9': (85, -15),
    'X51,9': (85, -18),
    #10mo semestre
    'X50,10': (95, -3),
    'X47,10': (95, -6),
    'X48,10': (95, -9),
    'X49,10': (95, -12),
    'X51,10': (95, -15),
    #11vosemestre
    'X52,11': (105, 0)
}

# Datos de conexiones entre asignaturas con el estado de aprobación: (origen, destino, aprobado)
conexiones = [
    #Conexion de las materias de primer semestre al nodo fuente
    ('X1,0', 'X2,1', 1),
    ('X1,0', 'X3,1', 1),
    ('X1,0', 'X4,1', 1),
    ('X1,0', 'X5,1', 1),
    ('X1,0', 'X6,1', 1),
    ('X1,0', 'X7,1', 1),
    ('X1,0', 'X8,1', 1),
    #Conexiones de las materias de primer semestre
    ('X2,1', 'X9,2', 1),
    ('X2,1', 'X10,2', 1),
    ('X3,1','X28,5',1),
    ('X3,1','X41,7',1),
    ('X4,1', 'X11,2',1),
    ('X4,1', 'X18,3',1),
    ('X4,1', 'X20,3',1),
    ('X4,1', 'X33,6',1),
    ('X5,1', 'X12,2',1),
    ('X5,1', 'X28,5',1),
    ('X5,1', 'X41,7',1),
    ('X6,1','X52,11',1),
    ('X7,1','X52,11',1),
    ('X8,1','X52,11',1),
    #Conexión de materias de segundo semestre
    ('X9,2','X16,3',1),
    ('X9,2','X17,3',1),
    ('X9,2','X19,3',1),
    ('X10,2','X33,6',1),
    ('X11,2','X19,3',1),
    ('X11,2','X39,6',1),
    ('X11,2','X42,7',1),
    ('X11,2','X43,7',1),
    ('X12,2','X31,5',1),
    ('X12,2','X19,3',1),
    ('X13,2','X52,11',1),
    ('X14,2','X52,11',1),
    ('X15,2','X52,11',1),
    #Conexion de materias prerrequisito 3er semestre
    ('X16,3','X22,4',1),
    ('X16,3','X23,4',1),
    ('X16,3','X24,4',1),
    ('X17,3','X23,4',1),
    ('X17,3','X25,4',1),
    ('X17,3','X27,5',1),
    ('X17,3','X41,7',1),
    ('X17,3','X42,7',1),
    ('X18,3','X43,7',1),
    ('X19,3','X40,6',1),
    ('X20,3','X20,5',0),
    ('X21,3','X52,11',1),

    #Conexion de materias prerrequisito 4to semestre
    ('X22,4','X26,5',1),
    ('X22,4','X27,5',1),
    ('X23,4','X40,6',1),
    ('X24,4','X29,5',1),
    ('X24,4','X40,6',1),
    ('X25,4','X40,6',1),
    #Conexion de materias prerrequisito quinto semestre
    ('X20,5','X40,6',1),
    ('X20,5','X20,7',0),
    ('X31,5','X39,6',1),
    ('X31,5','X31,6',0),
    ('X26,5','X52,11',1),
    ('X27,5','X33,6',1),
    ('X27,5','X42,7',1),
    ('X27,5','X47,9',1),
    ('X28,5','X32,6',1),
    ('X29,5','X33,6',1),
    ('X29,5','X34,6',1),
    ('X30,5','X52,11',1),
    #sexto semestre
    ('X40,6','X50,8',1),
    ('X40,6','X40,7',0),
    ('X20,6','X40,7',1),
    ('X20,6','X20,7',0),
    ('X39,6','X52,11',1),
    ('X39,6','X39,7',1),
    ('X31,6','X39,7',1),
    ('X31,6','X31,7',1),
    ('X37,6','X45,7',1),
    ('X34,6','X52,11',1),
    ('X35,6','X52,11',1),
    ('X36,6','X52,11',1),
    ('X38,6','X52,11',1),
    #Septimo semestre
    ('X40,7','X50,8',1),
    ('X40,7','X40,8',0),
    ('X20,7','X40,8',1),
    ('X20,7','X20,8',0),
    ('X39,7','X50,8',1),
    ('X39,7','X39,8',0),
    ('X31,7','X39,8',1),
    ('X31,7','X31,8',0),
    ('X42,7','X52,11',1),
    ('X43,7','X52,11',1),
    ('X44,7','X52,11',1),
    ('X45,7','X52,11',1),
    ('X46,7','X52,11',1),
    #Octavo semestre
    ('X50,8','X52,11',1),
    ('X50,8','X50,9',0),
    ('X40,8','X50,9',1),
    ('X40,8','X40,9',0),
    ('X20,8','X52,11',1),
    ('X39,8','X52,11',1),
    ('X39,8','X39,9',0),
    ('X31,8','X39,9',1),
    ('X47,8','X52,11',1),
    ('X48,8','X52,11',1),
    ('X49,8','X52,11',1),
    ('X50,8','X52,11',1),
    ('X51,8','X52,11',1),
    #Noveno semestre
    ('X50,9','X52,11',1),
    ('X50,9','X50,10',0),
    ('X40,9','X50,10',1),
    ('X39,9','X52,11',1),
    ('X47,9','X52,11',1),
    ('X48,9','X52,11',1),
    ('X49,9','X52,11',1),
    ('X50,9','X52,11',1),
    ('X51,9','X52,11',1),
    #Decimo semestre
    ('X50,10','X52,11',1),
    ('X47,10','X52,11',1),
    ('X48,10','X52,11',1),
    ('X49,10','X52,11',1),
    ('X50,10','X52,11',1),
    ('X51,10','X52,11',1)    
]

# Configurar etiquetas para los nodos
labels_nodos = {
    nodo: f"{asignaturas[nodo]} ({asignatura_costo[nodo]})\nSem: {datos['semestre']}"
    for nodo, datos in G.nodes(data=True)
}

# Configurar colores de las aristas según el estado de aprobación
colores_aristas = [
    "green" if datos["aprobado"] == 1 else "red" 
    for _, _, datos in G.edges(data=True)
]

# Crear nodos y aristas
# Agregar nodos al grafo con etiquetas que incluyan el identificador y el costo
for asignatura, semestre in asignaturas.items():
    costo = asignatura_costo[asignatura]
    etiqueta = f"{asignatura}\nCosto: {costo}"
    G.add_node(asignatura, label=etiqueta, semestre=semestre)

arista_colores = []
for origen, destino, aprobado in conexiones:
    G.add_edge(origen, destino)
    arista_colores.append('green' if aprobado == 1 else 'red')

# Dibujar grafo
nx.draw(G, pos, labels=nx.get_node_attributes(G, 'label'), with_labels=True, node_size=1000, node_color='lightblue', font_size=8, font_weight='bold', edge_color=arista_colores, arrows=True )
plt.show()

#codigo para la visualizacion de la tabla 
# Convertir la lista en un DataFrame para facilidad
df = pd.DataFrame(materias, columns=["Índice", "Materia"])

# Crear la figura
fig, ax = plt.subplots(figsize=(10, 15))

# Ocultar los ejes
ax.axis("tight")
ax.axis("off")

# Crear la tabla
tabla = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc="center",
    loc="center",
)

# Ajustar el diseño
tabla.auto_set_font_size(False)
tabla.set_fontsize(10)
tabla.auto_set_column_width(col=list(range(len(df.columns))))

# Mostrar la tabla
plt.show()
