
import numpy as np
import pandas as pd
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.operators.sampling.rnd import IntegerRandomSampling
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.visualization.scatter import Scatter

# Este script resuelve un problema de optimización multiobjetivo para seleccionar computadoras 
# considerando cuatro criterios: precio, RAM, procesador y almacenamiento.
# Utiliza el algoritmo NSGA-II para encontrar soluciones óptimas en un frente de Pareto.

# Definir el problema de optimización multi-objetivo
class SeleccionComputadora(ElementwiseProblem):
    def __init__(self, computadoras):
        self.computadoras = computadoras
        # Definimos 1 variable de decisión (el índice de la computadora)
        # y 4 objetivos (precio, RAM, procesador, almacenamiento)
        super().__init__(n_var=1, 
                         n_obj=4, 
                         n_constr=0, 
                         xl=np.zeros(1),
                         xu=np.ones(1) * (len(computadoras) - 1))

    def _evaluate(self, x, out, *args, **kwargs):
        # Convertir la variable de decisión a un índice entero
        idx = int(x[0])
        
        # Obtener los valores de la computadora seleccionada
        precio = self.computadoras.iloc[idx]['precio']
        ram = self.computadoras.iloc[idx]['ram']
        procesador = self.computadoras.iloc[idx]['procesador']
        almacenamiento = self.computadoras.iloc[idx]['almacenamiento']
        
        # Definir los objetivos (queremos minimizar precio y maximizar el resto)
        out["F"] = np.array([
            precio,          # Minimizar precio
            -ram,            # Maximizar RAM
            -procesador,     # Maximizar procesador
            -almacenamiento  # Maximizar almacenamiento
        ])

# Genera un conjunto de computadoras con características aleatorias
# para simular un escenario de selección de computadoras óptimas.
def generar_datos_ejemplo(n_computadoras=50):
    np.random.seed(42)  # Para reproducibilidad
    
    # Generar datos aleatorios para cada característica
    ids = np.arange(n_computadoras)
    precios = np.random.uniform(500, 3000, n_computadoras)  # Precio entre 500 y 3000
    ram = np.random.choice([4, 8, 16, 32, 64], n_computadoras)  # RAM entre 4 y 64 GB
    procesador = np.random.uniform(1000, 3000, n_computadoras)  # Puntuación del procesador
    almacenamiento = np.random.choice([256, 512, 1024, 2048], n_computadoras)  # Almacenamiento en GB
    
    # Crear DataFrame con los datos
    df = pd.DataFrame({
        'id': ids,
        'precio': precios,
        'ram': ram,
        'procesador': procesador,
        'almacenamiento': almacenamiento
    })
    
    return df

# Función principal que ejecuta la optimización y muestra los resultados
def main():
    # Generar datos de ejemplo
    computadoras = generar_datos_ejemplo(50)
    print("Datos de las computadoras generados:")
    print(computadoras.head())
    
    # Crear el problema de selección de computadoras
    problema = SeleccionComputadora(computadoras)
    
    # Configurar el algoritmo NSGA-II con sus parámetros
    algorithm = NSGA2(
        pop_size=100,  # Tamaño de la población
        sampling=IntegerRandomSampling(),
        crossover=SBX(prob=0.8, eta=15, vtype=int),  # Probabilidad de cruce 0.8
        mutation=PM(eta=20, vtype=int),  # Tasa de mutación 20
        eliminate_duplicates=True  # Eliminar soluciones duplicadas
    )
    
    # Ejecutar la optimización con NSGA-II
    res = minimize(
        problema,
        algorithm,
        ('n_gen', 100),  # Número de generaciones
        seed=1,
        verbose=True
    )
    
    # Obtener las soluciones no dominadas (frente de Pareto)
    print("\nNúmero de soluciones óptimas encontradas:", len(res.X))
    
    # Convertir las soluciones a índices enteros
    indices_optimos = [int(x[0]) for x in res.X]
    
    # Mostrar las computadoras óptimas
    computadoras_optimas = computadoras.iloc[indices_optimos]
    print("\nComputadoras óptimas:")
    print(computadoras_optimas)
    
    # Implementar un selector simple para el usuario
    print("\nRecomendación de computadoras según preferencias:")
    
    # Normalización para comparación justa entre características
    computadoras_norm = computadoras_optimas.copy()
    for col in ['precio', 'ram', 'procesador', 'almacenamiento']:
        computadoras_norm[col + '_norm'] = (computadoras_optimas[col] - computadoras_optimas[col].min()) / \
                                           (computadoras_optimas[col].max() - computadoras_optimas[col].min())
    
    # Calcular puntuaciones para diferentes perfiles de usuario
    computadoras_norm['puntuacion_equilibrada'] = (
        -computadoras_norm['precio_norm'] + computadoras_norm['ram_norm'] + 
        computadoras_norm['procesador_norm'] + computadoras_norm['almacenamiento_norm']
    )
    
    computadoras_norm['puntuacion_economica'] = (
        -2 * computadoras_norm['precio_norm'] + 0.5 * computadoras_norm['ram_norm'] + 
        0.5 * computadoras_norm['procesador_norm'] + 0.5 * computadoras_norm['almacenamiento_norm']
    )
    
    computadoras_norm['puntuacion_alto_rendimiento'] = (
        -0.5 * computadoras_norm['precio_norm'] + 1.5 * computadoras_norm['ram_norm'] + 
        2 * computadoras_norm['procesador_norm'] + 0.5 * computadoras_norm['almacenamiento_norm']
    )
    
    # Mostrar las mejores computadoras según diferentes perfiles
    print("\nTop 3 computadoras con mejor equilibrio precio/rendimiento:")
    print(computadoras_optimas.iloc[computadoras_norm['puntuacion_equilibrada'].argsort()[::-1][:3]])
    
    print("\nTop 3 computadoras más económicas con prestaciones aceptables:")
    print(computadoras_optimas.iloc[computadoras_norm['puntuacion_economica'].argsort()[::-1][:3]])
    
    print("\nTop 3 computadoras de alto rendimiento:")
    print(computadoras_optimas.iloc[computadoras_norm['puntuacion_alto_rendimiento'].argsort()[::-1][:3]])

# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
