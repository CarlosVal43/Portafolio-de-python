mivariablefb = 1

def mi_funcion(variable):
    return variable + 1

while mivariablefb < 100:
    mivariablefb = mi_funcion(mivariablefb)

    if  mivariablefb % 3 == 0 and mivariablefb % 5 == 0:
        print("FIZZBUZZ")

    elif mivariablefb % 5 == 0:
        print("BUZZ")
    
    elif mivariablefb % 3 == 0:
        print("FIZZ!!")

    else:
        print(mivariablefb)
