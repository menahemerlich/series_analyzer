
series = []

def create_series():
    while len(series) < 3:
        num = input('Rules:\n '
                    'You must enter at least 3 numbers.\n'
                    'All numbers must be positive (> 0).\n '
                    'Separate the numbers using spaces.')

        ech = num.split(" ")
        for i in ech:
            if i.replace('.','').isdigit() and float(i) > 0:
                series.append(float(i))
        if len(series) == len(ech):
            return series
        else:
            series.clear()
            print('Incorrect input! Try again.. ')
create_series()
print(series)
def sert_series(series):
    len_list = len(series)
    for i in range(len_list - 1):
        for j in range(len_list - i - 1):
            if series[j] > series[j + 1]:
                series[j], series[j + 1] = series[j + 1], series[j]
    return series

def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

def sum_parameter(list):
    sum = 0
    for i in list:
        sum += i
    return sum

while True:
    print("==Series Analyzer - Menu==\n "
          "1. Input a new series\n "
          "2. Display the series\n "
          "3. Display the series\n "
          "4. Display the series\n "
          "5. Display the Max value\n "
          "6. Display the Min value\n "
          "7. Display the average value\n "
          "8. Display the number of elements\n "
          "9. Display the Sum of the series\n "
          "0. Exit")
    choice = input('enter your choice.. ')
    if choice == "1":
        series = []
        create_series()
    elif choice == "2":
        print(series)
    elif choice == "3":
        print(series[::-1])
    elif choice == "4":
        print(sert_series(series))
    elif choice == "5":
        print(max(series))
    elif choice == "6":
        print(min(series))
    elif choice == "7":
        print(average(series))
    elif choice == "8":
        print(len(series))
    elif choice == "9":
        print(sum_parameter(series))
    elif choice == "0":
        break
    else:
        print("Syntax error! ")
