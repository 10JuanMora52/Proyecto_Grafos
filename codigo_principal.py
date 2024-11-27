import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo dirigido
G = nx.DiGraph()

# Datos de asignaturas: (nombre, costo)
#Costos
costo_2023=475000
costo_2024=523000
costo_2025=576000
costo_2026=634000
costo_2027=698000

asignaturas = {
    'Inicio pregrado': 0,
    'Precalculo': costo_2023*3,
    'Pensamiento matematico': costo_2023*2,
    'Programacion de computadores': costo_2023*3,
    'Logica TNC': costo_2023*3,
    'Analisis de textos': costo_2023*2,
    'Etica': costo_2023*2,
    'Catedra rosarista': costo_2023*2,
    'Calculo 1': costo_2023*3,
    'Fisica 1': costo_2023*3,
    'Algoritmos y estructura de datos': costo_2023*3,
    'Logica para ciencias de la computacion': costo_2023*3,
    'Escritura de textos': costo_2023*2,
    'Constitución politica y civica': costo_2023*2,
    'Electiva HM 1': costo_2023*3,
    'Calculo 2': costo_2024*3,
    'Algebra lineal': costo_2024*3,
    'Arquitectura del computador': costo_2024*3,
    'Teoria de la computacion': costo_2024*3,
    'Cornerstone Project': costo_2024*3,
    'Ingenieria de datos': costo_2024*3,
    'Calculo 3': costo_2024*3,
    'Optimizacion': costo_2024*3,
    'Diseño y analisis de algoritmos': costo_2024*3,
    'Probabilidad y estadistica 1': costo_2024*3,
    'Teoria de grafos': costo_2024*3,
    'Electiva HM 2': costo_2024*3,
    'Variable compleja': costo_2025*3,
    'Ecuaciones diferenciales': costo_2025*3,
    'Analisis real': costo_2025*3,
    'Probabilidad y estadistica 2': costo_2025*3,
    'Keystone project': costo_2025*3,
    'Electiva de profundizacion 1': costo_2025*3,
    'Topologia': costo_2025*3,
    'Math modeling': costo_2025*3,
    'Analisis estadistico de datos': costo_2025*3,
    'Electiva de profundizacion 2': costo_2025*3,
    'Redes de computadores': costo_2025*3,
    'Seminario de grado': costo_2025*1,
    'Electiva general 1': costo_2025*2,
    'Algebra abstracta': costo_2026*3,
    'Analisis numerico y computacion': costo_2026*3,
    'Operating systems': costo_2026*3,
    'Electiva de profundizacion 3': costo_2026*3,
    'Trabajo de grado 1': costo_2026*4,
    'Electiva general 2': costo_2026*2,
    'Geometria': costo_2026*3,
    'Electiva de profundizacion 4': costo_2026*3,
    'Electiva de profundizacion 5': costo_2026*3,
    'Capsone project': costo_2026*3,
    'Trabajo de grado 2': costo_2026*4,
    'Grado': 1532000,
}

