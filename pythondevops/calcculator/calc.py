def compound_interest(principal,rate,time):
 
    Amount = principal*(pow((1+rate/100),time))
    CI = Amount-principal
    return print (CI)
  
    
 
 
print (compound_interest(1000,5,2))
