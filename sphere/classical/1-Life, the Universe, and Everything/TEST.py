la = []
def rawInputTest():
	x = input()
	if x != "42":
		la.append(x)
	else:
		return 1

print("Input: ")
while(True):
	r = rawInputTest()
	if r == 1:
		break

print("Output:")
for i in range(len(la)):
	print(la[i])
			
