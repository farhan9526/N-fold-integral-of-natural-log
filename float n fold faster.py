import timeit
import math
import psutil
def f(x):
    return 1/x
		
		
		
n = int(input('Enter the number of iterations: '))
		
		# Measure execution time
start_time = timeit.default_timer()
c=0.0
for x in range(1, n):
    c -= f(x)
		
		# Calculate elapsed time
end_time = timeit.default_timer()
elapsed_time = end_time - start_time
		
print("Result:", c)
print("Time taken:", elapsed_time, "seconds")
		
x_power = n - 1
factorial_n_minus_1 = math.factorial(n-1)
ln_x_c = '(ln(x+{})'.format(c)
		
expression = '(x**{}/{})*{}'.format(x_power, factorial_n_minus_1, ln_x_c)
		
		
		# Calculate memory usage
process = psutil.Process()
memory_usage = process.memory_info().rss / (1024 ** 2)  # in megabytes
		
print("Expression:", expression)
print("Memory usage:", memory_usage, "MB")
