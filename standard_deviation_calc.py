import math

# With the input being a list of numbers, it calculates the range, average, variance, and standard deviation.

def find_standard_deviation(inputs):
    inputss = inputs
    summ = 0
    average = 0
    print(f"Range: {max(inputss) - min(inputss)}")
    for x in inputss:
        average += x
    print(f"Average: {average/len(inputss)}" )
    for x in inputss:
        summ += ((x - average/(len(inputs))) ** 2)
    variance = summ /(len(inputs) -1)
    print(f"Sum for Variance: {summ}")
    print(f"Variance: {variance}")
    print(f"Standard deviation: {math.sqrt(variance)}")
    
    for i in inputss:
        temp = float(i - 78.55)
        print(f"({temp})^2")

find_standard_deviation([68, 79, 95, 48, 73, 95, 92, 62, 59, 88, 77, 82, 83, 97, 99, 92, 90, 42, 63, 87])

# find_standard_deviation([67, 45, 52, 36, 78, 61, 46, 52, 61, 54]) 




