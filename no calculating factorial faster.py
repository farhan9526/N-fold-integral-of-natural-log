from fractions import Fraction
import timeit
#import resource

def f(x):
    return Fraction(1, x)

n = int(input('Enter the number of iterations: '))

# Measure execution time
start_time = timeit.default_timer()

c = Fraction(0, 1)
for x in range(1, n):
    c -= f(x)

# Calculate elapsed time
end_time = timeit.default_timer()
elapsed_time = end_time - start_time

print("Result:", c)
print("Time taken:", elapsed_time, "seconds")

x_power = n - 1
factorial_n_minus_1 = '({}!)'.format(n - 1)
ln_x_c = '(ln(x{})'.format(c)

expression = '(x**{}/{})*{}'.format(x_power, factorial_n_minus_1, ln_x_c)

# Get peak memory usage
#peak_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 if hasattr(resource, 'RUSAGE_SELF') else 1024 * 1024)

print("Expression:", expression)
#print("Peak memory usage:", peak_memory, "MB")
