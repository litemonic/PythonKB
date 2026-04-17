def ListsInList(s):
    main = [[0] * s for _ in range(s)]
    x, y, dx, dy = 0, 0, 0, 1
    for i in range(1, s*s + 1):
        main[x][y] = i
        if x + dx >= s or x + dx < 0 or y + dy >= s or y + dy < 0 or main[x+dx][y+dy] != 0:
            dx, dy = dy, -dx
        x, y = x + dx, y + dy

    return main
print (ListsInList(5))