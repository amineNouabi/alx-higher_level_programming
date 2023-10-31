#!/usr/bin/python3

delta = ord("a") - ord("A")
bobo = False

for ch in range(ord("z"), ord("a") - 1, -1):
	to = ch
	if bobo:
		to = ch - delta
	else:
		to = ch
	bobo = not bobo
	print("{}".format(chr(to)), end="")
