output = ["[("]
for i in range(0, 100, 8):
	output.append("    {0}, {1}, {2}, {3},".format(i,i+2,i+4,i+6))
output.append("), \n(")
for i in range(1, 101, 8):
    output.append("    {0}, {1}, {2}, {3},".format(i,i+2,i+4,i+6))
output.append(")]")
print "\n".join(output)