def unique_names(names1, names2):
    mylist = []
    myname = names1+names2
    
    for x in myname:
        if x not in mylist:
          mylist = mylist + [x] 
    return mylist

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia