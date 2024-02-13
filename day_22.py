from collections import defaultdict

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

bricks = []
for line in lines:
    start, end = line.split('~')
    bricks.append(([int(v) for v in start.split(',')], [int(v) for v in end.split(',')]))

bricks.sort(key=lambda v: v[0][2])

matrix = defaultdict(lambda: defaultdict(list))
# support[a] get all bricks that support a
support = defaultdict(set)
# supported[a] get all bricks that are supported by a
supported = defaultdict(set)
for brick_idx, brick in enumerate(bricks):
    start, end = brick

    x_start, y_start, z_start = start
    x_end, y_end, z_end = end

    dimensions_length = [x_end - x_start, y_end - y_start, z_end - z_start]
    heights_under_brick = []
    supported[brick_idx] = set()
    if y_end != y_start:
        for y in range(y_start, y_end + 1):
            if len(matrix[x_start][y]) > 0:
                height = matrix[x_start][y][-1]['height']
                heights_under_brick.append(height)
            else:
                heights_under_brick.append(0)

        for y in range(y_start, y_end + 1):
            max_height = max(heights_under_brick)
            if len(matrix[x_start][y]) > 0:
                if matrix[x_start][y][-1]['height'] == max_height:
                    support[brick_idx].add(matrix[x_start][y][-1]['brick_idx'])
                    supported[matrix[x_start][y][-1]['brick_idx']].add(brick_idx)
            matrix[x_start][y].append({'height': max_height + 1, 'brick_idx': brick_idx})
    elif x_end != x_start:
        for x in range(x_start, x_end + 1):
            if len(matrix[x][y_start]) > 0:
                height = matrix[x][y_start][-1]['height']
                heights_under_brick.append(height)
            else:
                heights_under_brick.append(0)

        for x in range(x_start, x_end + 1):
            max_height = max(heights_under_brick)
            if len(matrix[x][y_start]) > 0:
                if matrix[x][y_start][-1]['height'] == max_height:
                    support[brick_idx].add(matrix[x][y_start][-1]['brick_idx'])
                    supported[matrix[x][y_start][-1]['brick_idx']].add(brick_idx)
            matrix[x][y_start].append({'height': max_height + 1, 'brick_idx': brick_idx})
    else:
        if len(matrix[x_start][y_start]) > 0:
            height = matrix[x_start][y_start][-1]['height']
            support[brick_idx].add(matrix[x_start][y_start][-1]['brick_idx'])
            supported[matrix[x_start][y_start][-1]['brick_idx']].add(brick_idx)
            for z in range(z_start, z_end + 1):
                matrix[x_start][y_start].append({'height': height + z - z_start + 1, 'brick_idx': brick_idx})
        else:
            for z in range(z_start, z_end + 1):
                matrix[x_start][y_start].append({'height': 0 + z - z_start + 1, 'brick_idx': brick_idx})


def part_1():
    safe_to_disintegrate_count = 0
    for support_brick, supported_brick_set in supported.items():
        if all([len(support[supported_brick]) > 1 for supported_brick in supported_brick_set]):
            safe_to_disintegrate_count += 1
    print(safe_to_disintegrate_count)
#part_1()


def get_falling_bricks(support_brick):
    global falling_bricks_count
    falling_bricks_per_brick = {}
    queue = [support_brick]
    fallen_bricks = {support_brick}

    while queue:
        brick = queue.pop(0)

        for supported_brick in supported[brick]:
            if supported_brick in fallen_bricks:
                continue

            queue.append(supported_brick)

            if support[supported_brick].issubset(fallen_bricks):
                falling_bricks_count += 1
                fallen_bricks.add(supported_brick)

falling_bricks_count = 0
print(supported)
def part_2():
    for idx, support_brick in enumerate(supported):
        print(idx, 'for brick :', support_brick)
        get_falling_bricks(support_brick)
    print(falling_bricks_count)
part_2()
