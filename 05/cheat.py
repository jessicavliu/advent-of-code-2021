lines = [i.replace("\n", "").split(" -> ") for i in open("input.txt", "r")]

conv = [[list(map(int, i[0].split(","))), list(map(int, i[1].split(",")))] for i in lines]

valids = []
wodiag = []

for i in conv:
    valids.append(i)
    if i[0][0] == i[1][0] or i[0][1] == i[1][1]:
        wodiag.append(i)

allpoints = [[], []]

for c in range(2):
    for i in (valids if c == 1 else wodiag):
        lh_x = [i[0][0], i[1][0]]
        lh_y = [i[0][1], i[1][1]]

        step_x = -1 if i[0][0] > i[1][0] else 1
        step_y = -1 if i[0][1] > i[1][1] else 1

        for x, y in zip(range(i[0][0], i[1][0] + step_x, step_x) if min(lh_x) != max(lh_x) else [min(lh_x)] * (max(lh_y) - min(lh_y) + 1), range(i[0][1], i[1][1] + step_y, step_y) if min(lh_y) != max(lh_y) else [min(lh_y)] * (max(lh_x) - min(lh_x) + 1)):
            allpoints[c].append([x, y])

h_x = int(max([i[j][0] for i in valids for j in range(2)])) + 1
h_y = int(max([i[j][1] for i in valids for j in range(2)])) + 1

current = [[[0 for i in range(h_x)] for j in range(h_y)] for a in range(2)]

for c in range(len(allpoints)):
    for i in range(len(allpoints[c])):
        current[c][allpoints[c][i][1]][allpoints[c][i][0]] += 1

print("at least 2 overlap without diags:", sum([j >= 2 for i in current[0] for j in i]))
print("at least 2 overlap with diags:", sum([j >= 2 for i in current[1] for j in i]))