import sys
from guess import play , judge
from sol import main , genAns , ans , tst , tryAns

probS = ans.copy()
probS = list(map(lambda l:''.join(list(map(str , l))) , probS))
bkt = [0 for i in range(0 , 11)]

for prob in probS:
    tryAns.count = 0
#   ans = [] # weired
    genAns(0)
    play.prob = prob
    main(False)
    bkt[tryAns.count] += 1
    if tryAns.count > 7:
        print(prob)

for i in range(1 , 11):
    print((i , bkt[i]))
