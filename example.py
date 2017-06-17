from bullscows import Bullscows
import random
from itertools import count

settings = {
    'alphabet': '0123456789',
    'secret_len': 4

}

secret = ''.join(str(digit) for digit in random.sample(*settings.values()))
print "Generated secret is: {}".format(secret)

cb = Bullscows(**settings)

for n in count(1):
    print "Remaining options count: {}".format(len(cb.remaining_options))
    print "Guess: {}".format(cb.guess)
    result = Bullscows.evaluate(cb.guess, secret)

    print "Response: {} cows, {} bulls".format(*result)
    if cb.guess == secret:
        print "I guessed {}. Number of tries: {}".format(cb.guess, n)
        break

    cb.adjust_guess(result)