# Posición
pos = {
    'Inicio pregrado': (0, 0),
    'Precalculo': (5, -3),
    'Pensamiento matematico': (5, -6),
    'Programacion de computadores': (5, -9),
    'Logica TNC': (5, -12),
    'Analisis de textos': (5, -15),
    'Etica': (5, -18),
    'Catedra rosarista': (5, -21),
    'Calculo 1': (10, -3),
    'Fisica 1': (10, -6),
    'Algoritmos y estructura de datos': (10, -9),
    'Logica para ciencias de la computacion': (10, -12),
    'Escritura de textos': (10, -15),
    'Constitución politica y civica': (10, -18),
    'Electiva HM 1': (10, -21),
    'Calculo 2': (15, -3),
    'Algebra lineal': (15, -6),
    'Arquitectura del computador': (15, -9),
    'Teoria de la computacion': (15, -12),
    'Cornerstone Project': (15, -15),
    'Ingenieria de datos': (15, -18),
    'Calculo 3': (20, -3),
    'Optimizacion': (20, -6),
    'Diseño y analisis de algoritmos': (20, -9),
    'Probabilidad y estadistica 1': (20, -12),
    'Teoria de grafos': (20, -15),
    'Electiva HM 2': (20, -18),
    'Variable compleja': (25, -3),
    'Ecuaciones diferenciales': (25, -6),
    'Analisis real': (25, -9),
    'Probabilidad y estadistica 2': (25, -12),
    'Keystone project': (25, -15),
    'Electiva de profundizacion 1': (25, -18),
    'Topologia': (30, -3),
    'Math modeling': (30, -6),
    'Analisis estadistico de datos': (30, -9),
    'Electiva de profundizacion 2': (30, -12),
    'Redes de computadores': (30, -15),
    'Seminario de grado': (30, -18),
    'Electiva general 1': (30, -21),
    'Algebra abstracta': (35, -3),
    'Analisis numerico y computacion': (35, -6),
    'Operating systems': (35, -9),
    'Electiva de profundizacion 3': (35, -12),
    'Trabajo de grado 1': (35, -15),
    'Electiva general 2': (35, -18),
    'Geometria': (40, -3),
    'Electiva de profundizacion 4': (40, -6),
    'Electiva de profundizacion 5': (40, -9),
    'Capsone project': (40, -12),
    'Trabajo de grado 2': (40, -15),
    'Grado': (45, 0)
}

# Diccionario que asigna cada asignatura a un semestre
semestre_asignatura = {
    'Inicio pregrado': 0,
    'Precalculo': 1,
    'Pensamiento matematico': 1,
    'Programacion de computadores': 1,
    'Logica TNC': 1,
    'Analisis de textos': 1,
    'Etica': 1,
    'Catedra rosarista': 1,
    'Calculo 1': 2,
    'Fisica 1': 2,
    'Algoritmos y estructura de datos': 2,
    'Logica para ciencias de la computacion': 2,
    'Escritura de textos': 2,
    'Constitución politica y civica': 2,
    'Electiva HM 1': 2,
    'Calculo 2': 3,
    'Algebra lineal': 3,
    'Arquitectura del computador': 3,
    'Teoria de la computacion': 3,
    'Cornerstone Project': 3,
    'Ingenieria de datos': 3,
    'Calculo 3': 4,
    'Optimizacion': 4,
    'Diseño y analisis de algoritmos': 4,
    'Probabilidad y estadistica 1': 4,
    'Teoria de grafos': 4,
    'Electiva HM 2': 4,
    'Variable compleja': 5,
    'Ecuaciones diferenciales': 5,
    'Analisis real': 5,
    'Probabilidad y estadistica 2': 5,
    'Keystone project': 5,
    'Electiva de profundizacion 1': 5,
    'Topologia': 6,
    'Math modeling': 6,
    'Analisis estadistico de datos': 6,
    'Electiva de profundizacion 2': 6,
    'Redes de computadores': 6,
    'Seminario de grado': 6,
    'Electiva general 1':6,
    'Algebra abstracta': 7,
    'Analisis numerico y computacion': 7,
    'Operating systems': 7,
    'Electiva de profundizacion 3': 7,
    'Trabajo de grado 1': 7,
    'Electiva general 2': 7,
    'Geometria': 8,
    'Electiva de profundizacion 4': 8,
    'Electiva de profundizacion 5': 8,
    'Capsone project': 8,
    'Trabajo de grado 2': 8,
    'Grado': 9,
}

