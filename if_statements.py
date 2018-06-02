# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the peron you know: ")

# if person in know_people:
# 	print("You know {}!".format(person))
# else:
# 	print("You don't {}!".format(person))


##Exercise

def who_do_you_know():
	people = input("List some people that you know seperated by commas: ")
	
	return [person.strip() for person in people.split(",")]


def ask_user():
	
	name = input("Give us a name: ")
	if name in who_do_you_know():
		print("You know {}".format(name))


ask_user()