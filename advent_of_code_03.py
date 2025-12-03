def main():	
	part_one()	
	part_two()

def parse():
	return [[int(battery) for battery in list(line.strip())] for line in open("aoc_3.txt", "r").readlines()]

def part_one():
	banks = parse()
	joltage = 0
	for bank in banks:
		max_left = bank[0]
		max_left_idx = 0
		for x in range(1, len(bank)-1):
			if bank[x] > max_left:
				max_left = bank[x]
				max_left_idx = x
		max_right = bank[max_left_idx+1]
		max_right_idx = max_left_idx+1
		for x in range(max_left_idx+1, len(bank)):
			if bank[x] > max_right:
				max_right = bank[x]
				max_right_idx = x
		joltage += max_left*10 + max_right
	print(joltage)

def part_two():
	banks = parse()
	joltage = 0
	for bank in banks:
		on_batteries = dict()
		max_idx = 0
		for battery_idx in range(0, 12):
			max_rating = bank[max_idx]
			for x in range(max_idx+1, len(bank)-(12-battery_idx)+1):
				if bank[x] > max_rating:
					max_rating = bank[x]
					max_idx = x
			joltage += 10 ** (11-battery_idx) * max_rating
			max_idx += 1
	print(joltage)


if __name__=="__main__":
    main()
