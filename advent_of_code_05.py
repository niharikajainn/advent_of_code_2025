def main():	
	part_two(part_one())
	
def parse():
	ranges = [tuple(map(int,tuple(line.strip().split("-")))) for line in open("aoc_5_ranges.txt", "r").readlines()]
	ingredients = [int(line.strip()) for line in open("aoc_5_ingredients.txt", "r").readlines()]
	return ranges, ingredients

def part_one():
	ranges, ingredients = parse()
	range_map = dict()
	for fresh_range in sorted(ranges):
		merged_into_existing = False
		first, last = fresh_range
		for key in range_map:
			if first <= range_map[key]:
				if range_map[key] <= last:
					range_map[key] = last
				merged_into_existing = True
		if not merged_into_existing:
			range_map[first] = last

	count_fresh = 0
	for ingredient in ingredients:
		for key in range_map:
			if key <= ingredient <= range_map[key]:
				count_fresh += 1
				break

	print(count_fresh)
	return range_map

def part_two(range_map):
	count_fresh_ids = 0
	for key in range_map:
		count_fresh_ids += range_map[key] - key + 1
	print(count_fresh_ids)


if __name__=="__main__":
    main()
