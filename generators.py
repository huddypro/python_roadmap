def fentch_line(file_name):
    with open(file_name) as file:
        lines = []
        for line in file:
            lines.append(line)
        return lines
huddy = fentch_line("hudson.txt")
print(huddy)

#Generators
def fentch_line(file_name):
    with open(file_name) as file:
        for line in file:
            yield line
huddy = fentch_line("hudson.txt")
print(next(huddy))