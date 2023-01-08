import math


def get_digit(n: int, i: int) -> int:
    return int(n / (10 ** i)) % 10

def is_palindrome(n: int) -> bool:
    length = int(math.log10(n)) + 1
    
    for i in range(int(length / 2)):
        if get_digit(n, i) != get_digit(n, length - 1 - i):
            return False

    return True


if __name__ == '__main__':
    print(is_palindrome(int(input())))