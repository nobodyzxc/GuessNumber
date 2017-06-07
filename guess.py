import sys
from random import randint

def issue(li):
    while len(li) != 4:
        n = randint(0 , 9)
        if n not in li: li.append(n)
    return ''.join([str(e) for e in li])

def legal(line):
    if not line.isdigit() \
        or len(line) != 4 \
        or len(line) != len(set(line)):
        print("illegal guess")
        return False
    return True

def judge(prob , line):
    a = sum([1 for x , y in zip(line , prob) if x == y])
    c = sum([1 for x in line if x in prob])
    return a , c - a

def play(line):
    if play.prob == []: play.prob = issue([]);
    return judge(play.prob , line)

play.prob = []

if __name__ == '__main__':
    for line in sys.stdin:
        guess = line.strip()
        if legal(guess): print("{}A{}B".format(*play(guess)))