# Datos de conexiones entre asignaturas con el estado de aprobación: (origen, destino, aprobado)
conexiones = [
    #Conexion de las materias de primer semestre al nodo fuente
    ('Inicio pregrado', 'Precalculo', 1),
    ('Inicio pregrado', 'Pensamiento matematico', 1),
    ('Inicio pregrado', 'Programacion de computadores', 1),
    ('Inicio pregrado', 'Logica TNC', 1),
    ('Inicio pregrado', 'Etica', 1),
    ('Inicio pregrado', 'Catedra rosarista', 1),
    #Conexiones de las materias de primer semestre
    ('Precalculo', 'Calculo 1', 1),
    ('Precalculo', 'Fisica 1', 1),
    ('Pensamiento matematico','Analisis real',1),
    ('Pensamiento matematico','Algebra abstracta',1),
    ('Programacion de computadores', 'Algoritmos y estructura de datos',1),
    ('Programacion de computadores', 'Arquitectura del computador',1),
    ('Programacion de computadores', 'Ingenieria de datos',1),
    ('Programacion de computadores', 'Math modeling',1),
    ('Logica TNC', 'Logica para ciencias de la computacion',1),
    ('Logica TNC', 'Analisis real',1),
    ('Logica TNC', 'Algebra abstracta',1),
    ('Analisis de textos','Grado',1),
    ('Etica','Grado',1),
    ('Catedra rosarista','Grado',1),
    #Conexión de materias de segundo semestre
    ('Calculo 1','Calculo 2',1),
    ('Calculo 1','Algebra lineal',1),
    ('Calculo 1','Cornerstone Project',1),
    ('Fisica 1','Math modeling',1),
    ('Algoritmos y estructura de datos','Cornerstone Project',1),
    ('Algoritmos y estructura de datos','Diseño y analisis de algoritmos',1),
    ('Algoritmos y estructura de datos','Analisis numerico y computacion',1),
    ('Algoritmos y estructura de datos','Operating systems',1),
    ('Logica para ciencias de la computacion','Teoria de la computacion',1),
    ('Logica para ciencias de la computacion','Cornerstone Project',1),
    ('Escritura de textos','Grado',1),
    ('Constitución politica y civica','Grado',1),
    ('Electiva HM 1','Grado',1),
    #Conexion de materias prerrequisito 3er semestre
    ('Calculo 2','Calculo 3',1),
    ('Calculo 2','Optimizacion',1),
    ('Calculo 2','Probabilidad y estadistica 1',1),
    ('Algebra lineal','Optimizacion',1),
    ('Algebra lineal','Teoria de grafos',1),
    ('Algebra lineal','Ecuaciones diferenciales',1),
    ('Algebra lineal','Algebra abstracta',1),
    ('Algebra lineal','Analisis numerico y computacion',1),
    ('Arquitectura del computador','Operating systems',1),
    ('Teoria de la computacion','Diseño y analisis de algoritmos',1),
    ('Cornerstone Project','Keystone project',1),
    ('Ingenieria de datos','Keystone project',1),
    #Conexion de materias prerrequisito 4to semestre
    ('Calculo 3','Variable compleja',1),
    ('Calculo 3','Ecuaciones diferenciales',1),
    ('Optimizacion','Keystone project',1),
    ('Probabilidad y estadistica 1','Probabilidad y estadistica 2',1),
    ('Probabilidad y estadistica 1','Keystone project',1),
    ('Teoria de grafos','Keystone project',1),
    #No son prerrequisito
    ('Diseño y analisis de algoritmos','Grado',1),
    ('Electiva HM 2','Grado',1),
    #Conexion de materias prerrequisito quinto semestre
    ('Ecuaciones diferenciales','Math modeling',1),
    ('Ecuaciones diferenciales','Analisis numerico y computacion',1),
    ('Ecuaciones diferenciales','Geometria',1),
    ('Analisis real','Topologia',1),
    ('Probabilidad y estadistica 2','Math modeling',1),
    ('Probabilidad y estadistica 2','Analisis estadistico de datos',1),
    ('Keystone project','Capsone project',1),
    #No son prerrequisito
    ('Variable compleja','Grado',1),
    ('Electiva de profundizacion 1','Grado',1),
    #sexto semestre
    ('Topologia','Geometria',1),
    ('Math modeling','Capsone project',1 ),
    ('Seminario de grado','Trabajo de grado 1',1),
    #No son prerrequisitos
    ('Analisis estadistico de datos','Grado',1),
    ('Electiva de profundizacion 2','Grado',1),
    ('Redes de computadores','Grado',1),
    ('Electiva general 1','Grado',1),
    #Septimo semestre
    #No son prerrequisito
    ('Algebra abstracta','Grado',1),
    ('Analisis numerico y computacion','Grado',1),
    ('Operating systems','Grado',1),
    ('Electiva de profundizacion 3','Grado',1),
    ('Trabajo de grado 1','Grado',1),
    ('Electiva general 2','Grado',1),
    #Octavo semestre
    ('Geometria','Grado',1),
    ('Electiva de profundizacion 4','Grado',1),
    ('Electiva de profundizacion 5','Grado',1),
    ('Capsone project','Grado',1),
    ('Trabajo de grado 2','Grado',1)
]

