def group_by_owners(files):
    myfiles=sorted(files.items())
    mydic={}    
    for x in myfiles:
        if (mydic != {}) and (x[1] in  mydic):
#         #list use ectend to add new element
          mydic[x[1]].extend( [x[0]])
          #print( dc, [x[0]])  
        else:  
          ##Dictionay uses update to add element 
           mydic.update({x[1]:[x[0]]})       
    return mydic

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))