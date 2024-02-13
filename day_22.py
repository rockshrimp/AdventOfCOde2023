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
        print(z_start, z_end)
        if len(matrix[x_start][y_start]) > 0:
            height = matrix[x_start][y_start][-1]['height']
            support[brick_idx].add(matrix[x_start][y_start][-1]['brick_idx'])
            supported[matrix[x_start][y_start][-1]['brick_idx']].add(brick_idx)
            for z in range(z_start, z_end + 1):
                matrix[x_start][y_start].append({'height': height + z - z_start + 1, 'brick_idx': brick_idx})
        else:
            for z in range(z_start, z_end + 1):
                matrix[x_start][y_start].append({'height': 0 + z - z_start + 1, 'brick_idx': brick_idx})

print('supported', supported)
print('support',support)


def part_1():
    safe_to_disintegrate_count = 0
    for support_brick, supported_brick_set in supported.items():
        if all([len(support[supported_brick]) > 1 for supported_brick in supported_brick_set]):
            safe_to_disintegrate_count += 1
            #print(support_brick, 'is safe to disintegrate')
    print(safe_to_disintegrate_count)
part_1()
