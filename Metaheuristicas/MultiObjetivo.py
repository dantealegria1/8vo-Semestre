import numpy as np
import pandas as pd
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.operators.sampling.rnd import IntegerRandomSampling
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.visualization.scatter import Scatter

# Definir el problema de optimización multi-objetivo
class SeleccionComputadora(ElementwiseProblem):
    def __init__(self, computadoras):
        """
        Inicializa el problema de selección de computadora.
        
        Parameters:
        -----------
        computadoras : pandas.DataFrame
            DataFrame con las columnas: 'id', 'precio', 'ram', 'procesador', 'almacenamiento'
        """
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
        
        # Definir los objetivos (queremos minimizar estos valores)
        # Para RAM, procesador y almacenamiento, usamos el negativo ya que queremos maximizarlos
        out["F"] = np.array([
            precio,          # Minimizar precio
            -ram,            # Maximizar RAM
            -procesador,     # Maximizar procesador
            -almacenamiento  # Maximizar almacenamiento
        ])

# Generar datos de ejemplo (computadoras con diferentes características)
def generar_datos_ejemplo(n_computadoras=50):

    np.random.seed(42)  # Para reproducibilidad
    
    # Generar datos aleatorios para cada característica
    ids = np.arange(n_computadoras)
    
    # Precios entre 500 y 3000
    precios = np.random.uniform(500, 3000, n_computadoras)
    
    # RAM entre 4 y 64 GB
    ram = np.random.choice([4, 8, 16, 32, 64], n_computadoras)
    
    # Procesador (puntuación entre 1000 y 3000, mayor es mejor)
    procesador = np.random.uniform(1000, 3000, n_computadoras)
    
    # Almacenamiento entre 256 y 2048 GB
    almacenamiento = np.random.choice([256, 512, 1024, 2048], n_computadoras)
    
    # Crear DataFrame
    df = pd.DataFrame({
        'id': ids,
        'precio': precios,
        'ram': ram,
        'procesador': procesador,
        'almacenamiento': almacenamiento
    })
    
    return df

# Función principal
def main():
    # Generar datos de ejemplo
    computadoras = generar_datos_ejemplo(50)
    print("Datos de las computadoras generados:")
    print(computadoras.head())
    
    # Crear el problema
    problema = SeleccionComputadora(computadoras)
    
    # Configurar el algoritmo NSGA-II
    algorithm = NSGA2(
        pop_size=100,
        sampling=IntegerRandomSampling(),
        crossover=SBX(prob=0.8, eta=15, vtype=int),
        mutation=PM(eta=20, vtype=int),
        eliminate_duplicates=True
    )
    
    # Ejecutar la optimización
    res = minimize(
        problema,
        algorithm,
        ('n_gen', 100),
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
    
    # Ordenar por relación precio/prestaciones (suma ponderada normalizada)
    # Normalizar los valores para que estén en la misma escala
    computadoras_norm = computadoras_optimas.copy()
    computadoras_norm['precio_norm'] = (computadoras_optimas['precio'] - computadoras_optimas['precio'].min()) / (computadoras_optimas['precio'].max() - computadoras_optimas['precio'].min())
    computadoras_norm['ram_norm'] = (computadoras_optimas['ram'] - computadoras_optimas['ram'].min()) / (computadoras_optimas['ram'].max() - computadoras_optimas['ram'].min())
    computadoras_norm['procesador_norm'] = (computadoras_optimas['procesador'] - computadoras_optimas['procesador'].min()) / (computadoras_optimas['procesador'].max() - computadoras_optimas['procesador'].min())
    computadoras_norm['almacenamiento_norm'] = (computadoras_optimas['almacenamiento'] - computadoras_optimas['almacenamiento'].min()) / (computadoras_optimas['almacenamiento'].max() - computadoras_optimas['almacenamiento'].min())
    
    # Calcular puntuación para diferentes perfiles de usuario
    computadoras_norm['puntuacion_equilibrada'] = (
        -computadoras_norm['precio_norm'] + 
        computadoras_norm['ram_norm'] + 
        computadoras_norm['procesador_norm'] + 
        computadoras_norm['almacenamiento_norm']
    )
    
    computadoras_norm['puntuacion_economica'] = (
        -2*computadoras_norm['precio_norm'] + 
        0.5*computadoras_norm['ram_norm'] + 
        0.5*computadoras_norm['procesador_norm'] + 
        0.5*computadoras_norm['almacenamiento_norm']
    )
    
    computadoras_norm['puntuacion_alto_rendimiento'] = (
        -0.5*computadoras_norm['precio_norm'] + 
        1.5*computadoras_norm['ram_norm'] + 
        2*computadoras_norm['procesador_norm'] + 
        0.5*computadoras_norm['almacenamiento_norm']
    )
    
    # Recomendaciones para diferentes perfiles
    print("\nTop 3 computadoras con mejor equilibrio precio/rendimiento:")
    top_equilibrado = computadoras_optimas.iloc[computadoras_norm['puntuacion_equilibrada'].argsort()[::-1][:3]]
    print(top_equilibrado[['id', 'precio', 'ram', 'procesador', 'almacenamiento']])
    
    print("\nTop 3 computadoras más económicas con prestaciones aceptables:")
    top_economico = computadoras_optimas.iloc[computadoras_norm['puntuacion_economica'].argsort()[::-1][:3]]
    print(top_economico[['id', 'precio', 'ram', 'procesador', 'almacenamiento']])
    
    print("\nTop 3 computadoras de alto rendimiento:")
    top_rendimiento = computadoras_optimas.iloc[computadoras_norm['puntuacion_alto_rendimiento'].argsort()[::-1][:3]]
    print(top_rendimiento[['id', 'precio', 'ram', 'procesador', 'almacenamiento']])

if __name__ == "__main__":
    main()
