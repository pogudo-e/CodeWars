def points(games: list) -> int:
    res = []
    for i in games:
        x = i.strip(':')
        if int(x[0]) > int(x[-1]):
            res.append(3)
        elif int(x[0]) == int(x[-1]):
            res.append(1)
    return sum(res)


print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))
print(points(['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4']))
