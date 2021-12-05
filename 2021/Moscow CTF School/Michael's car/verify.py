from random import randrange
from math import gcd
from Crypto.Util.number import isPrime

import sys


def is_prime(n):
    if n <= 2 or n % 2 == 0:
        return False

    for a in [randrange(3, n, 2) for i in range(1337)]:
        if gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True


def verify(n):
    if n.bit_length() < 64:
        return False
    for i in range(5):
        if not is_prime(n):
            return False
    if isPrime(n):
        return False
    return True


N = 443656337893445593609056001

if __name__ == "__main__":
    print(
        "Hey! Please provide your serial number so we can verify that this is your Car, Michael."
    )
    n = int(input("Your number:"))
    if verify(n):
        with open("flag.txt", "r") as f:
            flag = f.read()
            print("Good evening, Michael, that's your Car!")
            print(flag)
    else:
        print("Hmm!, your serial number seems wrong. Isn't it too prime?")
