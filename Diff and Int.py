def differentiate():  # doesn't work
    coefficients = []
    powerx = int(input("Please enter the highest power of x: "))
    coefficients.append(0)
    for i in range(1, powerx + 1):
        coefficients.append(int(input("Enter the coefficient for x^{}: ".format(i))))
    for i in range(1, powerx + 1):
        coefficients[i] = coefficients[i] * i
    for i in range(powerx):
        print("{}x^{}".format(coefficients[i], i))


def integrate():  # doesn't work!
    coefficients = []
    powerx = int(input("Please enter the highest power of x: "))
    coefficients.append(input("Please enter the units: "))
    for i in range(1, powerx):
        coefficients.append(int(input("Enter the value for x^{}".format(i))))


while True:
    ans = input("do you want to integrate (1) or differentiate (2) ?: ")
    if ans == "1":
        integrate()
    elif ans == "2":
        differentiate()
    else:
        print("Please enter option 1 or option 2")
