import sys
from guess import play , judge

ans = [];tst = []

def genAns(idx):
    global tst , ans
    for i in range(0 , 10):
        if i in tst:continue
        else:
            if idx == 3:
                ans.append(tst + [i])
            else:
                tst.append(i)
                genAns(idx + 1)
                tst.pop()

intList = lambda l:list(map(int , list(l)))
lfilter = lambda f , l:list(filter(f , l))
nans = lambda l , a , b: lfilter(lambda p:judge(intList(l) , p) == (a , b) , ans)

def redAns(line , a , b): global ans; ans = nans(line , a , b)

def tryAns(line):
    global ans
    tryAns.count += 1
    print("{}: guess {}".format(tryAns.count , line))
    redAns(line , *play(line))

tryAns.count = 0

nextGuess = lambda: ''.join(list(map(str , ans[0])))

genAns(0)
if not sys.flags.interactive:
    while len(ans) != 1:
        tryAns(nextGuess())
    print('ans is {}'.format(ans[0]))
