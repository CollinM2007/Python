person1 = int(input("How many slices does person 1 eat?")) 
person2 = int(input("How many slices does person 2 eat?")) 
person3 = int(input("How many slices does person 3 eat?")) 
person4 = int(input("How many slices does person 4 eat?")) 
total_slices = person1 + person2 + person3 + person4 
pizzas = total_slices // 8  
if total_slices % 8 != 0: 
    pizzas = pizzas + 1 
leftover = pizzas * 8 - total_slices 
print("Total slices:", total_slices ) 
print("Pizzas needed:", pizzas) 
print("Leftover slices:", leftover)