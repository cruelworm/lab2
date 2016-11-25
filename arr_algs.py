# Part 1 - Arrays
print("Работа с массивами:")
arr = list(range(20))
for x in arr:
	if x%2 == 1:
		arr[x] = x**2 - x*15
	else:
		arr[x] = x**3 - x*20
print(arr)

def minarr(arr):
	min = arr[0]
	for x in arr:
		if x < min:
			min = x
	return min
	
def avgarr(arr):
	sum = 0
	for x in arr:
		sum+=x
	return sum/len(arr)

print("Наименьший элемент массива:", minarr(arr))
print("Среднее значение массива:", avgarr(arr))
