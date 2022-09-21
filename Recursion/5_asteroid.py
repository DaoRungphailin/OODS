def asteroid_collision(index, asts):
    # print(asts)
    if index + 1 == len(asts):  # Last
        return asts
    elif index < len(asts):
        ast1, ast2 = asts[index], asts[index+1]
        if ast1 > 0 and ast2 < 0:  # Crash !
            if ast1 > abs(ast2):
                asts.pop(index+1)
            elif ast1 < abs(ast2):
                asts.pop(index)
            else:  # same size
                asts.pop(index+1)
                asts.pop(index)
            return asteroid_collision(index-1, asts)
        else:
            return asteroid_collision(index+1, asts)


x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(0, x))
