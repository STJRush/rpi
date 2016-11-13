import readchar

while True:
	c = readchar.readchar()
	key = readchar.readkey()

	if key == "w":
		print("up")
	elif key == "s":
                print("down")
	elif key == "a":
                print("left")
	elif key == "d":
                print("right")


	elif key == "z":
		print("exiting")
		break
