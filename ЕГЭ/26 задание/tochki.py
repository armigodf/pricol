with open('tochki.txt') as f:
    n = int(f.readline())
    points = []

    for s in f:
        ryad, mesto = map(int, s.split())
        points.append((ryad, mesto))

    light_counts = {}
    for ryad, mesto in points:
        if mesto % 2 == 0:
            if ryad in light_counts:
                light_counts[ryad] += 1
            else:
                light_counts[ryad] = 1

    max_count = 0
    best_ryad = None
    for ryad, count in light_counts.items():
        if count > max_count:
            max_count = count
            best_ryad = ryad

print(max_count, best_ryad)
