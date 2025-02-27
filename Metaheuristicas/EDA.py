import random
import numpy as np

class Eda:
    def __init__(self):
        # Parámetros principales del algoritmo
        self.LINES = 10               # Filas por individuo
        self.COLUMNS = 10              # Columnas por individuo
        self.POPULATION_SIZE = 100    # Número de individuos en la población
        self.MAX_GENERATIONS = 100    # Máximo número de generaciones
        self.STAGNATION_LIMIT = 20    # Límite de generaciones sin mejora
        self.TOP_SELECTION = 10

    def generate_random_individual(self):
        """Genera un individuo aleatorio representado como una matriz binaria."""
        return np.random.randint(0, 2, (self.LINES, self.COLUMNS))

    def generate_initial_population(self):
        """Genera una población inicial de matrices binarias."""
        return [self.generate_random_individual() for _ in range(self.POPULATION_SIZE)]

    def calculate_fitness(self, individual):
        """Calcula el fitness de un individuo como la suma total de 1s."""
        return np.sum(individual)
    
    def probability_per_cell(self, population):
        """Calcula la probabilidad de 1s por celda en la población."""
        top_individuals = sorted(population, key=self.calculate_fitness, reverse=True)[:self.TOP_SELECTION]
        stacked = np.stack(top_individuals)
        return np.mean(stacked, axis=0)  # Promedio de 1s en cada celda

    def generate_child(self, prob_matrix):
        """Genera un nuevo individuo muestreando de la distribución de probabilidades."""
        child = np.random.rand(self.LINES, self.COLUMNS) < prob_matrix  # Muestreo
        return child.astype(int)  # Convertimos a binario

    def acceptance(self, child, parent):
        """Acepta el hijo si tiene mejor fitness, de lo contrario mantiene el padre."""
        return child if self.calculate_fitness(child) > self.calculate_fitness(parent) else parent

    def run(self):
        """Ejecuta el algoritmo EDA."""
        population = self.generate_initial_population()
        best_fitness = 0
        stagnation_counter = 0
        
        for generation in range(self.MAX_GENERATIONS):
            # Estimar probabilidades por celda
            prob_matrix = self.probability_per_cell(population)
            
            # Generar nuevos individuos y aplicar selección
            new_population = []
            for parent in population:
                child = self.generate_child(prob_matrix)
                new_population.append(self.acceptance(child, parent))
            
            # Actualizar población
            population = new_population
            
            # Evaluar mejor individuo
            best_individual = max(population, key=self.calculate_fitness)
            current_best_fitness = self.calculate_fitness(best_individual)
            
            print(f"Generación {generation + 1}:")
            print(f"Mejor Fitness: {current_best_fitness}")
            print(f"Generaciones sin mejora: {stagnation_counter}")
            print("Mejor individuo:")
            print(best_individual)
            print("-" * 50) 

            if current_best_fitness == (self.LINES * self.COLUMNS):
                print("¡Solución óptima encontrada!")
                break
            
            # Criterio de parada por estancamiento
            if current_best_fitness > best_fitness:
                best_fitness = current_best_fitness
                stagnation_counter = 0
            else:
                stagnation_counter += 1
                if stagnation_counter >= self.STAGNATION_LIMIT:
                    print("Criterio de estancamiento alcanzado. Terminando.")
                    break
        
# Ejecutar el algoritmo
eda = Eda()
eda.run()
