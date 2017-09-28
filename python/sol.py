import sys
from guess import play , judge

ans = [];

def main(show):
    while len(ans) != 1: tryAns(nextGuess() , show)
    if show: print('ans is {}'.format(ans[0]))

def genAns(idx , cur):
    global ans
    if idx == 0: ans = [];
    for i in range(0 , 10):
        if i in cur: continue
        elif idx != 3: genAns(idx + 1 , cur + [i])
        else :ans.append(''.join([str(e) for e in cur + [i]]))

def redAns(guess , a , b):
    global ans
    ans = [e for e in ans if judge(guess , e) == (a , b)]

def tryAns(guess , show):
    tryAns.count += 1
    redAns(guess , *play(guess))
    if show: print("{}: guess {}".format(tryAns.count , guess))

nextGuess = lambda: ''.join([str(e) for e in ans[0]])

genAns(0 , [])

if not sys.flags.interactive and __name__ == '__main__':
    tryAns.count = 0
    main(show=True)
