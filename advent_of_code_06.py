import csv
import numpy as np

def parse():
	csvfile = open("aoc_6.csv")
	reader = csv.reader(csvfile, delimiter = " ")
	worksheet = [[term for term in math_list if term] for math_list in reader]
	operations = worksheet[-1]
	return worksheet, operations

def main():
	worksheet, operations = parse()
	part_one(worksheet, operations)
	part_two(operations)

def part_one(worksheet, operations):
	arr = np.array([[int(term) for term in row] for row in worksheet[0:-1]]).T
	mults = np.prod(arr, axis=1)
	sums = np.sum(arr, axis=1)
	
	total = 0
	for idx, operation in enumerate(operations):
	 	if operation == "*":
	 		total += mults[idx]
	 	else:
	 		total += sums[idx]

	print(total)

def part_two(operations):
	worksheet = [line.rstrip("\n") for line in open("aoc_6.txt", "r").readlines()[0:-1]]
	arr = np.array(worksheet)
	total_result = 0
	operation_idx = 0
	operation = operations[operation_idx]
	column_result = 0 if operation == "+" else 1

	for idx in range(0, len(arr[0])):
		concat_num = ""
		for row in arr:
			concat_num += row[idx]
		num_str = concat_num.strip()

		if num_str != "":
			column_result = column_result + int(num_str) if operation == "+" else column_result * int(num_str)
		else:
			total_result += column_result
			operation_idx += 1
			operation = operations[operation_idx]
			column_result = 0 if operation == "+" else 1
	total_result += column_result
	
	print(total_result)

if __name__=="__main__":
    main()

