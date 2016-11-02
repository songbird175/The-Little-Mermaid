iterations = 3**6
Ucount = 0
Scount = 0
Tcount = 0
Acount = 0

for number in range(0, iterations):
	number += 1

	working_file = open("Rewrite_%s" % str(number), "w")

	if number % 3 == 1:
		Ursula2_pro = "she"
		Ucount += 1

		if Ucount % 3 == 1:
			Ursula_pro = "she"
			Scount += 1

			if Scount % 3 == 1:
				Scuttle_pro = "she"
				Tcount += 1

				if Tcount % 3 == 1:
					Triton_pro = "she"
					Acount += 1

					if Acount % 3 == 1:
						Ariel_pro = "she"
					elif Acount % 3 == 2:
						Ariel_pro = "he"
					elif Acount % 3 == 0:
						Ariel_pro = "they"

				elif Tcount % 3 == 2:
					Triton_pro = "he"
				elif Tcount % 3 == 0:
					Triton_pro = "they"

			elif Scount % 3 == 2:
				Scuttle_pro = "he"
			elif Scount % 3 == 0:
				Scuttle_pro = "they"

		elif Ucount % 3 == 2:
			Ursula_pro = "he"
		elif Ucount % 3 == 0:
			Ursula_pro = "they"

	elif number % 3 == 2:
		Ursula2_pro = "he"
	elif number % 3 == 0:
		Ursula2_pro = "they"

	working_file.write("Version %s" % number + "\n")
	working_file.write("Ariel: %s," % Acount + " Triton: %s," % Triton_pro + " Scuttle: %s," % Scuttle_pro + " Ursula: %s," % Ursula_pro + " Transformed Ursula: %s" % Ursula2_pro)
	working_file.close()