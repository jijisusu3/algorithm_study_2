topping_num = int(input())
dough_price, topping_price = map(int, input().split()) 
dough_calorie = int(input()) 
toppings = [] 
for _ in range(topping_num): 
    toppings.append(int(input()))
    
#버블정렬 내림차순
for i in range(len(toppings)):
    for j in range(i,len(toppings)):
        zero = 0
        if toppings[i] < toppings[j]:
            zero = toppings[i]
            toppings[i] = toppings[j]
            toppings[j] = zero
print(toppings)
            

t_kcal = 0 
t_cost = 0 
# 첫값을 넣어줘야함. 안넣는게 나을 수 있음.
result = (dough_calorie + t_kcal)/(dough_price+t_cost) 
for i in toppings: 
    t_kcal += i 
    t_cost += topping_price 
    total = (dough_calorie + t_kcal)/(dough_price+t_cost) 
    if result > total: 
        break
    else:
        result = total
print(result)
