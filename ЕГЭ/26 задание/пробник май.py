with open('пробник май.txt') as f:
    def crasivo(l):
        str_num = str(l)
        if all(d == '0' for d in str_num[1:]):
            return True
        for i in range(len(str_num) - 2):
            if str_num[i] == str_num[i + 1] == str_num[i + 2]:
                return True
        return False


    n = f.readline()
    score = [int(num) for num in f]
    cheat = []
    maxi = 0
    for scores in score:
        if crasivo(scores):
            cheat.append(scores)
            maxi = max(maxi, scores)
    print(len(cheat), maxi)
