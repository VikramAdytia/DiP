SPACE = ' '
STRAR = '*'

if __name__ == "__main__":
    rows = int(input("Сколько рядов у ёлки?"))
    spaces = rows - 1
    stars = 3
    print(
        (SPACE * spaces + SPACE) +
        STRAR +
        (SPACE * spaces)
    )

    for i in range(rows - 1):
        print(
            (SPACE * spaces) +
            (STRAR * stars) +
            (SPACE * spaces)
        )
        stars += 2
        spaces -= 1
