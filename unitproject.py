def arearectangle(a,b):
    """
    solve the area of the rectangle
    :param a: heigth
    :param b: with
    :return: return the fucntion to do it more times
    """
    return a*b

def withh():# dpuble (h) because dosent let me put one # with called by the user
    """
    make the user tell the with
    :return: the function so we know the number and we can make the calculation
    """
    a=float(input("what is the with"))
    return a

def lenght():# lenght called by the user
    """
    user called the lenght
    :return: return the function to make the calculations
    """
    b=float(input("what is the lenght"))
    return b

def height():# height called by the user
    """
    user called height
    :return: return the function to make the claculations
    """
    c=float(input("what ois the height"))
    return c

def instructions():
    print("this is gonna calculate the surace area of a rectangle with the length, with and height choosed by the user")

def calculations():#surface area calculations
    a =withh()
    b=lenght()
    c=height()
    top=arearectangle(a,b)
    bottom=arearectangle(b,a)
    front=arearectangle(c,b)
    back=arearectangle(b,c)
    left=arearectangle(c,a)
    right=arearectangle(a,c)
    total=top+bottom+right+left+front+back
    instructions()
    print(total)
calculations()
