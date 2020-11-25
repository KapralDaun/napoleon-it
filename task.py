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

    def romanToInt(self, s: str) -> int:
        result = 0
        prev_char = None
        for char in s:
            if prev_char and self.add[prev_char] < self.add[char]:
                result += self.div[(prev_char, char)]
            else:
                result += self.add[char]
            prev_char = char
        return result


def main():
    pass


if __name__ == "__main__":
    main()
