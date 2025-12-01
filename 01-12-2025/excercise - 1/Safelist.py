def safelist(x):
    try:
        x[10] = "John"
    except IndexError:
        print("Wrong index john!")

x = [1, 2, 3, 4, 5, 6, 7, 8]
safelist(x)