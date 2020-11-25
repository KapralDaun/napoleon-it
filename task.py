
class Solution:
    add = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    div = {
        ('I', 'V'): 3,
        ('I', 'X'): 8,
        ('X', 'L'): 30,
        ('X', 'C'): 80,
        ('C', 'D'): 300,
        ('C', 'M'): 800,
    }

    def roman_to_arabic(self, roman_number):
        result = 0
        prev_char = None
        for char in roman_number:
            if prev_char and self.add[prev_char] < self.add[char]:
                result += self.div[(prev_char, char)]
            else:
                result += self.add[char]
            prev_char = char
        return result


class UnitTests(Solution):
    def all_tests(self):
        if self.roman_to_arabic('I') != 1:
            print('I is not 1')

        if self.roman_to_arabic('III') != 3:
            print('III is not 3')

        if self.roman_to_arabic('IV') != 4:
            print('IV is not 4')

        if self.roman_to_arabic('IX') != 9:
            print('IX is not 9')

        if self.roman_to_arabic('XXX') != 30:
            print('XXX is not 30')

        if self.roman_to_arabic('LVIII') != 58:
            print('LVIII is not 58')

        if self.roman_to_arabic('CCXXVIII') != 228:
            print('CCXXVIII is not 228')

        if self.roman_to_arabic('DLXXXV') != 585:
            print('DLXXXV is not 585')

        if self.roman_to_arabic('DCCCLXIV') != 864:
            print('DCCCLXIV is not 864')

        if self.roman_to_arabic('MD') != 1500:
            print('MD is not 1500')

        if self.roman_to_arabic('MCMXCIV') != 1994:
            print('MCMXCIV is not 1994')

        if self.roman_to_arabic('MM') != 2000:
            print('MM is not 2000')

        if self.roman_to_arabic('MMDCXLVIII') != 2648:
            print('MMDCXLVIII is not 2648')


def main():
    y = UnitTests()
    y.all_tests()
    Solution.roman_to_arabic(1,'MMDCXLVIII')
    pass


if __name__ == "__main__":
    main()
