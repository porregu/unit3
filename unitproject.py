def arearectangle(a,b):
   return a*b



a=7#with
b=8#length
c=9#height

def calculations():#surface area calculations
    top=arearectangle(3,4)
    bottom=arearectangle(3,4)
    front=arearectangle(9,4)
    back=arearectangle(9,4)
    left=arearectangle(9,3)
    right=arearectangle(9,3)
    total=top+bottom+right+left+front+back
    print(total)
calculations()


