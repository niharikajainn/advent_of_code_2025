import itertools

paper_map = [list(line.strip()) for line in open("aoc_4.txt", "r").readlines()]
num_rows = len(paper_map)
num_cols = len(paper_map[0])

def main():		
	part_one()
	part_two()

def part_one():
	count_accessible_paper = 0
	for row in range(num_rows):
		for col in range(num_cols):
			node = row, col
			if is_paper(*node):
				adjacents = children(*node)
				if len(adjacents) < 4:
					count_accessible_paper += 1
	print(count_accessible_paper, "rolls of paper are accessible by the forklift.")

def part_two():
	count_accessible_paper = 0
	paper_left = True
	while paper_left:
		accessible_papers = set()
		for row in range(num_rows):
			for col in range(num_cols):
				node = row, col
				if is_paper(*node):
					adjacents = children(*node)
					if len(adjacents) < 4:
						accessible_papers.add(node)
						count_accessible_paper += 1
		if len(accessible_papers) == 0:
			paper_left = False
		for paper in accessible_papers:
			paper_map[paper[0]][paper[1]] = '.'
		
	print(count_accessible_paper, "rolls of paper are accessible by the forklift.")

def children(row,col):
	children_rows = [row]
	children_cols = [col]
	if(row > 0):
		children_rows.append(up(row))
	if(row < num_rows-1):
		children_rows.append(down(row))
	if(col > 0):
		children_cols.append(left(col))
	if(col < num_cols-1):
		children_cols.append(right(col))
	indices = list(itertools.product(children_rows, children_cols))[1:]
	children = []
	for adj_row, adj_col in indices:
		if(is_paper(adj_row, adj_col)):
			children.append((adj_row, adj_col))
	return children

def is_paper(row,col):
	return paper_map[row][col] == '@'

def up(row):
	return(row-1)

def down(row):
	return(row+1)

def left(col):
	return(col-1)

def right(col):
	return(col+1)

if __name__=="__main__":
    main()
