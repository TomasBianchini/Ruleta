from test import runsTest, monobit_test, chi_test
from graph import plot_scatter, create_bitmap_image
import random 
def generatorLGC(seed, mult, mod,inc, m) -> list:
    # Linear congruential generator
    numbers = [seed] # No se si es necesario agregar la semilla a la lista
    for i in range(m):
        next_number = ((mult*numbers[i])+inc) % mod
        numbers.append(next_number)
    return numbers
h = generatorLGC(1, 1664525, 2**32 , 1013904223,10)
print(h)
h2 = runsTest(h)
print('Runs Test Linear Congrutial Generator=',h2)
h3 = monobit_test(h)
print('Monibit Test Linear Congrutial Generator=',h3)


# Metodo de los cuadrados medios #
def AlgorithmMiddleSquare(seed: int, n: int) -> list:
    if len(str(seed)) < 4:
        raise ValueError("Seed should be at least 4 digits long")
    r_i = []
    X_n = seed
    D = len(str(seed))   
    for i in range(n):
        X_n = X_n ** 2
        str_X_n = str(X_n).zfill(2 * D)
        middle_digits = str_X_n[D//2 : D + D//2] 
        X_n = int(middle_digits)
        r_i.append(X_n / (10 ** D))
    return r_i

h = AlgorithmMiddleSquare(5735, 100)
print(h)
h2 = runsTest(h)
print('Runs Test Middle Square=',h2)
h3 = monobit_test(h)
print('Monibit Test Middle Square=',h3)
h4 = chi_test(h, 10, 0.05)
print('Chi Test Middle Square=',h4)
plot_scatter(h, color=(0, 0, 0), alpha=0.5, title='Scatter plot', xlabel='x', ylabel='y')

# Generar números pseudoaleatorios usando tu generador LCG
lcg_numbers = generatorLGC(1, 1664525, 2**32, 1013904223, 512 * 512)
#print(lcg_numbers)
# Crear una imagen de bitmap a partir de los números generados
create_bitmap_image(lcg_numbers, 512, 512, "lcg_bitmap.png")

# Generar números pseudoaleatorios usando el método Middle Square
middle_square_numbers = AlgorithmMiddleSquare(8217, 512 * 512)
#print(middle_square_numbers)
# Crear una imagen de bitmap a partir de los números generados
create_bitmap_image(middle_square_numbers, 512, 512, "middle_square_bitmap.png")
