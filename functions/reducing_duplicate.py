'''Reducing the duplication of code



You are managing a busy cafe. you want to recieve many orders and want ot print the name of each

customer along with the type of coffee they ordered



Task:



.Write a function print_order(name,coffee_type)

. call it multple times for different customers

'''
def print_order(name, coffee_type):

    print(f"{name} ordered {coffee_type} ")

print_order("Ali","espresso") 
print_order("Aftab","espresso") 

Name=input("Enter your name:")
Coffee=input("Enter your desired coffee:")
print_order(Name,Coffee)

