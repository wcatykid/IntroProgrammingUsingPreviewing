import math

def roots(fltA, fltB, fltC):
    """Computes and prints the roots of a quadratic polynomial: ax^2 + bx + c
       @input: fltA -- a in the expression ax^2 + bx + c
       @input: fltB -- b in the expression ax^2 + bx + c
       @input: fltC -- c in the expression ax^2 + bx + c
       @output: No output; the result is printed
       @Restrictions: None
    """
    
    # Compute the discriminant of the quadratic formula
    fltDiscriminant = fltB * fltB - 4 * fltA * fltC    
    
    # Check if roots are imaginary: no roots
    if fltDiscriminant < 0:
        print ('None')    
        return    
    
    # One unique root
    if fltDiscriminant == 0:    
        print ('x =', -fltB / (2 * fltA))
        return

    # Compute the two roots
    fltX_1 = (-fltB + math.sqrt(fltDiscriminant)) / (2 * fltA)
    fltX_2 = (-fltB - math.sqrt(fltDiscriminant)) / (2 * fltA)

    # Report two roots
    print ('x1 =', fltX_1)
    print ('x2 =', fltX_2)


def test():
    #
    # Call the function with three input values: a, b, c
    #
    floatA = 1
    floatB = -2
    floatC = -3
    print(str(floatA) + "x^2 + " + str(floatB) + "x + " + str(floatC) + ":")
    roots(floatA, floatB, floatC)

    print()

    floatA = 1
    floatB = 0
    floatC = 0
    print(str(floatA) + "x^2 + " + str(floatB) + "x + " + str(floatC) + ":")
    roots(floatA, floatB, floatC)

# Invokes the testing function
if __name__ == "__main__":
    test()
