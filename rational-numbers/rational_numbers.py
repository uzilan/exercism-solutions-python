from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise Exception("Denominator is zero")

        gcd = self.gcd(numer, denom)
        self.numer = numer / gcd
        self.denom = denom / gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = other.numer * self.denom
        return Rational(numer, denom)

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)

    def __pow__(self, power):
        abs_power = abs(power)
        numer = self.numer ** abs_power
        denom = self.denom ** abs_power
        return Rational(numer, denom)

    def __rpow__(self, base):
        return (abs(base) ** self.numer) ** (1 / self.denom)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
