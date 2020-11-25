'''
============ЗАДАНИЕ:
            Римские цифры представлены в виде I, V, X, L, C, D и M
            Необходимо с помощью кода python преобразовать римское число в АРАБСКОЕ (стандартное) число.

            I - 1
            V - 5
            X - 10
            L - 50
            C - 100
            D - 500
            M - 1000

            Пример 1:
            Input: s = "III"
            Output: 3

            Пример 2:
            Input: s = "IV"
            Output: 4

            Пример 3:
            Input: s = "IX"
            Output: 9

            Пример 4:
            Input: s = "LVIII"
            Output: 58
            Explanation: L = 50, V= 5, III = 3.

            Пример 5:
            Input: s = "MCMXCIV"
            Output: 1994
            Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


============Условия:
            1. Длина 1 <= s.length <= 15
            2. s состоит только из ('I', 'V', 'X', 'L', 'C', 'D', 'M')
            3. Гарантируется, что конвертируемая в число s будет в диапозоне [1, 3999]

            4. Необходимо написать решение если дан следующий python код
            class Solution:
                 def romanToInt(self, s: str) -> int:

            5. Не используй сторонние библиотеки (код должен быть написан на pure python)

            7. Решение вышли в виде ссылки на репозиторий GitHub, имя файла - любое, но с расширением .py

            8. Ссылку можно прислать ответом на это письмо или по почте school.napoleonit.ru до 25.11.2020 включительно.


========================================================================================================================
            Идея и важные моменты:

            1. Римская система - непозиционная СЧ.
            2. Правило записи:
                    1) каждый меньший знак, поставленный слева от большего, вычитается из него;
                    2) каждый меньший знак, поставленный справа от большего, прибавляется к нему.
            3. Следствия из пункта 2:
                    1) Нужно разбивать строку по 2 символа и сравнить их.После из большего вычитаем меньшее и сохраняем.
                       После выполнения для всех пар символов сложить все числа и вывести ответ.

                    ВАЖНО!!!!
                    2) Крайний случай если у нас будет нечётное число римский цифр. Тогда последнее число мы
                       должны просто перевести в арабское число.
                    3) Крайний случай, когда мы имеем одинаковые числа стоящие рядом, например: "III".

'''


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
