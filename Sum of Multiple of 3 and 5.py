user_rage=int(input("enter the number for which sum of 3 or 5 factors  is to be calculated"))

def factorlist(user_input):
    factor_list = []
    for incrementor in range(1,user_input):
        if (incrementor%3 == 0 or incrementor%5 == 0):
            factor_list.append(incrementor) 
#    print(factor_list) 
    total = 0
    for counter in (factor_list):
        total = counter + total
    print(total) 
    
    return(factor_list)
   
#this definition is not working. need to check how to pass a list which is returned from another funciton. in this case passed from factorlist 
# def factorsum(factor_lists):
#     print("entered factor lists")
#     total = 0
#     for counter in (factor_lists):
#         total = counter + total
#     print(total)    

factorlist(user_rage)
# print(factor_list)
# print("before callinig factor lists", factor_list)
# factorsum(factor_list)    

