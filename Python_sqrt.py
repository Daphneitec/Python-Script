import math
def find_roots(a,b,c):

    r1 = int(( ( -1 * b + math.sqrt((b**2-4*a*c))   ) / (2*a) ) )
    r2= int(( ( -1 * b - math.sqrt((b**2-4*a*c))   ) / (2*a) ) )  
    myt = (r1,r2)

    if ( r1==r2 ):
        myt =  r1   
    return myt

print(find_roots(2, 10, 8));  