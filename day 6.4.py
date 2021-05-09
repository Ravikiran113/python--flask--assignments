def palindromeNumbers(list_a): 
  
    c = 0
  
     
    for i in list_a:             
        t = i 
        rev = 0
        while t > 0: 
            rev = rev * 10 + t % 10
            t = t // 10
        if rev == i: 
            print (i) 
            c = c + 1
    print()
    print ("Total palindrome nos. are", c )
    print()
def main(): 
  
    list_a = [10, 121, 133, 155, 141, 252] 
    palindromeNumbers (list_a)
  
if __name__=="__main__": 
    main()           