# https://github.com/karan/Projects
# Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def get_colletz_cojecture(number):
    n = number
    steps = 0
    flag = True
    while flag:
        if n == 1:
            flag = False
        if n % 2 == 0:
            n /= 2
            steps += 1
        else:
            n = n*3+1
    return steps


def main():
    steps = get_colletz_cojecture()
    print(steps)


if __name__ == "__main__":
    main()
