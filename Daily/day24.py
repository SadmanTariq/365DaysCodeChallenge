def gcd(_a, _b):
    a, b = sorted([_a, _b])
    if r := a % b:
        return gcd(b, r)
    else:
        return b


def lcm(a, b):
    return abs(a * b) / gcd(a, b)


class Fraction:
    numerator = 0
    denominator = 0

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        

    def add(frac1, frac2):
        denom = lcm(frac1.denominator, frac2.denominator)
        num = frac1.numerator * (frac1.denominator / denom) + frac1.numerator * (frac1.denominator / denom)

        return Fraction(num, denom)

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)