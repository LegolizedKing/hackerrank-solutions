if __name__ == '__main__':
    a=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        a.append([name,score])
 
    scores=set([a[x][1] for x in range(n)])
    scores=list(scores)
    scores.sort()

    names=[x[0] for x in a if x[1]==scores[1]]
    names.sort()

    for i in names:
        print(i)
