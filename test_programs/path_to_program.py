import sys

def sum_diff(a,b):
    return a+b, a-b

if __name__ == "__main__":

    for input in sys.stdin:
        list_input = input.split('\n')[0].split(',')
        a = int(list_input[0])
        b = int(list_input[1])
        sum, diff = sum_diff(a,b)
        print(f"{sum}, {diff}")
        break