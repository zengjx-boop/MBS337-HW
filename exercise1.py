nub_list = [20,31,23,41,44,54,36,57,90,11]
def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
for num in nub_list:
    print(num, even_or_odd(num))
