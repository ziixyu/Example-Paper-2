import math

x = 1.2
H = [1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4]

for h in H:
    one_side_diff = (math.sin(x + h) - math.sin(x)) / h
    symm_diff = (math.sin(x + h) - math.sin(x - h)) / (2 * h)

    print("h =", h)
    print(" One-side error: {:.2e}".format(abs(one_side_diff - math.cos(x))))
    print(" Symmetric error: {:.2e}".format(abs(symm_diff - math.cos(x))))
