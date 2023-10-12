def outer_function(person , coins):
    #coins = 3
    def inner_function():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print("\n"+ person + " is left with " + str(coins) + " coins")
        elif coins == 1:
            print("\n"+ person + " is left with " + str(coins) + " coins")
        else:
            print("\n" + person + " is out of coins")
    return inner_function

huddy = outer_function("huddy", 5)
huddy()
huddy()

#Exercise
def all_numbers():
    sqr=[]
    def square_numbers():
        nonlocal sqr
        number = input("Enter your number: ")
        for num in number:
            try:
                num = int(num)
                sqr.append(num ** 2)
            except ValueError:
                print(f"skipping invalide input: {num}")
        return sqr
    return square_numbers
cal_square_num = all_numbers()

result = cal_square_num()
print("sqaures of the numbers: ", result)



