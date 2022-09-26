def pipeline(*funcs):
    global i
    pass
    i= len(funcs)+1
    def helper(arg):
        global i
        i = i-1
        if i >= 0 :
           print('arg:',arg,'len', len(funcs),'i', i)
           if i > 0:
             helper(funcs[3-i](arg))    
                     
    return helper    
#fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)

fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0