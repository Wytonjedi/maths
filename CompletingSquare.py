# this is a program to complete the squared for x^2

while True:
    power2 = int(input("Please enter the X^2: "))
    power1 = int(input("Please enter the X: ")) / power2
    power0 = int(input("please enter the unit: ")) / power2
    ans1 = power2
    ans2 = power1 / 2
    ans3 = (power0 - ans2 ** 2) * power2
    print("{}x^2 + {}x + {} =  {}(x + {}) + {}".format(power2, power1, power0, ans1, ans2, ans3))
