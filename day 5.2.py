def Series(n, m):
  
    
  
    str_n = str(n)
  
    sums = n
    sum_str = str(n)
  
    for i in range(1, m):
         
        sum_str = sum_str + str_n
          
        sums = sums + int(sum_str)
  
    return sums
  

n = 2
m = 5
total = Series(n, m)
print(total)