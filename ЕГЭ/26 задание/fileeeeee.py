with open('fileeeeee.txt') as f:
    v, n = map(int, f.readline().split())
    papka = []
    s = [int(num) for num in f]
    s.sort()
    for i in range(len(s)):
        if sum(papka) < v:
            papka.append(s[i])
    print(len(papka), max(papka))

