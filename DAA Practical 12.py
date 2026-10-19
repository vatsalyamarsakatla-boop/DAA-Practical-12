from itertools import permutations

n = 4
INF = 99999

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = list(range(1, n))
min_cost = INF
best_path = []

for path in permutations(cities):
    total = cost[0][path[0]]

    for i in range(len(path) - 1):
        total += cost[path[i]][path[i + 1]]

    total += cost[path[-1]][0]

    if total < min_cost:
        min_cost = total
        best_path = [0] + list(path) + [0]

print("Minimum Cost:", min_cost)
print("Best Tour:", " -> ".join(str(city + 1) for city in best_path))
print("EN.No: 92460118673")