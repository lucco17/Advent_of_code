import copy

def find_next_workflow(part, full_workflow):
	for instr in full_workflow:
		if not isinstance(instr, list):
			return instr
		if instr[1] == '<':
			if part[instr[0]] < instr[2]:
				return instr[3]
		else:
			if part[instr[0]] > instr[2]:
				return instr[3]

workflows = {}
parts = []

with open('19_workflows.txt', 'r') as f:
	reading_workflows = True
	for line in f.readlines():
		line = line.replace('\n', '')
		if line == '':
			reading_workflows = False
		elif reading_workflows:
			workflow_name, workflow_instr = line.split('{')
			workflow_instr = workflow_instr.replace('}', '')
			workflow_full_instr = []
			for instr in workflow_instr.split(','):
				if ':' in instr:
					instr = instr.split(':')
					full_instr = [instr[0][0], instr[0][1], int(instr[0][2:]), instr[1]]
					workflow_full_instr.append(full_instr)
				else:
					workflow_full_instr.append(instr)
			workflows[workflow_name] = workflow_full_instr
		else:
			part = {}
			part_nums = line.replace('{', '').replace('}', '')
			part_nums = part_nums.split(',')
			for part_num in part_nums:
				categorie, num = part_num.split('=')
				part[categorie] = int(num)
			parts.append(part)


#s = 0
#for i, part in enumerate(parts):
#	RorA = False
#	curr_workflow = 'in'
#	while not RorA:
#		curr_workflow = find_next_workflow(part, workflows[curr_workflow])
#		if curr_workflow == 'A':
#			for num in part.values():
#				s += num
#			RorA = True
#		elif curr_workflow == 'R':
#			RorA = True
#print(s)

s = 0

partitions = [['in', {'x':[1, 4001], 'm':[1, 4001], 'a':[1, 4001], 's':[1, 4001]}]]

while len(partitions) > 0:
	workflow_name, curr_part = partitions.pop(0)
	if workflow_name == 'A':
		m = 1
		for v in curr_part.values():
			m *= v[1] - v[0]
		s += m
	elif workflow_name != 'R':
		workflow = workflows[workflow_name]
		for instr in workflow:
			if not isinstance(instr, list):
				partitions.append([instr, curr_part])
			elif instr[1] == '<':
				if curr_part[instr[0]][0] < instr[2]:
					part_copy = copy.deepcopy(curr_part)
					part_copy[instr[0]][1] = instr[2]
					partitions.append([instr[3], part_copy])
					curr_part[instr[0]][0] = instr[2]
			else:
				if curr_part[instr[0]][1] > instr[2] + 1:
					part_copy = copy.deepcopy(curr_part)
					part_copy[instr[0]][0] = instr[2] + 1
					partitions.append([instr[3], part_copy])
					curr_part[instr[0]][1] = instr[2] + 1

print(s)