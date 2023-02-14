n = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for x in range (0, n + 1):  
    if x > 0:  
        for i in range (2, x):  
            if (x % i) == 0:  
                break 
            else:  
              print (x)  