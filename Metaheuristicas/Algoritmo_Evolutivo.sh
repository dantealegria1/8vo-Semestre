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

# Configuration
MATRIX_SIZE=5  # 5x5 matrix
POPULATION_SIZE=12
MUTATION_RATE=10  # Out of 100
MAX_GENERATIONS=100

# Generate a random 5x5 binary matrix
generate_random_individual() {
    local matrix=""
    for ((i=0; i<MATRIX_SIZE; i++)); do
        local row=""
        for ((j=0; j<MATRIX_SIZE; j++)); do
            row+=$((RANDOM % 2))  # Random 0 or 1
        done
        matrix+="$row "
    done
    echo "$matrix"
}

# Calculate fitness (number of 1s in the matrix)
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

# Tournament selection
select_parent() {
    local population=("$@")
    local best_fitness=-1
    local best_individual=""
    local size_tornament=4
    for ((i=0; i<$size_tornament; i++)); do
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

# Crossover (swap rows between two matrices)
crossover() {
    local parent1=($1)
    local parent2=($2)
    local point=$((RANDOM % (MATRIX_SIZE - 1) + 1))

    local child1=("${parent1[@]:0:$point}" "${parent2[@]:$point}")
    local child2=("${parent2[@]:0:$point}" "${parent1[@]:$point}")

    echo "${child1[*]}|${child2[*]}"
}

# Mutation (flip a random bit in the matrix)
mutate() {
    local matrix=($@)
    local row_idx=$((RANDOM % MATRIX_SIZE))
    local col_idx=$((RANDOM % MATRIX_SIZE))

    local mutated_matrix=()
    for ((i=0; i<MATRIX_SIZE; i++)); do
        local row="${matrix[$i]}"
        if [ $i -eq $row_idx ]; then
            local new_row=""
            for ((j=0; j<MATRIX_SIZE; j++)); do
                if [ $j -eq $col_idx ]; then
                    if [ "${row:$j:1}" = "1" ]; then
                        new_row+="0"
                    else
                        new_row+="1"
                    fi
                else
                    new_row+="${row:$j:1}"
                fi
            done
            mutated_matrix+=("$new_row")
        else
            mutated_matrix+=("$row")
        fi
    done

    echo "${mutated_matrix[*]}"
}

# Initialize population
population=()
for ((i=0; i<POPULATION_SIZE; i++)); do
    individual=$(generate_random_individual)
    population+=("$individual")
done

# Main evolution loop
for ((generation=0; generation<MAX_GENERATIONS; generation++)); do
    # Find best individual in current generation
    best_fitness=-1
    best_individual=""

    for individual in "${population[@]}"; do
        fitness=$(calculate_fitness $individual)
        if [ $fitness -gt $best_fitness ]; then
            best_fitness=$fitness
            best_individual=$individual
        fi
    done

    echo "Generation $generation: Best Fitness = $best_fitness"
    echo "Best Matrix:"
    for row in $best_individual; do echo "$row"; done
    echo ""

    # Check if we found the perfect solution (all 1s)
    if [ $best_fitness -eq $((MATRIX_SIZE * MATRIX_SIZE)) ]; then
        echo "Perfect solution found!"
        exit 0
    fi

    # Create new population
    new_population=()
    while [ ${#new_population[@]} -lt $POPULATION_SIZE ]; do
        parent1=$(select_parent "${population[@]}")
        parent2=$(select_parent "${population[@]}")

        # Crossover
        children=($(crossover "$parent1" "$parent2"))
        IFS='|' read -r child1 child2 <<< "${children[*]}"

        # Mutate children
        child1=$(mutate $child1)
        child2=$(mutate $child2)

        new_population+=("$child1" "$child2")
    done

    # Update population (keep size constant)
    population=("${new_population[@]:0:$POPULATION_SIZE}")
done

