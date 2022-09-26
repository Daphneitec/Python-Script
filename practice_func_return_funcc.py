def pipeline(*funcs):
    global i,x
    i= -1
    def helper(arg):
        global i,x
        i = i + 1
        if i <=  len(funcs) : 
            if i==  len(funcs)  : 
                x=arg
            else:             
                helper(funcs[i](arg))
            return x

    return helper  
#fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)                
fun = pipeline( lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0