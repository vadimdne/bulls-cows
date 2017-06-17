Bulls and Cows game
-------------------------------

Implements [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) game via simple sieve algorithm.

### Usage

Usage example:

```python
from bullscows import Bullscows
from itertools import count

settings = {
    'alphabet': '0123456789',
    'secret_len': 4

}

secret = '6734'
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
```

Run example:

```
Generated secret is: 6374
Remaining options count: 5040
Guess: 0123
Response: 1 cows, 0 bulls
Remaining options count: 1440
Guess: 1456
Response: 2 cows, 0 bulls
Remaining options count: 369
Guess: 2547
Response: 2 cows, 0 bulls
Remaining options count: 80
Guess: 3674
Response: 4 cows, 2 bulls
Remaining options count: 3
Guess: 3764
Response: 4 cows, 1 bulls
Remaining options count: 2
Guess: 6374
Response: 4 cows, 4 bulls
I guessed 6374. Number of tries: 6
```