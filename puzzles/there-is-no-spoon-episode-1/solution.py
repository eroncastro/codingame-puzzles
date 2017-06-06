width = int(input())
height = int(input())
table = [list(input()) for i in range(height)]

for y, row in enumerate(table):
    for x, elem in enumerate(row):
        if elem == '.':
            continue
        print('%s %s' % (x, y), end=' ')

        neighbor_x = x + 1
        while neighbor_x < width:
            if row[neighbor_x] == '0':
                break
            neighbor_x += 1

        if neighbor_x >= width or row[neighbor_x] == '.':
            print('-1 -1', end=' ')
        else:
            print('%s %s' % (neighbor_x, y), end=' ')

        neighbor_y = y + 1
        while neighbor_y < height:
            if table[neighbor_y][x] == '0':
                break
            neighbor_y += 1

        if neighbor_y >= height or table[neighbor_y][x] == '.':
            print('-1 -1')
        else:
            print('%s %s' % (x, neighbor_y))
