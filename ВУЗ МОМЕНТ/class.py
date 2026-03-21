class Fraction:
    def __init__(self, ch, zn):
        self.chisl = ch
        self.znam = zn

    def __str__(self):
        return f"{self.chisl}/{self.znam}"

    def __mul__(self, other):
        return Fraction(self.chisl * other.chisl, self.znam * other.znam)

    def __sub__(self, other):
        new_ch = self.chisl * other.znam - other.chisl * other.znam
        new_zn = self.znam * other.znam
        return Fraction(new_ch, new_zn)

    def __add__(self, other):
        new_ch = self.chisl * other.znam + other.chisl * self.znam
        new_zn = self.znam * other.znam
        return Fraction(new_ch, new_zn)

    def __div__(self):
