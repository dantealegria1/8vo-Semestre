#!/bin/bash
:<<'COMMENT'
EXPLANATION
Comparison Operators in Bash:
-gt means "greater than" (Greater Than)
-lt means "less than" (Less Than)
-eq: equals
-ne: not equals
-ge: greater than or equal to
-le: less than or equal to

These are used in bash instead of > and < because:

> and < are used for input/output redirection in bash
-gt and -lt are specifically for numerical comparisons

Ah, that's a great question! In bash, $1, $2, $3, etc. are special 
parameters that refer to the arguments passed to a function or script.

$1 equals 4 (the first argument)
$2 would be the second argument (if there was one)
$0 is special - it refers to the script name itself

So local population=($@) is:

Creating a local array variable named population
Converting all the arguments passed ($@) into an array

$#: Number of arguments passed
$@: All arguments as separate strings
$*: All arguments as a single string
$$: Process ID of the current script
$?: Exit status of the last command

${#individual} gets the length of the string individual
COMMENT
:<<'COMMENT'

CRITERIOS:

Cruzamiento de un solo punto
Seleccion por torneo de 4 individuos
tamaño del individuo 50
Mutacion del 10%
Tamaño de la generacion de 20
Criterio de parada de 100 generaciones
COMANDO TIME <archivo>

COMMENT

# Definición de constantes
BIT_COUNT=50 
POPULATION_SIZE=20  # Tamaño de la población
MAX_GENERATIONS=201  # Número máximo de generaciones
NO_IMPROVEMENT_LIMIT=20 # Límite de generaciones sin mejora

# Función para generar un individuo aleatorio (lista de bits)
generate_random_individual() {
    local individual=""
    for ((i=0; i<BIT_COUNT; i++)); do
        individual+=$((RANDOM % 2))  # Genera un 0 o 1 aleatorio
    done
    echo "$individual"
}

# Función para calcular la aptitud (fitness), contando los "1" en la lista
calculate_fitness() {
    local individual=$1
    local count=0
    for ((i=0; i<BIT_COUNT; i++)); do
        if [ "${individual:$i:1}" = "1" ]; then
            ((count++))
        fi
    done
    echo $count
}

# Selección por torneo de 4 individuos
select_parent() {
    local population=("$@")
    local best_fitness=-1
    local best_individual=""
    local size_tournament=4
    for ((i=0; i<size_tournament; i++)); do
        local idx=$((RANDOM % ${#population[@]}))
        local individual=${population[$idx]}
        local fitness=$(calculate_fitness "$individual")
        if [ $fitness -gt $best_fitness ]; then
            best_fitness=$fitness
            best_individual=$individual
        fi
    done
    echo "$best_individual"
}

# Cruzamiento de un solo punto
crossover() {
    local parent1=$1
    local parent2=$2
    local point=$((RANDOM % (BIT_COUNT - 1) + 1))
    local child1="${parent1:0:$point}${parent2:$point}"
    local child2="${parent2:0:$point}${parent1:$point}"
    echo "$child1|$child2"
}

# Mutación: cambia el 10% de los bits en la lista
mutate() {
    local individual=$1
    local num_mutations=$((BIT_COUNT / 10))
    for ((m=0; m<num_mutations; m++)); do
        local index=$((RANDOM % BIT_COUNT))
        local mutated=""
        for ((i=0; i<BIT_COUNT; i++)); do
            if [ $i -eq $index ]; then
                mutated+=$((1 - ${individual:$i:1}))
            else
                mutated+="${individual:$i:1}"
            fi
        done
        individual=$mutated
    done
    echo "$individual"
}

# Inicialización de la población
population=()
for ((i=0; i<POPULATION_SIZE; i++)); do
    individual=$(generate_random_individual)
    population+=("$individual")
done

no_improvement_count=0
last_best_fitness=-1

# Bucle principal del algoritmo evolutivo
for ((generation=0; generation<MAX_GENERATIONS; generation++)); do
    best_fitness=-1
    best_individual=""
    
    # Encontrar el mejor individuo de la generación actual
    for individual in "${population[@]}"; do
        fitness=$(calculate_fitness "$individual")
        if [ $fitness -gt $best_fitness ]; then
            best_fitness=$fitness
            best_individual=$individual
        fi
    done
    clear    
    echo "Generation $generation: Best Fitness = $best_fitness"
    echo "$best_individual"
    
    # Verificar si se encontró la solución óptima (todos los bits en 1)
    if [ $best_fitness -eq $BIT_COUNT ]; then
        echo "Perfect solution found!"
        echo "$best_individual"
        echo ""
        exit 0
    fi
    
    # Contar generaciones sin mejora
    if [ $best_fitness -le $last_best_fitness ]; then
        ((no_improvement_count++))
    else
        no_improvement_count=0
    fi
    last_best_fitness=$best_fitness
    
    # Creación de la nueva población
    new_population=()
    while [ ${#new_population[@]} -lt $POPULATION_SIZE ]; do
        parent1=$(select_parent "${population[@]}")
        parent2=$(select_parent "${population[@]}")
        
        # Cruzamiento
        children=($(crossover "$parent1" "$parent2"))
        IFS='|' read -r child1 child2 <<< "${children[*]}"
        
        # Mutación
        child1=$(mutate "$child1")
        child2=$(mutate "$child2")
        
        # Agregar hijo mutado si no ha mejorado en muchas generaciones
        if [ $no_improvement_count -ge $NO_IMPROVEMENT_LIMIT ]; then
            new_population+=("$child1" "$child2")
        else
          # Reemplazar el bloque actual de reemplazo con:
fitness_p1=$(calculate_fitness "$parent1")
fitness_p2=$(calculate_fitness "$parent2")
fitness_c1=$(calculate_fitness "$child1")
fitness_c2=$(calculate_fitness "$child2")

# Permitir degradación de hasta 10%
degradation_threshold=$((fitness_p1 * 90 / 100))  # 90% del fitness del padre
if [ $fitness_c1 -ge $degradation_threshold ]; then
    new_population+=("$child1")
else
    new_population+=("$parent1")
fi

degradation_threshold=$((fitness_p2 * 90 / 100))
if [ $fitness_c2 -ge $degradation_threshold ]; then
    new_population+=("$child2")
else
    new_population+=("$parent2")
fi
        fi
    done
    
    # Mantener el tamaño de la población
    population=("${new_population[@]:0:$POPULATION_SIZE}")
done

