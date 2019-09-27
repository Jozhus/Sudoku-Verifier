def validSolution(board):
    vert = [[] for x in range(9)]
    boxes = [[] for x in range(9)]
    for i, x in enumerate(board):
        if sum(x) != 45 or not all(x.count(z) for z in x):
            return False
        for n, y in enumerate(x):
            boxes[(n // 3) + ((i // 3) * 3)].append(y)
            vert[n].append(y)
    for x in vert:
        if sum(x) != 45 or not all(x.count(z) for z in x):
            return False
    for x in boxes:
        if sum(x) != 45 or not all(x.count(z) for z in x):
            return False
    return True
