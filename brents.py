def linear_quietlent(keys, m, m1):
    kayit = [None] * m
    for key in keys:
        h = key % m
        artis = key // m1  # Burası değişebilir
        if kayit[h] is None:
            kayit[h] = key
        else:
            while kayit[h] is not None:
                h = (h + artis) % m
            kayit[h] = key

    for i in range(m):
        print(f"{i}. {kayit[i]}\n")