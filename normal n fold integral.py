import sympy as sp
import timeit
import psutil
		
		# Define the symbol
x = sp.symbols('x')
		
		# Define the function you want to integrate
func = 1 / x
		
		# Define the number of iterations (n)
n = int(input('Enter the number of iterations: '))
		
		# Measure execution time
start_time = timeit.default_timer()
		
integrated_func = func
for _ in range(n):
    integrated_func = sp.integrate(integrated_func, x)
		
		# Calculate elapsed time
end_time = timeit.default_timer()
elapsed_time = end_time - start_time
		
		# Calculate memory usage
process = psutil.Process()
memory_usage = process.memory_info().rss / (1024 ** 2)  # in megabytes
		
		# Print the result of n-fold integration
print(f"{n}-fold Indefinite integration:", integrated_func)
		
		# Print the time taken
print("Time taken:", elapsed_time, "seconds")
		
		# Print the memory usage
print("Memory usage:", memory_usage, "MB")
