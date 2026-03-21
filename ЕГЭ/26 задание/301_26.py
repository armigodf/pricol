with open('301_26.txt') as f:
    n = int(f.readline())
    korob = sorted([int(s) for s in f], reverse=True)
    matr = [korob[0]]
    for i in range(1, n):
        if matr[-1] >= korob[i] + 3:
            matr.append(korob[i])
    print(len(matr), matr[-1])
