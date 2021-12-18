path_map = {}

with open('input.txt') as file:
	for line in file:
		nodes = line.strip().split('-')
		if(not nodes[0] in path_map.keys()):
			path_map[nodes[0]] = []
		if(not nodes[1] in path_map.keys()):
			path_map[nodes[1]] = []

		path_map[nodes[0]].append(nodes[1])
		path_map[nodes[1]].append(nodes[0])

visit_map = {}
for k in path_map.keys():
	visit_map[k] = 1

all_small_caves = []
for k in path_map.keys():
	if(not k.upper() == k and not k == 'start' and not k == 'end'):
		all_small_caves.append(k)

print(path_map)
print(visit_map)
print(all_small_caves)


def solve(node, string):
	for small_cave in all_small_caves:
		visit_map[small_cave] = 2
		dfs('start', string)
		visit_map[small_cave] = 1

paths = set()
def dfs(node, string):
	if(node == 'end'):
		global num_paths
		string += 'end'
		paths.add(string)
		string = ''

	string += node + '-'
	# if it's not a big cave, we can mark as visited
	if(not node.upper() == node):
		visit_map[node] -= 1

	for neighbor in path_map[node]:
		if(not visit_map[neighbor] == 0):
			dfs(neighbor, string)

	#backtrack
	visit_map[node] += 1
	return

solve('start', '')
print(len(paths))