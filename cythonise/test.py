# Docs :- https://cython.readthedocs.io/en/latest/index.html
# info at :- https://pythonprogramming.net/introduction-and-basics-cython-tutorial/

import timeit


cy = timeit.timeit('example_cy.test(5)', setup='import example_cy', number=10000)
py = timeit.timeit('example_py.test(5)', setup='import example_py', number=10000)

print(cy, py)
print(py/cy)

# To compile to c
# python setup.py build_ext --inplace

# To get html analysis of interaction between python
# "cython -a basic_cy.pyx"