file = open("constant/polyMesh/boundary", "r")
lines = file.readlines()


here = lines.index('    outerCylinder\n')

lines[here+2] = '        type            symmetry;\n'
lines[here+3] = '        inGroups        1(symmetry);\n'

file = open("constant/polyMesh/boundary", "w")

for line in lines:
	file.write(line)




