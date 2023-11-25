def main():
    sas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = 3
    fes1 = 0
    fes2 = 1
    fes = fes1 + fes2
    while fes < len(sas):
        fes2 = fes1
        fes1 = fes
        fes = fes1 + fes2
    index = -1
    while fes > 1:
        i = min(index + fes2, (len(sas) - 1))
        if sas[i] < d:
            fes = fes1
            fes1 = fes2
            fes2 = fes - fes1
            index = i
        elif sas[i] > d:
            fes = fes2
            fes1 = fes1 - fes2
            fes2 = fes - fes1
        else:
            continue
    if (fes1 and index < (len(sas) - 1)) and (sas[index + 1] == d):
        print(index + 1)


if __name__ == "__main__":
    main()
