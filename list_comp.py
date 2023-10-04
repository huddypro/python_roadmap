numbers = [40, 45, 23, 87, 75, 78, 65, 46, 58, 76, 18, 94]
even_num = [num for num in numbers if num % 2 == 0]
'''for num in numbers:
    if num % 2 == 0:
        even_num.append(num)'''

print(even_num)


#exercise 2

square = [x ** 2 for x in range(1, 10)]
'''for x in range(1, 10):
    sqr = x ** 2
    square.append(sqr)'''

print(square)

#exercise 3

colors = ['Red', 'Blue', 'Green', 'Black', 'White']
sec_colors = [color.upper() for color in colors]
'''for color in colors:
    sec_colors.append(color.upper())'''

print(sec_colors)