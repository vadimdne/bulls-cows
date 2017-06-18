"""
Bulls and Cows game: https://en.wikipedia.org/wiki/Bulls_and_Cows
"""
from itertools import permutations


class Bullscows:
    def __init__(self, alphabet, secret_len):
        self.alphabet = alphabet
        self.secret_len = secret_len
        self.all_possible_options = [''.join(c) for c in permutations(self.alphabet, self.secret_len)]
        self.remaining_options = list(self.all_possible_options)
        self.guess = self.alphabet[:self.secret_len]

    @staticmethod
    def evaluate(guess, secret):
        """
        Evaluate guess and return (cows, bulls) tuple.
        Cows - count of characters in different position.
        Bulls - count of characters in same position.
            >>> Bullscows.evaluate('5678', '1234')
            (0, 0)
            >>> Bullscows.evaluate('8912', '1234')
            (2, 0)
            >>> Bullscows.evaluate('1289', '1234')
            (2, 2)
            >>> Bullscows.evaluate('1234', '1234')
            (4, 4)
        """
        cows = sum(g in secret for g in guess)
        bulls = sum(g == s for g, s in zip(guess, secret))
        return cows, bulls

    def adjust_guess(self, result):
        """
        Reduce remaining options, picking only ones which give same evaluate result if they're the secret.
        Update guess to first remaining option.
        """
        self.remaining_options = [option for option in self.remaining_options if self.evaluate(self.guess, option) == result]
        self.guess = self.remaining_options[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()



