def fractional_knapsack(value, weight, capacity):
   
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)] # calling for all values in the same index of
                                                 # value and weight
    index.sort(key=lambda i: ratio[i], reverse=True) # index is sorted acc. to ratio in
                                                    # decreasing order so max value comes at top
    
    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break
 
    return max_value, fractions
  
n = int(input('Enter number of items: '))
value = input('Enter values of the {} item(s) in order: '.format(n)).split()
value = [int(v) for v in value]
weight = input('Enter weights of {} item(s) in order: '.format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input('Enter maximum weight allowed: '))
max_value, fractions = fractional_knapsack(value, weight, capacity)
print('The value of items that can be carried:', max_value)
print('Fractional Knapsack solution:', fractions)