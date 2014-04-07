'''
Derived from http://stackoverflow.com/questions/4632322
- Extended to allow float inputs.
- Added an optimization: sort numbers in descending order first
  -> As the algorithm cycles to the next number at a given index when
       the sum thus far exceeds the target, starting with the largest numbers
       means that we'll be able to cycle forward earlier

The whole global thing at the start of each method could use a tidy
'''
from decimal import *

exact_match = False
iterations = 0
closest_list = []
closest_amount = []
closest_absdiff = []

original_numbers = numbers[:]
original_index_order_decimals = numbers[:]

def subset_sum(numbers,target):
    global iterations
    global closest_list
    global closest_amount
    global closest_absdiff
    global original_numbers
    global original_index_order_decimals
    original_numbers = numbers[:]
    numbers = [Decimal(str(x)) for x in numbers]
    original_index_order_decimals = numbers[:]
    numbers.sort(reverse=True)
    subset_sum_recurse(numbers,Decimal(str(target)))
    if not exact_match:
        closest_list = [original_numbers[original_index_order_decimals.index(num)] for num in closest_list]
        print('Execution finished. No exact match found. Final Details:')
        print('    Iterations: ' + str(iterations))
        print('    Closest Set: ' + str(closest_list))
        print('    Closest Amount: ' + str(closest_amount))
        print('    Closest Absolute Difference: ' + str(closest_absdiff))
    else:
        print('Execution Finished after ' + str(iterations) + ' iterations. Exact match(es) found, see above for details')

def subset_sum_recurse(numbers, target, partial=[]):
    global exact_match
    global iterations
    global closest_list
    global closest_amount
    global closest_absdiff
    s = sum(partial)
    iterations += 1
    if((abs(abs(target) - abs(s))) < closest_absdiff):
        closest_list = partial
        closest_amount = s
        closest_absdiff = abs(abs(target) - abs(s))
    if s == target: 
        exact_match = True
        print('Interim Result - Exact Match found:')
        print('    Iterations: ' + str(iterations))
        print('    Matching Set: ' + str(convert_match_list_to_original_numbers()))
        print('    Amount: ' + str(closest_amount))
    if s >= target:
        return  # if we reach the number why bother to continue
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum_recurse(remaining, target, partial + [n])

def convert_match_list_to_original_numbers():
    global closest_list
    global original_numbers
    global original_index_order_decimals
    return [original_numbers[original_index_order_decimals.index(num)] for num in closest_list]
