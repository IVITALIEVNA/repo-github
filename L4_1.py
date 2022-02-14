from sys import argv
def result():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"result - {time * rate + bonus}")

    except ValueError:
       print("Enter all 3 numbers")
result()
