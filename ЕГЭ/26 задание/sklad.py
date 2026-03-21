with open('sklad.txt') as f:
    n = int(f.readline())
    f = [i.split() for i in f]
    gruzy = []
    for i in range(len(f)):
        time_start, time_end, typy = int(f[i][0]), int(f[i][0]) + int(f[i][1]), f[i][2]
        gruzy.append((time_start, time_end, typy))

    a_slots = []  # 100 мест
    b_slots = []  # 40 мест
    cnt_dop = 0  # уехали на доп склад
    cnt_gryz = 0  # малых расположиться на складе

    gruzy.sort()

    for time_start, time_end, typy in gruzy:
        a_slots = [i for i in a_slots if i > time_start]
        b_slots = [i for i in b_slots if i > time_start]

        if typy == 'A':
            if len(a_slots) < 100:
                a_slots.append(time_end)
                cnt_gryz += 1
            elif len(b_slots) < 40:
                b_slots.append(time_end)
            else:
                cnt_dop += 1

        elif typy == 'B':
            if len(b_slots) < 40:
                b_slots.append(time_end)
            else:
                cnt_dop += 1
    print(cnt_gryz, cnt_dop)
