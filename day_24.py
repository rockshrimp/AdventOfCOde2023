from sympy import solve, symbols, Eq

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

def line(x, y, v_x, v_y):
    m = v_y / v_x
    q = -m * x + y
    return m, q

def get_intersection(a, b):
    xa_0, ya_0, za_0 = a[0]
    vx_a, vy_a, vz_a = a[1]

    xb_0, y_b0, zb_0 = b[0]
    vx_b, vy_b, vz_b = b[1]


    div = vx_b * vy_a - vx_a * vy_b
    if div == 0:
        #print("parallel")
        return False

    m1, q1 = line(xa_0, ya_0, vx_a, vy_a)
    m2, q2 = line(xb_0, y_b0, vx_b, vy_b)

    # Intersection coordinates
    x = (q2 - q1) / (m1 - m2)
    y = m1 * x + q1

    t1 = (x - xa_0) / vx_a
    t2 = (x - xb_0) / vx_b
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
            if get_intersection(current_hailstone, next_hailstone):
                intersections_count += 1
    print(intersections_count)
part_1()

def part_2():
    x0, y0, z0, vx, vy, vz = symbols('x0 y0 z0 vx vy vz')

    equations = []
    for i in range(5):
        hailstone = hailstones[i]
        x0_a, y0_a, z0_a = hailstone[0]
        vx_a, vy_a, vz_a = hailstone[1]

        eq1 = Eq((x0_a - x0) * (vy - vy_a) / (vx - vx_a), (y0_a - y0))
        eq2 = Eq((x0_a - x0) * (vz - vz_a) / (vx - vx_a), (z0_a - z0))
        equations.extend([eq1, eq2])
    solution = solve(equations, (x0, y0, z0, vx, vy, vz), dict=True)[0]

    print(sum([solution[x0], solution[y0], solution[z0]]))

part_2()