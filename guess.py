import sys
from random import randint

def issue(li):
    while len(li) != 4:
        n = randint(0 , 9)
        if n not in li:
            li.append(n)
    return ''.join(list(map(str , li)))

def legal(line):
    if not line.isdigit() or len(line) != 4:
        print(line , "not digit or repeat digit")
        return False
    for n in line:
        if line.count(n) != 1:
            print("repeat n")
            return False
    return True

def judge(prob , line):
    a = 0 ; c = 0
    for i in range(4):
        if line[i] == prob[i]:
            a += 1
    for i in line:
        if i in prob:
            c += 1
    return a , c - a

def play(line):
    if play.prob == []:
        play.prob = issue([]);
    if legal(line):
        return judge(play.prob , line)
play.prob = []

if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        print("{}A{}B <- {}".format(*play(line) , line))
