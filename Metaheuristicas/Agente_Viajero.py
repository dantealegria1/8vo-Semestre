import random
import numpy as np
import matplotlib.pyplot as plt

class TspEda:
    def __init__(self):
        # Parámetros principales del algoritmo
        self.NUM_CITIES = 20            # Número de ciudades en el problema
        self.POPULATION_SIZE = 100      # Número de individuos en la población
        self.MAX_GENERATIONS = 100      # Máximo número de generaciones
        self.STAGNATION_LIMIT = 21      # Límite de generaciones sin mejora
        self.TOP_SELECTION = 30         # Número de mejores individuos para estimar probabilidades
        
        # Ciudades estáticas (coordenadas x, y)
        self.cities = np.array([
            [82.4, 15.7],  # Ciudad 0
            [25.3, 71.2],  # Ciudad 1
            [46.8, 91.3],  # Ciudad 2
            [64.2, 32.1],  # Ciudad 3
            [37.9, 56.8],  # Ciudad 4
            [92.5, 60.1],  # Ciudad 5
            [15.3, 32.7],  # Ciudad 6
            [78.1, 45.6],  # Ciudad 7
            [55.4, 78.2],  # Ciudad 8
            [34.8, 12.3],  # Ciudad 9
            [67.9, 89.5],  # Ciudad 10
            [23.4, 45.7],  # Ciudad 11
            [78.9, 30.2],  # Ciudad 12
            [45.3, 24.8],  # Ciudad 13
            [90.1, 82.3],  # Ciudad 14
            [12.7, 85.4],  # Ciudad 15
            [36.2, 96.7],  # Ciudad 16
            [58.9, 54.3],  # Ciudad 17
            [41.5, 70.6],  # Ciudad 18
            [87.3, 39.5]   # Ciudad 19
        ])
        
        # Calcular matriz de distancias entre ciudades
        self.distance_matrix = self.calculate_distance_matrix()
    
    def calculate_distance_matrix(self):
        """Calcula la matriz de distancias entre todas las ciudades."""
        n = len(self.cities)
        dist_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i != j:
                    # Distancia euclidiana entre ciudades
                    dist_matrix[i, j] = np.sqrt(np.sum((self.cities[i] - self.cities[j])**2))
        return dist_matrix
    
    def generate_random_individual(self):
        """Genera una ruta aleatoria como permutación de ciudades."""
        route = list(range(self.NUM_CITIES))
        random.shuffle(route)
        return np.array(route)
    
    def generate_initial_population(self):
        """Genera una población inicial de rutas aleatorias."""
        return [self.generate_random_individual() for _ in range(self.POPULATION_SIZE)]
    
    def calculate_fitness(self, individual):
        """Calcula el fitness de una ruta como la distancia total recorrida.
        Menor distancia = mejor fitness."""
        total_distance = 0
        for i in range(len(individual)):
            from_city = individual[i]
            to_city = individual[(i + 1) % len(individual)]  # Vuelve a la primera ciudad
            total_distance += self.distance_matrix[from_city, to_city]
        
        # Devolvemos directamente la distancia total (menor es mejor)
        return total_distance
    
    def probability_matrix(self, population):
        """
        Calcula una matriz de probabilidades para cada par de ciudades
        basado en las mejores rutas de la población actual.

        Se toman las TOP_SELECTION mejores rutas.
        Se cuenta cuántas veces aparecen las conexiones entre ciudades.
        Se normalizan las frecuencias para obtener una matriz de probabilidades

        Se recorren las rutas seleccionadas y, para cada ciudad, se toma la ciudad siguiente en la ruta.
        Se incrementa el contador en la freq_matrix, reflejando la cantidad de veces que esa conexión aparece en las mejores soluciones.

        Se convierte la freq_matrix en una matriz de probabilidades.
        Cada fila representa una ciudad y muestra la probabilidad de moverse a otra ciudad.
        Se normalizan las frecuencias de cada fila dividiendo por la suma de la fila.
        Se usa np.where para evitar divisiones por cero
        """
        # Seleccionar los mejores individuos (menor distancia = mejor)
        top_individuals = sorted(population, key=self.calculate_fitness)[:self.TOP_SELECTION]
        
        # Inicializar matriz de frecuencias
        freq_matrix = np.zeros((self.NUM_CITIES, self.NUM_CITIES))
        
        # Contar frecuencias de conexiones entre ciudades
        for route in top_individuals:
            for i in range(len(route)):
                from_city = route[i]
                to_city = route[(i + 1) % len(route)]
                freq_matrix[from_city, to_city] += 1
        
        # Normalizar para obtener probabilidades
        prob_matrix = np.where(np.sum(freq_matrix, axis=1, keepdims=True) > 0, 
                       freq_matrix / np.sum(freq_matrix, axis=1, keepdims=True), 
                       0)
        
        return prob_matrix
    
    def generate_child(self, prob_matrix):
        """
        Genera una nueva ruta usando la matriz de probabilidades.
        Implementa un algoritmo greedy probabilístico.
        """
        remaining_cities = set(range(self.NUM_CITIES))
        route = []
        
        # Elegir ciudad inicial aleatoriamente
        current_city = random.randint(0, self.NUM_CITIES - 1)
        route.append(current_city)
        remaining_cities.remove(current_city)
        
        # Construir la ruta seleccionando ciudades según las probabilidades
        while remaining_cities:
            probs = prob_matrix[current_city].copy()
            # Poner a cero las probabilidades de ciudades ya visitadas
            for city in range(self.NUM_CITIES):
                if city not in remaining_cities:
                    probs[city] = 0
            
            # Normalizar probabilidades
            if np.sum(probs) > 0:
                probs = probs / np.sum(probs)
            else:
                # Si todas las probabilidades son cero, usar selección uniforme
                probs = np.zeros(self.NUM_CITIES)
                for city in remaining_cities:
                    probs[city] = 1.0 / len(remaining_cities)
            
            # Seleccionar siguiente ciudad
            next_city = np.random.choice(self.NUM_CITIES, p=probs)
            route.append(next_city)
            remaining_cities.remove(next_city)
            current_city = next_city
            
        return np.array(route)
    
    def acceptance(self, child, parent):
        """Acepta el hijo si tiene mejor fitness (menor distancia), de lo contrario mantiene el padre."""
        return child if self.calculate_fitness(child) < self.calculate_fitness(parent) else parent
    
    def run(self):
        """Ejecuta el algoritmo EDA para el TSP."""
        population = self.generate_initial_population()
        best_fitness = float('inf')  # Inicializar con un valor muy alto
        best_route = None
        stagnation_counter = 0
        
        fitness_history = []
        
        for generation in range(self.MAX_GENERATIONS):
            # Estimar matriz de probabilidades
            prob_matrix = self.probability_matrix(population)
            
            # Generar nuevos individuos y aplicar selección
            new_population = []
            for parent in population:
                child = self.generate_child(prob_matrix)
                selected = self.acceptance(child, parent)
                new_population.append(selected)
            
            # Actualizar población
            population = new_population
            
            # Evaluar mejor individuo (el de menor distancia)
            best_individual = min(population, key=self.calculate_fitness)
            current_best_fitness = self.calculate_fitness(best_individual)
            
            # Guardar historial de fitness
            fitness_history.append(current_best_fitness)
            
            print(f"Generación {generation + 1}:")
            print(f"Mejor Fitness (Distancia Total): {current_best_fitness:.2f}")
            print(f"Generaciones sin mejora: {stagnation_counter}")
            print("-" * 50)
            
            # Guardar mejor ruta (menor distancia)
            if current_best_fitness < best_fitness:
                best_fitness = current_best_fitness
                best_route = best_individual.copy()
                stagnation_counter = 0
            else:
                stagnation_counter += 1
                if stagnation_counter >= self.STAGNATION_LIMIT:
                    print("Criterio de estancamiento alcanzado. Terminando.")
                    break
        
        # Imprimir resultados finales
        print("\nResultados finales:")
        print(f"Mejor distancia encontrada: {best_fitness:.2f}")
        print(f"Mejor ruta: {best_route}")
                
        return best_route, best_fitness

# Ejecutar el algoritmo
if __name__ == "__main__":
    tsp_solver = TspEda()
    best_route, best_distance = tsp_solver.run()
