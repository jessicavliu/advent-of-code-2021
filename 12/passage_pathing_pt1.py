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
	visit_map[k] = False

print(path_map)
print(visit_map)

num_paths = 0


def dfs(node):
	if(node == 'end'):
		global num_paths
		num_paths += 1

	# if it's not a big cave, we can mark as visited
	if(not node.upper() == node):
		visit_map[node] = True

	for neighbor in path_map[node]:
		if(not visit_map[neighbor]):
			dfs(neighbor)

	#backtrack
	visit_map[node] = False
	return

dfs('start')
print(num_paths)