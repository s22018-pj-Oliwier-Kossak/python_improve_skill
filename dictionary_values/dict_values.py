salary = {'ksiegowa': 5000, 'kierowca': 4500, 'recepcjonistka': 4000}

def sum_values(dict):
    sum = 0
    for i in dict.values():
        sum += i
    return sum

print(sum_values(salary))

print(sum(salary.values()))