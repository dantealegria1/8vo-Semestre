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
TARGET_LENGTH=10
POPULATION_SIZE=10
MUTATION_RATE=10  # Out of 100
MAX_GENERATIONS=100

# Generate a random binary string of specified length
generate_random_individual() {
    local length=$1
    local result=""
    for ((i=0; i<length; i++)); do
        if [ $((RANDOM % 2)) -eq 0 ]; then
            result="${result}0"
        else
            result="${result}1"
        fi
    done
    echo "$result"
}

# Calculate fitness (number of 1s in the string)
calculate_fitness() {
    local individual=$1
    local count=0
    for ((i=0; i<${#individual}; i++)); do
        if [ "${individual:$i:1}" = "1" ]; then
            ((count++))
        fi
    done
    echo $count
}

# Tournament selection
select_parent() {
    local population=($@)
    local best_fitness=-1
    local best_individual=""
    
    # Tournament size of 3
    for ((i=0; i<3; i++)); do
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

# Single point crossover
crossover() {
    local parent1=$1
    local parent2=$2
    local point=$((RANDOM % (TARGET_LENGTH - 1) + 1))
    
    local child1="${parent1:0:$point}${parent2:$point}"
    local child2="${parent2:0:$point}${parent1:$point}"
    
    echo "$child1 $child2"
}

# Mutation
mutate() {
    local individual=$1
    local result=""
    
    for ((i=0; i<${#individual}; i++)); do
        if [ $((RANDOM % 100)) -lt $MUTATION_RATE ]; then
            # Flip bit
            if [ "${individual:$i:1}" = "1" ]; then
                result="${result}0"
            else
                result="${result}1"
            fi
        else
            result="${result}${individual:$i:1}"
        fi
    done
    
    echo "$result"
}

# Initialize population
population=()
for ((i=0; i<POPULATION_SIZE; i++)); do
    individual=$(generate_random_individual $TARGET_LENGTH)
    population+=("$individual")
done

# Main evolution loop
for ((generation=0; generation<MAX_GENERATIONS; generation++)); do
    # Find best individual in current generation
    best_fitness=-1
    best_individual=""
    for individual in "${population[@]}"; do
        fitness=$(calculate_fitness "$individual")
        if [ $fitness -gt $best_fitness ]; then
            best_fitness=$fitness
            best_individual=$individual
        fi
    done
    
    echo "Generation $generation: Best = $best_individual (Fitness = $best_fitness)"
    
    # Check if we found perfect solution
    if [ $best_fitness -eq $TARGET_LENGTH ]; then
        echo "Perfect solution found!"
        exit 0
    fi
    
    # Create new population
    new_population=()
    while [ ${#new_population[@]} -lt $POPULATION_SIZE ]; do
        # Select parents
        parent1=$(select_parent "${population[@]}")
        parent2=$(select_parent "${population[@]}")
        
        # Crossover
        children=($(crossover "$parent1" "$parent2"))
        
        # Mutate children
        child1=$(mutate "${children[0]}")
        child2=$(mutate "${children[1]}")
        
        new_population+=("$child1" "$child2")
    done
    
    # Update population (keep size constant)
    population=("${new_population[@]:0:$POPULATION_SIZE}")
done

echo "Evolution completed. Best solution: $best_individual"
