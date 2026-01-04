def progressive_overflow(keys,m):
    kayit = [None] * m
    for key in keys:
        h = key % m
        if kayit[h] is None:
            kayit[h] = key
        else:
            for i in range(h + 1, m+1, 1):
                if i == m:
                    for a in range(0, h, 1):
                        if kayit[a] is None:
                            kayit[a] = key
                            break
                    break
                if kayit[i] is None:
                    kayit[i] = key
                    break

    for i in range(m):
        print(f"{i}. {kayit[i]}\n")

