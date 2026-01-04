def brents(keys,m1,m2):
    liste = [None] * m1
    for key in keys:
        h = key % m1
        artis = key // m2
        if liste[h] is None:
            liste[h] = key
        else:
            bos_indeks = [h]
            while liste[h] is not None:
                h = (h + artis) % m1
                bos_indeks.append(h)
            if len(bos_indeks) <= 2:
                liste[h] = key
            else:
                sayac_list = []
                for idx, i in enumerate(bos_indeks[:-1]):
                    artis = liste[i] // m1
                    son = i
                    sayac = idx + 1

                    while liste[son] is not None:
                        son = (son + artis) % m1
                        sayac += 1
                        if sayac > 100:
                            break
                    sayac_list.append({"sayac": sayac, "indeks": i, "bos": son})

                en_kucuk = min(sayac_list, key=lambda x: x["sayac"])
                liste[en_kucuk["bos"]] = liste[en_kucuk["indeks"]]
                liste[en_kucuk["indeks"]] = key
    for i in range(m1):
        print(f"{i}. {liste[i]}\n")

