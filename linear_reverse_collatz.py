def linearlyReversedCollatz(n, fullPaths=True, sequential=True):
    
    def nextSequentialRoot(lastRoot, _):
        return lastRoot + 6
    
    def nextChaoticRoot(_, n):
        return (n // 4) +5
    
    def belongsToOddLessThan(lastRoot, n):
        x = n
        while x % 2 == 0:
            x //= 2
        return x < lastRoot 
    
    lastRoot = -3
    visitedOne = False
    if sequential:
        nextRoot = nextSequentialRoot
    else:
        nextRoot = nextChaoticRoot
    while True:
        yield n
        if n % 2 == 0:
            condition = n % 8 == 0
            if fullPaths:
                condition = condition and belongsToOddLessThan(lastRoot, n)
            if condition:
                n = nextRoot(lastRoot, n)
                lastRoot = n
            else:
                n //= 2
        else:
            if n != 1:
                n = n * 3 + 1
            else:
                if not visitedOne:
                    visitedOne = True
                    n = n * 3 + 1
                else:
                    n = nextRoot(lastRoot)
                    lastRoot = n

def main():
    n = linearlyReversedCollatz(1)
    highest = 0
    while True:
        #input()
        x = next(n)
        #if x % 2 == 1 and x % 3 == 0:
        #    print(x, 'root')
        #else:
        #    print(x)
        if x % 2 == 1 and x % 3 == 0:
            if x > highest:
                highest = x
                print(highest, 'root')
        
if __name__ == '__main__':
    main()
