from bullscows import Bullscows
import random
from itertools import count

settings = {
    'alphabet': '0123456789',
    'secret_len': 4

}

secret = ''.join(str(digit) for digit in random.sample(*settings.values()))
print "Generated secret is: {}".format(secret)
bc = Bullscows(**settings)

for n in count(1):
    print "Remaining options count: {}".format(len(bc.remaining_options))
    print "Guess: {}".format(bc.guess)
    result = Bullscows.evaluate(bc.guess, secret)
    print "Response: {} cows, {} bulls".format(*result)
    if bc.guess == secret:
        print "I guessed {}. Number of tries: {}".format(bc.guess, n)
        break
    bc.adjust_guess(result)
