iterations = 3**5
for number in range(0, iterations):
	number += 1
	if number % 3 == 1:
		Ursula2_pro = "she"
	elif number % 3 == 2:
		Ursula2_pro = "he"
	elif number % 3 == 0:
		Ursula2_pro = "they"
	print Ursula2_pro