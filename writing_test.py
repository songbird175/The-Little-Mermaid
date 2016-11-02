for i in range(0,5):
	i += 1

	working_file = open("Python_test%s.txt" % i, 'w')
	working_file.write("This is a test. \n")
	working_file.write("Test number two")
	