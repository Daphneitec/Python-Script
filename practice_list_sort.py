
if __name__ == '__main__':
    number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    number_list.sort()

    for i in number_list:
        if i <= 50:
          print(i)
        else:
          mypop = number_list.index(i)  
          #print(number_list.index(i)) 
          break

    del number_list[mypop:len(number_list)]
            
    print(number_list)         