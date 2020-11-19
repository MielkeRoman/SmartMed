def rrtt(x, m, n):
    d = {m: 'gf', n: 'dr', x: 'drgf'}
    y = 2
    if y == 2:
        y = x
        print(y)
        print(d[y])
        print(m*n)


def main():
    m = 2
    n = 3
    x = m**n
    rrtt(x, m, n)


if __name__ == "__main__":
    main()