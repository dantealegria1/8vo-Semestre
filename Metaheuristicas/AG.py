"""
MIEMBROS DEL EQUIPO
ANDREA MARGARITA BALANDRAN FELIX
DANTE ALEJANDRO ALEGRIA ROMERO
DIEGO ALBERTO 'BETO' ARANDA GONZALEZ
"""
import random
import numpy as np

class AlgoritmoGenetico:
    """
    Implementación de un Algoritmo Genético para maximizar el número de unos en una cadena binaria.
    El algoritmo utiliza selección por torneo, cruzamiento de un punto, mutación y elitismo.
    """
    def __init__(self):
        # Parámetros principales del algoritmo
        self.BIT_COUNT = 50          # Longitud de cada individuo (cromosoma)
        self.POPULATION_SIZE = 100     # Número de individuos en la población
        self.MAX_GENERATIONS = 100    # Máximo número de generaciones a ejecutar
        self.TOURNAMENT_SIZE = 10      # Número de individuos que participan en cada torneo
        self.MUTATION_RATE = 0.2      # Probabilidad de mutación (10% de los bits)
        self.DEGRADATION = 0.9  # Umbral de degradación permitida (90% del fitness del padre)
        self.STAGNATION_LIMIT = 20    # Número de generaciones sin mejora antes de parar
        
    def generate_random_individual(self):
        """
        Genera un individuo aleatorio como una lista de bits (0s y 1s).
        Returns:
            list: Lista de bits aleatorios de longitud BIT_COUNT
        """
        return [random.randint(0, 1) for i in range(self.BIT_COUNT)]
    
    def calculate_fitness(self, individual):
        """
        Calcula el fitness de un individuo sumando todos sus unos.
        Args:
            individual (list): Lista de bits que representa al individuo
        Returns:
            int: Número total de unos en el individuo
        """
        return sum(individual)
    
    def tournament_selection(self, population):
        """
        Realiza la selección por torneo, escogiendo el mejor individuo de un grupo aleatorio.
        Favoreciendo la explotacion de buenas soluciones en lugar de la exploracion
        Args:
            population (list): Lista de individuos de la población actual
        Returns:
            list: El individuo ganador del torneo
        """
        tournament = random.sample(population, self.TOURNAMENT_SIZE)
        return max(tournament, key=self.calculate_fitness)
    
    def single_point_crossover(self, parent1, parent2):
        """
        Realiza el cruzamiento de un punto entre dos padres.
        Args:
            parent1 (list): Primer padre
            parent2 (list): Segundo padre
        Returns:
            tuple: Par de hijos resultantes del cruzamiento
        """
        point = random.randint(1, self.BIT_COUNT - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    
    def mutate(self, individual):
        """
        Aplica mutación a un individuo, cambiando aleatoriamente algunos de sus bits.
        Aqui favorecemos la exploracion
        Args:
            individual (list): Individuo a mutar
        Returns:
            list: Individuo mutado
        """
        num_mutations = int(self.BIT_COUNT * self.MUTATION_RATE)
        mutated = individual.copy()
        for _ in range(num_mutations):
            pos = random.randint(0, self.BIT_COUNT - 1)
            mutated[pos] = 1 - mutated[pos]  # Invierte el bit en la posición seleccionada
        return mutated
    
    def accept_offspring(self, parent_fitness, child_fitness):
        """
        Decide si aceptar un hijo basado en el umbral de degradación permitido.
        Esto para mantener un estandar en las soluciones sin quedarnos en optimos locales
        Args:
            parent_fitness (int): Fitness del padre
            child_fitness (int): Fitness del hijo
        Returns:
            bool: True si el hijo es aceptado, False en caso contrario
        """
        if child_fitness >= parent_fitness * self.DEGRADATION:
            return True
        return False
    
    def run(self):
        """
        Ejecuta el algoritmo genético completo.
        Returns:
            tuple: (best_fitness_history, avg_fitness_history) - Historiales de fitness
        """
        # Crear población inicial aleatoria
        population = [self.generate_random_individual() for i in range(self.POPULATION_SIZE)]
        best_fitness_history = []  # Almacena el mejor fitness de cada generación
        avg_fitness_history = []   # Almacena el fitness promedio de cada generación
        
        generations_without_improvement = 0
        best_fitness_ever = float('-inf')
        
        # Bucle principal de evolución
        for generation in range(self.MAX_GENERATIONS):
            new_population = []
            
            # Generar nueva población
            while len(new_population) < self.POPULATION_SIZE:
                # Seleccionar padres mediante torneo
                parent1 = self.tournament_selection(population)
                parent2 = self.tournament_selection(population)
                
                # Calcular fitness de los padres
                fitness_p1 = self.calculate_fitness(parent1)
                fitness_p2 = self.calculate_fitness(parent2)
                
                # Generar hijos mediante cruzamiento
                child1, child2 = self.single_point_crossover(parent1, parent2)
                
                # Aplicar mutación a los hijos
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                
                # Calcular fitness de los hijos
                fitness_c1 = self.calculate_fitness(child1)
                fitness_c2 = self.calculate_fitness(child2)
                
                # Aplicar política de reemplazo con degradación permitida
                if self.accept_offspring(fitness_p1, fitness_c1):
                    new_population.append(child1)
                else:
                    new_population.append(parent1)
                    
                # Verificar si hay espacio para el segundo hijo
                if len(new_population) < self.POPULATION_SIZE:
                    if self.accept_offspring(fitness_p2, fitness_c2):
                        new_population.append(child2)
                    else:
                        new_population.append(parent2)
            
            # Ajustar tamaño de la población si es necesario
            population = new_population[:self.POPULATION_SIZE]
            
            # Calcular y almacenar estadísticas de la generación
            fitness_values = [self.calculate_fitness(ind) for ind in population]
            current_best_fitness = max(fitness_values)
            avg_fitness = sum(fitness_values) / len(fitness_values)            
            best_individual = max(population, key=self.calculate_fitness)

            best_fitness_history.append(current_best_fitness)
            avg_fitness_history.append(avg_fitness)
            
            # Verificar si hay mejora en el fitness
            if current_best_fitness > best_fitness_ever:
                best_fitness_ever = current_best_fitness
                generations_without_improvement = 0
            else:
                generations_without_improvement += 1
            
            # Mostrar progreso de la evolución
            print(f"Generación {generation + 1}:")
            print(f"Mejor Fitness: {current_best_fitness}")
            print(f"Fitness Promedio: {avg_fitness:.2f}")
            print(f"Generaciones sin mejora: {generations_without_improvement}")
            print("Mejor individuo:", best_individual)
            print("-" * 50)
            
            # Verificar criterios de parada
            if current_best_fitness == self.BIT_COUNT:
                print("¡Solución óptima encontrada!")
                break
            
            if generations_without_improvement >= self.STAGNATION_LIMIT:
                print(f"¡Algoritmo detenido por estancamiento después de {self.STAGNATION_LIMIT} generaciones sin mejora!")
                break
        
        return best_fitness_history, avg_fitness_history


if __name__ == "__main__":
    ag = AlgoritmoGenetico()
    best_fitness_history, avg_fitness_history = ag.run()
