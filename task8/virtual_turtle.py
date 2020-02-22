def turtle(coord, direction):
	command = yield coord
	while command:
		if command == 'f':
			if direction == 0:
				coord = coord[0] + 1, coord[1]
			elif direction == 1:
				coord = coord[0], coord[1] + 1
			elif direction == 2:
				coord = coord[0] - 1, coord[1]
			else:
				coord = coord[0], coord[1] - 1
		elif command == 'l':
			direction = (direction + 1) % 4
		else:
			direction = (direction - 1) % 4
		command = yield coord
