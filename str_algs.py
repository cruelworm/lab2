# Part 2 - Strings
str1 = "Hello, World!"
def revstr(str):
	newstr = ""
	for i in range(len(str)):
		newstr+=str[-i-1]
	print(str, "--->", newstr)

print("\nРабота со строками:\nВызов функции:", end=" ")
revstr(str1)

