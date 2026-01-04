def eisch(keys,m):
    kayit = [None] * m
    baglanti = [None] * m
    for key in keys:
        h = key % m
        if kayit[h] is None:
            kayit[h] = key
        else:
            for i in range(m-1, -1, -1):
                if kayit[i] is None:
                    kayit[i] = key
                    if baglanti[h] is None:
                        baglanti[h] = i
                    else:
                        index = baglanti[h]
                        baglanti[h] = i
                        baglanti[i] = index
                    break

    for i in range(m):
        print(f"{i}. {kayit[i]} -> {baglanti[i]}\n")
