# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def pow_numbers (n):
    x=1
    arr=[]
    for i in range(1,n+1):
        x=i*x
        arr.append(x)
    return arr
print(pow_numbers(6))