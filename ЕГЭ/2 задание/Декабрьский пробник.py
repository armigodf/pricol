for p in range(2):
    for q in range(2):
        for r in range(2):
            if ((p and q) or ((not(p)) and r) or (p <= q)) == 0:
                print(q, p, r)