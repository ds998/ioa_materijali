import random
import math

random.seed()

r0 = 15

S = [2.424595205726587e-01, 1.737226395065819e-01, 1.315612759386036e-01,
     1.022985539042393e-01, 7.905975891960761e-02, 5.717509542148174e-02,
     3.155886625106896e-02, -6.242228581847679e-03, -6.565183775481365e-02,
     -8.482380513926287e-02, -1.828677714588237e-02, 3.632382803076845e-02,
     7.654845872485493e-02, 1.152250132891757e-01, 1.631742367154961e-01,
     2.358469152696193e-01, 3.650430801728451e-01, 5.816044173713664e-01,
     5.827732223753571e-01, 3.686942505423780e-01]

dots = [(r0 * math.cos((2 * math.pi * i) / 20), r0 * math.sin((2 * math.pi * i) / 20)) for i in range(20)]


def opt_f(x):
    global r0, dots, S
    one_check = math.sqrt(math.pow(x[0], 2) + math.pow(x[1], 2))
    two_check = math.sqrt(math.pow(x[2], 2) + math.pow(x[3], 2))

    if one_check >= r0 or two_check >= r0:
        return 100

    total = 0.0
    for i in range(len(dots)):
        one_distance = math.sqrt(math.pow(dots[i][0] - x[0], 2) + math.pow(dots[i][1] - x[1], 2))
        two_distance = math.sqrt(math.pow(dots[i][0] - x[2], 2) + math.pow(dots[i][1] - x[3], 2))
        total += math.pow((x[4] / one_distance) + (x[5] / two_distance) - S[i], 2)

    return total


generation = []
for i in range(60):
    arr = []
    for j in range(6):
        arr.append(random.random() * 30 - 15)

    generation.append(arr)

minimum = 100
min_sol = []
for m in range(10000):
    for i in range(len(generation)):
        if opt_f(generation[i]) <= 1e-14:
            print("Resenje je:")
            print(generation[i])
            print("Vrednost je:")
            print(opt_f(generation[i]))
            exit(0)
        if opt_f(generation[i]) < minimum:
            minimum = opt_f(generation[i])
            min_sol = generation[i]

    next_generation = []
    for i in range(len(generation)):
        xa = []
        xb = []
        xc = []
        z = []
        y = []
        a = random.randint(0, 59)
        while a == i:
            a = random.randint(0, 59)
        b = random.randint(0, 59)
        while b == i or b == a:
            b = random.randint(0, 59)
        c = random.randint(0, 59)
        while c == i or c == b or c == a:
            c = random.randint(0, 59)

        xa = generation[a]
        xb = generation[b]
        xc = generation[c]

        for j in range(6):
            z.append((xa[j] + 0.8 * (xb[j] - xc[j])))

        R = random.randint(0, 5)

        for j in range(6):
            ri = random.random()
            if ri < 0.9 or j == R:
                y.append(z[j])
            else:
                y.append(generation[i][j])

        next_generation.append(y)

    for i in range(len(generation)):
        if opt_f(next_generation[i]) < opt_f(generation[i]):
            generation[i] = next_generation[i]

print("Najmanje nadjeno resenje je:")
print min_sol
print("Njegova vrednost je:")
print minimum
