user_entry = int(input("Please enter the fibnocci term count:"))
firstprevious = 2
secondprevious = 1
fibnocci_series=[1,2]
for x in range(user_entry):  
    new_term = firstprevious + secondprevious
    secondprevious = firstprevious
    firstprevious  = new_term
    fibnocci_series.append(new_term)
print(fibnocci_series)
ans=sum(x for x in list(fibnocci_series))
print("sum of all fibnocci terms is", ans)