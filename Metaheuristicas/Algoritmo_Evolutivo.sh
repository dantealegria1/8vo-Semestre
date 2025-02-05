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
Mutacion del 10%

COMANDO TIME <archivo>

COMMENT

# Definición de constantes
MATRIX_SIZE=5  # Tamaño de la matriz (5x5)
POPULATION_SIZE=12  # Tamaño de la población
MAX_GENERATIONS=76  # Número máximo de generaciones

# Función para generar un individuo aleatorio (matriz binaria de 5x5)
generate_random_individual() {
    local matrix=""
    for ((i=0; i<MATRIX_SIZE; i++)); do
        local row=""
        for ((j=0; j<MATRIX_SIZE; j++)); do
            row+=$((RANDOM % 2))  # Genera un 0 o 1 aleatorio
        done
        matrix+="$row "
    done
    echo "$matrix"
}

# Función para calcular la aptitud (fitness), contando los "1" en la matriz
calculate_fitness() {
    local matrix=($@)
    local count=0
    for row in "${matrix[@]}"; do
        for ((i=0; i<${#row}; i++)); do
            if [ "${row:$i:1}" = "1" ]; then
                ((count++))
            fi
        done
    done
    echo $count
}

# Selección por torneo de 4 individuos
select_parent() {
    local population=("$@")
    local best_fitness=-1
    local best_individual=""
    local size_tournament=4
    for ((i=0; i<$size_tournament; i++)); do
        local idx=$((RANDOM % ${#population[@]}))
        local individual=${population[$idx]}
        local fitness=$(calculate_fitness $individual)
        
        if [ $fitness -gt $best_fitness ]; then
            best_fitness=$fitness
            best_individual=$individual
        fi
    done
    echo "$best_individual"
}

# Cruzamiento de un solo punto
crossover() {
    local parent1=($1)
    local parent2=($2)
    local point=$((RANDOM % (MATRIX_SIZE - 1) + 1))
    local child1=("${parent1[@]:0:$point}" "${parent2[@]:$point}")
    local child2=("${parent2[@]:0:$point}" "${parent1[@]:$point}")
    echo "${child1[*]}|${child2[*]}"
}

# Mutación: cambia el 10% de los bits en la matriz
mutate() {
    local matrix=($@)
    local num_mutations=$(( (MATRIX_SIZE * MATRIX_SIZE) / 10 ))
    for ((m=0; m<num_mutations; m++)); do
        local row_idx=$((RANDOM % MATRIX_SIZE))
        local col_idx=$((RANDOM % MATRIX_SIZE))
        local mutated_matrix=()
        for ((i=0; i<MATRIX_SIZE; i++)); do
            local row="${matrix[$i]}"
            if [ $i -eq $row_idx ]; then
                local new_row=""
                for ((j=0; j<MATRIX_SIZE; j++)); do
                    if [ $j -eq $col_idx ]; then
                        new_row+=$((1 - ${row:$j:1}))
                    else
                        new_row+="${row:$j:1}"
                    fi
                done
                mutated_matrix+=("$new_row")
            else
                mutated_matrix+=("$row")
            fi
        done
        matrix=("${mutated_matrix[@]}")
    done
    echo "${matrix[*]}"
}

# Inicialización de la población
population=()
for ((i=0; i<POPULATION_SIZE; i++)); do
    individual=$(generate_random_individual)
    population+=("$individual")
done

# Bucle principal del algoritmo evolutivo
for ((generation=0; generation<MAX_GENERATIONS; generation++)); do
    best_fitness=-1
    best_individual=""
    
    # Encontrar el mejor individuo de la generación actual
    for individual in "${population[@]}"; do
        fitness=$(calculate_fitness $individual)
        if [ $fitness -gt $best_fitness ]; then
            best_fitness=$fitness
            best_individual=$individual
        fi
    done
    
    echo "Generation $generation: Best Fitness = $best_fitness"
    echo ""    
    # Verificar si se encontró la solución óptima (matriz llena de 1s)
    if [ $best_fitness -eq $((MATRIX_SIZE * MATRIX_SIZE)) ]; then
        echo "Perfect solution found!"
        for row in $best_individual; do echo "$row"; done
        echo ""
        exit 0
    fi
    
    # Creación de la nueva población
    new_population=()
    while [ ${#new_population[@]} -lt $POPULATION_SIZE ]; do
        parent1=$(select_parent "${population[@]}")
        parent2=$(select_parent "${population[@]}")
        
        # Cruzamiento
        children=($(crossover "$parent1" "$parent2"))
        IFS='|' read -r child1 child2 <<< "${children[*]}"
        
        # Mutación
        child1=$(mutate $child1)
        child2=$(mutate $child2)
        
        # Evaluar si los hijos mejoran a los padres
        fitness_p1=$(calculate_fitness $parent1)
        fitness_p2=$(calculate_fitness $parent2)
        fitness_c1=$(calculate_fitness $child1)
        fitness_c2=$(calculate_fitness $child2)
        
        # Agregar solo si los hijos son mejores o iguales a los padres
        if [ $fitness_c1 -ge $fitness_p1 ]; then
            new_population+=("$child1")
        else
            new_population+=("$parent1")
        fi
        
        if [ $fitness_c2 -ge $fitness_p2 ]; then
            new_population+=("$child2")
        else
            new_population+=("$parent2")
        fi
    done
    
    # Mantener el tamaño de la población
    population=("${new_population[@]:0:$POPULATION_SIZE}")
done

