# GUESS NUMBER GAME

To teach my friend python,

I try to make a simple game.

But the sol.py is really a funny crap.

sol.py:
```
$ python sol.py
1: guess 0123
2: guess 0245
3: guess 0367
4: guess 1843
5: guess 8293
ans is [8, 2, 9, 3]

$ python -i sol.py           │$ python guess.py
>>> nextGuess()              │0123
'0123'                       │1A0B <- 0123
>>> redAns('0123' , 1 , 0)   │0456
>>> nextGuess()              │1A0B <- 0456
'0456'                       │0789
>>> redAns('0456' , 1 , 0)   │0A2B <- 0789
>>> nextGuess()              │7158
'0789'                       │1A0B <- 7158
>>> redAns('0789' , 0 , 2)   │7493
>>> nextGuess()              │4A0B <- 7493
'7158'                       │
>>> redAns('7158' , 1 , 0)   │
>>> nextGuess()              │
'7493'                       │
>>>                          │
```

test.py:
```
5283 5293 8204 8214 8241
8431 9204 9214 9241 9431

^ probs that need guess 8 times

(1, 1)
(2, 15)
(3, 211)
(4, 1240)
(5, 2108)
(6, 1203)
(7, 252)
(8, 10)   < at least guess 8 times by using sol.py
(9, 0)
(10, 0)
```
