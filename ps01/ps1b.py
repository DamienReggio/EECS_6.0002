###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

import time
# Problem 1
def dp_make_weight(egg_weights, target_weight, step = 0, memo = {0 : 0}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # memo will be the number of eggs for a given weight
    # 1 : 1
    # 2 : 2 (1,1)
    # 4 : 5 (1, 1, 1, 1)
    # 5 : 1 (5)
    # 10: 1 (10)
    # 15 : 2 (10 , 5)
    # 24 : 6 (10, 10, 1, 1, 1, 1) (this needs to be seen as 10 and 10 and 4
    # 25 : 1 (25)
    #
    # how do I stop it from going to 26?
    # preload memo with target weights
    #
    # so brute force is to try all combonations
    # n
    # start bottom up?
    num_eggs = 0

    try:
        # need to take care of remaining_weight?
        #print("looked up a value!")
        return memo[target_weight] # this is the number of eggs
    except KeyError:
        for remaining_weight in range(1, target_weight+1):
            for weight in reversed(egg_weights):
                if weight <= remaining_weight:
                    remaining_weight_less = remaining_weight - weight
                    num_eggs = 1 + dp_make_weight(egg_weights, remaining_weight_less, memo)
                    memo[remaining_weight] = num_eggs
                    #print("mid", memo)
                    break
                    #return num_eggs
                
    #print('end', memo)
    return num_eggs #this will not fire
    

def dp_make_weight_recursive(egg_weights, target_weight, step = 0, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    remaining_weight = target_weight
    num_eggs = 0

    if target_weight in egg_weights:
        #print("1 step is: ", step)
        return 1
    elif remaining_weight == 0: # this should never fire
        print("0 step is: ", step)
        return 0
    else:
        for weight in reversed(egg_weights):
            if weight <= remaining_weight:
                remaining_weight_less = remaining_weight - weight
                num_eggs += 1 + dp_make_weight(egg_weights, remaining_weight_less, step + 1)
                return num_eggs
            

def dp_make_weight_greedy(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    best_number = target_weight # this should always be the WORST solution 1 * target_weight
    remaining_weight = target_weight
    # brute force
    #
    number_eggs = 0
    while remaining_weight > 0:
        for weight in reversed(egg_weights):
            if weight <= remaining_weight:
                remaining_weight -= weight
                number_eggs += 1
                break

    best_number = number_eggs

    return(best_number)

    

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    #egg_weights = range(1,100000)
    n = 9999999
    #n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    start = time.time()
    print("Actual output:", dp_make_weight(egg_weights, n))
    end = time.time()
    print("it took: ", end - start)
    start = time.time()
    print("Actual GREEDY output:", dp_make_weight_greedy(egg_weights, n)) # greedy will be more efficent always?
    end = time.time()
    print("it took: ", end - start)
    print()