# Agregar nodos y aristas (con atributos)
for asignatura, costo in asignaturas.items():
    G.add_node(asignatura, costo=costo, estado=1)  # Estado inicial aprobado (1)

for origen, destino, aprobado in conexiones:
    G.add_edge(origen, destino, aprobado=aprobado)

# Configurar nodo desaprobado
print("¿Que materia desaprobaste?:")
nodo_desaprobado = input ()  # Simular la materia desaprobada
G.nodes[nodo_desaprobado]['estado'] = 0  # 0 indica desaprobado

# Función para obtener todos los nodos afectados por la desaprobación
def obtener_nodos_afectados(grafo, nodo):
    afectados = set()
    pila = [nodo]  # Usamos una pila para recorrer los sucesores

    while pila:
        actual = pila.pop()
        if actual not in afectados:
            afectados.add(actual)
            for sucesor in grafo.successors(actual):
                if grafo.nodes[sucesor].get("estado", 1) == 1:  # Solo afecta si no está aprobado
                    pila.append(sucesor)
    return afectados

# Identificar nodos afectados y aristas correspondientes
nodos_afectados = obtener_nodos_afectados(G, nodo_desaprobado)
aristas_afectadas = [
    (origen, destino) for origen, destino in G.edges() if origen in nodos_afectados
]

# Crear etiquetas detalladas para los nodos
numero_asignatura = {asignatura: i + 1 for i, asignatura in enumerate(asignaturas.keys())}
labels_nodos = {
    nodo: f"{numero_asignatura[nodo]} ({semestre_asignatura[nodo]}° Sem)\nCosto: {datos['costo']}" 
    for nodo, datos in G.nodes(data=True)
}

# Colorear nodos
color_nodos = [
    "red" if nodo in nodos_afectados else "green" for nodo in G.nodes()
]

# Colorear aristas
color_aristas = [
    "red" if (origen, destino) in aristas_afectadas else "green" 
    for origen, destino in G.edges()
]

# Dibujar el grafo con números en los nodos
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, labels=labels_nodos, node_size=500, node_color=color_nodos, font_size=8, font_weight='bold', edge_color=color_aristas, arrows=True)

# Crear la tabla de convenciones
plt.figure(figsize=(5, 10))  # Aumentar el ancho de la figura para la tabla
plt.axis('off')
table_data = [(i+1, asignatura) for i, asignatura in enumerate(asignaturas.keys())]
table = plt.table(cellText=table_data, colLabels=['Número', 'Asignatura'], cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Ajustar el ancho de las columnas
table.auto_set_column_width([0, 1])  # Ajusta automáticamente el ancho de las columnas
table[0, 0].set_width(0.1)  # Ajusta manualmente el ancho de la columna del número
table[0, 1].set_width(0.8)  # Ajusta manualmente el ancho de la columna de la asignatura

# Mostrar el grafo y la tabla
plt.show()
