def add_to_n(input_n):
  i = 1 
  sum = 0
  for i in range(n+1):
     sum = sum + i
     i = i+1
  return sum   
if __name__ == '__main__' :
  n=10
  print(add_to_n(n))