# caculate the sum of even number from 0 to 100

result = 0
i = 0
while i <= 100:
	if i % 2 == 0:
		print(i)
		result += i

	i += 1
print ('the sum of even number from 0 to 100 is = %d' % result)