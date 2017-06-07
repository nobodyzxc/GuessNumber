import sys
from guess import play , judge

ans = []; tst = []

def main(show):
    while len(ans) != 1:
        tryAns(nextGuess() , show)
    if show: print('ans is {}'.format(ans[0]))

def genAns(idx):
    global tst , ans
    if idx == 0:
        ans = []; tst = []
    for i in range(0 , 10):
        if i in tst:
            continue
        elif idx == 3:
            ans.append(''.join([str(e) for e in tst + [i]]))
        else:
            tst.append(i)
            genAns(idx + 1)
            tst.pop()

def redAns(guess , a , b):
    global ans;
    ans = [ e for e in ans if judge(guess , e) == (a , b) ]

def tryAns(guess , show):
    global ans
    tryAns.count += 1
    if show:
        print("{}: guess {}".format(tryAns.count , guess))
    redAns(guess , *play(guess))

nextGuess = lambda: ''.join([str(e) for e in ans[0]])

genAns(0)

if not sys.flags.interactive \
        and __name__ == '__main__':
    tryAns.count = 0
    main(show=True)
