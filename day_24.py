with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

hailstones = []
for lines in lines:
    position, velocities = lines.split(' @ ')
    hailstones.append(([int(val) for val in position.split(', ')], [int(val) for val in velocities.split(', ')]))

print(hailstones)

test_area_min = 200000000000000
test_area_max = 400000000000000

def is_in_test_area(x, y, area_min, area_max):
    return area_min <= x <= area_max and area_min <= y <= area_max

def get_intersection(a, b):
    px_a, py_a, pz_a = a[0]
    vx_a, vy_a, vz_a = a[1]

    px_b, py_b, pz_b = b[0]
    vx_b, vy_b, vz_b = b[1]

    num = vx_a * vx_b * (py_b - py_a) + (vx_b * px_a * vy_a) - (vx_a * px_b * vy_b)

    div = vx_b * vy_a - vx_a * vy_b
    if div == 0:
        #print("parallel")
        return False
    x = num / div
    t1 = (x - px_a) / vx_a
    t2 = (x - px_b) / vx_b
    y = py_a + vy_a * t1
    if t1 < 0 and t2 < 0:
        #print("in the past for both")
        return False
    if t1 < 0:
        #print("in the past for A")
        return False
    if t2 < 0:
        #print("in the past for B")
        return False
    #print(x, y)
    return is_in_test_area(x, y, test_area_min, test_area_max)

def part_1():

    intersections_count = 0
    for i in range(len(hailstones)):
        current_hailstone = hailstones[i]
        for j in range(i + 1, len(hailstones)):
            next_hailstone = hailstones[j]
            #print(current_hailstone, next_hailstone)
            if get_intersection(current_hailstone, next_hailstone):
                intersections_count += 1
    print(intersections_count)



part_1()