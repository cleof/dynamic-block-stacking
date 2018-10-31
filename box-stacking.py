import sys
import itertools

# return relevant dimension permutations 
# (weight >= depth and weight/depth dimension combinations are not repeated)
def blockOrientations(dimension):
	b = dimension[0]
	w = dimension[1]
	h = dimension[2]
	orientations = []
	perms = [p for p in itertools.permutations(dimension)]
	for d, w, h in perms:
		if w >= d:
			orientations.append((d, w, h))
	return orientations

# print(blockOrientations((1, 4, 10)))

# Input: dimensions will be a list of tuples of the form (d, w, h)
def blockStacking(dimensions):

	# generating all possible orientations for the input list of dimensions
	blocks = []
	for dimension in dimensions:
		for o in blockOrientations(dimension):
			blocks.append(o)

	# calculating list of base sizes for blocks
	base_sizes = []
	for block in blocks:
		base = block[0]*block[1]
		base_sizes.append(base)

	# zipping our list of blocks to their corresponding base_sizes
	zipped_sizes = zip(blocks, base_sizes)

	# sorting blocks based on base size, ascending order
	zipped_sizes = sorted(zipped_sizes, key=lambda x: x[1])
	sorted_blocks = [dim for dim, base in zipped_sizes]

	# sort by decreasing area
	sorted_blocks.reverse()

	# initializing our DP table with individual block height
	max_stack = [sorted_blocks[i][2] for i in range(len(sorted_blocks))]
	count_blocks = [1 for i in range(len(sorted_blocks))]
	block_solutions = [[sorted_blocks[i]] for i in range(len(sorted_blocks))]

	# height will be at block[2], calculating total height using this value
	# generate our DP table from bottom-up
	for i in range(1, len(max_stack)):
		for j in range(i):
			if (sorted_blocks[i][0] < sorted_blocks[j][0]) and (sorted_blocks[i][1] < sorted_blocks[j][1]) and (max_stack[i] < max_stack[j] + sorted_blocks[i][2]):
				max_stack[i] = max_stack[j] + sorted_blocks[i][2]
				count_blocks[i] = count_blocks[j] + 1
				block_solutions[i] = [dims for dims in block_solutions[j]]
				block_solutions[i].append(sorted_blocks[i])
	maximum = 0
	max_index = -1
	for i in range(len(max_stack)):
		if maximum < max_stack[i]:
			maximum = max_stack[i]
			max_index = i
	print("The tallest tower has " + str(count_blocks[max_index]) + " blocks and a height of " + str(maximum))
	return maximum, count_blocks[max_index], block_solutions[max_index]


# print(blockStacking([(2, 6, 8), (4, 4, 4), (1, 10, 4)]))

def read_file(input):
	with open(input,'r') as i:
		lines = i.readlines()
	dims = []
	for line in lines:
		dim = tuple(map(int, line.split()))
		dims.append(dim)
	del(dims[0])
	maximum, num_blocks, solutions = blockStacking(dims)
	return maximum, num_blocks, solutions

def convertOutput(output):
	line1 = str(output[0]) + '\n'
	lines = [line1]
	for i in range(1,len(output)):
		d, w, h = output[i]
		lines += [str(d) + " " + str(w) + " " + str(h) + " \n" ]
	print(lines)
	return lines

def output_file(input, output):
	maximum, num_blocks, solutions = read_file(input)
	soln_blocks = [s for s in solutions]
	lines = [num_blocks] + soln_blocks
	to_print = convertOutput(lines)
	with open(sys.argv[2], 'w') as f:
		for line in to_print:
			f.write(line)

output_file(sys.argv[1], sys.argv[2])