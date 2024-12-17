import pygame
pygame.init()

graphic = pygame.image.load("graphic.bmp")

stream = []
p = False
run_length = 0

for x in range(graphic.get_width()):
	for y in range(graphic.get_height()):
		pixel = graphic.get_at((x, y))[0] != 0
		print(pixel)

		if pixel == p:
			if run_length == 0xF:
				stream.append(run_length)
				stream.append(0)
				run_length = 0

		else:
			stream.append(run_length)
			run_length = 0

		p = pixel
		run_length += 1

byte_count = len(stream) // 2
sector_size = 512
sizes = {}
i = 0

while byte_count > 0:
	size = min(byte_count, sector_size)
	sizes[i] = size

	print(f"graphic_i{i}:")

	remaining = size
	j = 0

	while remaining > 0:
		print("\tdb ", end="")

		for k in range(min(remaining, 8)):
			byte = stream[(i + j + k) * 2] << 4 | stream[(i + j + k) * 2 + 1]
			print(f"0x{byte:02X}, ", end="")

		print()
		j += 8
		remaining -= 8

	i += sector_size
	byte_count -= sector_size

for k, v in sizes.items():
	print(f"GRAPHIC_I{k}_SIZE equ {v}")

print(f"GRAPHIC_W equ {graphic.get_width()}")
print(f"GRAPHIC_H equ {graphic.get_height()}") 
