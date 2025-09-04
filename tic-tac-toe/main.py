l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(9):
    if i % 2 == 0:
        enter = int(input("Player 1: "))
        l[enter - 1] = "X"
    else:
        enter = int(input("Player 2: "))
        l[enter - 1] = "O"

    print(l[0], "|", l[1], "|", l[2])
    print("-----------")
    print(l[3], "|", l[4], "|", l[5])
    print("-----------")
    print(l[6], "|", l[7], "|", l[8])

    if l[0] == l[1] == l[2] or l[3] == l[4] == l[5] or l[6] == l[7] == l[8] or \
       l[0] == l[3] == l[6] or l[1] == l[4] == l[7] or l[2] == l[5] == l[8] or \
       l[0] == l[4] == l[8] or l[2] == l[4] == l[6]:
        print("Player", 1 if i % 2 == 0 else 2, "wins!")
        break
else:
    print("It's a draw!")
