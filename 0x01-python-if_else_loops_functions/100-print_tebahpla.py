#!/usr/bin/python3

delta = ord("a") - ord("A")
bobo = False

for ch in range(ord("z"), ord("a") - 1, -1):
	to = ch
	if bobo:
		to = chr(ch - delta)
	else:
		to = chr(ch)
	bobo = not bobo
	print("{}".format(to), end="")
