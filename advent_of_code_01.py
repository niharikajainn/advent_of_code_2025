rotations = [line.strip() for line in open("aoc_1.txt", "r").readlines()]

def main():		
	part_one()
	part_two()


def part_one():
	index = 50
	count_zeros = 0
	for rotation in rotations:
		direction, ticks = rotation[0], int(rotation[1:])

		allowance = index
		if (direction == "R"):
			allowance = 100 - index
		ticks_past_first_zero = ticks - allowance
		final_leftover = ticks_past_first_zero % 100
		index = final_leftover

		if (final_leftover > 0 and direction == "L"):
			index = 100 - final_leftover

		if index == 0:
			count_zeros += 1

	print("ended at zero", count_zeros, "times total")

def part_two():
	index = 50
	count_zeros = 0
	for rotation in rotations:
		direction, ticks = rotation[0], int(rotation[1:])

		allowance = index
		if (direction == "R"):
			allowance = 100 - index

		ticks_past_first_zero = ticks - allowance
		if allowance > 0 and ticks_past_first_zero > 0:
			count_zeros += 1
		final_leftover = ticks_past_first_zero % 100

		full_rotations = int(ticks_past_first_zero / 100)
		if full_rotations > 0 and final_leftover == 0:
			count_zeros -= 1
		count_zeros += full_rotations
		index = final_leftover

		if (final_leftover > 0 and direction == "L"):
			index = 100 - final_leftover

		if index == 0:
			count_zeros += 1

	print("passed zero", count_zeros, "times total")

if __name__=="__main__":
    main()
