output = ["["]
offset = 10
for i in range(0+offset, 30+offset, 3):
	output.append("    ({0}, {1}, {2}),".format(i, i+1, i+2))
output.append("]")
print("\n".join(output))