def sum_func(*args):
    sum_even = 0
    
    for num in args:
        if num % 2 == 0:
            sum_even += num
    
    return sum_even

# Тестове
print(sum_func(1, 4, 5))               
print(sum_func(4, 5, 6, 1, 3))         
print(sum_func(2, 20, 10, 15, 28, 3, 1))