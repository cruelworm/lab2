# Part 3 - Dictionaries
emps = []
emps.extend([
	{
		"name" : "Иванов И.И.",
		"age" : 23,
		"children" : []
	},
	{
		"name" : "Васильева В.В.",
		"age" : 45,
		"children" :
			[
				{
					"name" : "Валерий",
					"age" : 17
				},
				{
					"name" : "Вера",
					"age" : 12
				}
			]
	},
	{
		"name" : "Петров П.П.",
		"age" : 67,
		"children" :
			[
				{
					"name" : "Павел",
					"age" : 34
				}
			]
	},
	{
		"name" : "Максимова М.М.",
		"age" : 89,
		"children" :
			[
				{
					"name" : "Антон",
					"age" : 56
				},
				{
					"name" : "Антонина",
					"age" : 55
				}
			]
	}
	])
	
print("\nРабота со словарями:")
print("Сотрудники с совершеннолетними детьми:")
for i in emps:
	for j in i["children"]:
		if j["age"] >= 18:
			print(i["name"])
			break
