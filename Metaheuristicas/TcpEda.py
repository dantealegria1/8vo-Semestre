import random
import numpy as np

class TspEda:
    def __init__(self):
        # Ciudad de inicio y fin
        self.START_END_CITY = 1
        
        # Ciudades
        self.cities = np.array([
            [78.1, 45.6],  # Ciudad 0
            [55.4, 78.2],  # Ciudad 1
            [34.8, 12.3],  # Ciudad 2
            [67.9, 89.5],  # Ciudad 3
            [23.4, 45.7],  # Ciudad 4
            [78.9, 30.2],  # Ciudad 5
            [45.3, 24.8],  # Ciudad 6
            [90.1, 82.3],  # Ciudad 7
            [12.7, 85.4],  # Ciudad 8
            [36.2, 96.7],  # Ciudad 9
            [58.9, 54.3],  # Ciudad 10
            [41.5, 70.6],  # Ciudad 11
            [87.3, 39.5]   # Ciudad 12
        ])
        
        # Actualizar el numero de ciudades para que coincida con el tamano real del array
        self.NUM_CITIES = len(self.cities)
        
        # Otros parametros
        self.POPULATION_SIZE = 100  
        self.MAX_GENERATIONS = 100 
        self.STAGNATION_LIMIT = 21      
        self.TOP_SELECTION = 30        
        
        # Calcular matriz de distancias entre ciudades
        self.distance_matrix = self.calculate_distance_matrix()
        
        # Validar que la ciudad de inicio/fin este dentro del rango
        if self.START_END_CITY >= self.NUM_CITIES:
            print(f"Error: La ciudad de inicio/fin ({self.START_END_CITY}) esta fuera de rango. Ajustando a ciudad 0.")
            self.START_END_CITY = 0
    
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
        """Genera una ruta aleatoria como permutacion de ciudades, 
        asegurando que inicie y termine en la ciudad especificada."""
        # Crear lista de ciudades excluyendo la ciudad de inicio/fin
        cities = list(range(self.NUM_CITIES))
        cities.remove(self.START_END_CITY)
        
        # Aleatorizar el orden de las ciudades restantes
        random.shuffle(cities)
        
        # Crear ruta que comienza en START_END_CITY
        route = [self.START_END_CITY] + cities
        
        return np.array(route)
    
    def generate_initial_population(self):
        """Genera una poblacion inicial de rutas aleatorias."""
        return [self.generate_random_individual() for _ in range(self.POPULATION_SIZE)]
    
    def calculate_fitness(self, individual):
        """Calcula el fitness de una ruta como la distancia total recorrida.
        Menor distancia = mejor fitness.
        Ahora consideramos explicitamente el retorno a la ciudad de inicio."""
        total_distance = 0
        for i in range(len(individual) - 1):
            from_city = individual[i]
            to_city = individual[i + 1]
            total_distance += self.distance_matrix[from_city, to_city]
        
        # Anadir distancia de retorno a la ciudad de inicio
        total_distance += self.distance_matrix[individual[-1], self.START_END_CITY]
        
        return total_distance
    
    def probability_matrix(self, population):
        """
        Calcula una matriz de probabilidades para cada par de ciudades
        basado en las mejores rutas de la poblacion actual.
        """
        # Seleccionar los mejores individuos (menor distancia = mejor)
        top_individuals = sorted(population, key=self.calculate_fitness)[:self.TOP_SELECTION]
        
        # Inicializar matriz de frecuencias
        freq_matrix = np.zeros((self.NUM_CITIES, self.NUM_CITIES))
        
        # Contar frecuencias de conexiones entre ciudades
        for route in top_individuals:
            for i in range(len(route) - 1):
                from_city = route[i]
                to_city = route[i + 1]
                freq_matrix[from_city, to_city] += 1
            
            # Anadir conexion de la ultima ciudad a la ciudad de inicio
            freq_matrix[route[-1], self.START_END_CITY] += 1
        
        # Normalizar para obtener probabilidades
        prob_matrix = np.where(np.sum(freq_matrix, axis=1, keepdims=True) > 0, 
                       freq_matrix / np.sum(freq_matrix, axis=1, keepdims=True), 
                       0)
        
        return prob_matrix
    
    def generate_child(self, prob_matrix):
        """
        Genera una nueva ruta usando la matriz de probabilidades.
        La ruta siempre comienza en la ciudad especificada.
        """
        # La ruta siempre comienza en la ciudad especificada
        route = [self.START_END_CITY]
        remaining_cities = set(range(self.NUM_CITIES))
        remaining_cities.remove(self.START_END_CITY)
        
        current_city = self.START_END_CITY
        
        # Construir la ruta seleccionando ciudades segun las probabilidades
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
                # Si todas las probabilidades son cero, usar seleccion uniforme
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
            
            # Generar nuevos individuos y aplicar seleccion
            new_population = []
            for parent in population:
                child = self.generate_child(prob_matrix)
                selected = self.acceptance(child, parent)
                new_population.append(selected)
            
            # Actualizar poblacion
            population = new_population
            
            # Evaluar mejor individuo (el de menor distancia)
            best_individual = min(population, key=self.calculate_fitness)
            current_best_fitness = self.calculate_fitness(best_individual)
            
            # Guardar historial de fitness
            fitness_history.append(current_best_fitness)
            
            print(f"Generacion {generation + 1}:")
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
        print(f"Nota: La ruta comienza y termina en la ciudad {self.START_END_CITY}")
        
        # Visualizar la ruta si matplotlib esta disponible
        return best_route, best_fitness
    
# Ejecutar el algoritmo
if __name__ == "__main__":
    tsp_solver = TspEda()
    best_route, best_distance = tsp_solver.run()
