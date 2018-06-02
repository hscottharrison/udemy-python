my_variable = "hello"
grades = [77, 80, 90] #ordered (in order of creation) and mutable
tuple_grades = (77, 80, 90) #immutable
set_grades = {77, 80, 90, 100, 100} #unique and unordered

#This is how you mutate a tuple similar to Immutable.js
# tuple_grades = tuple_grades + (100,)
# print(tuple_grades)

# print(grades[0])


##Set Operations

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 7, 5, 11}

# print(set_one.intersection(set_two))
# print(set_one.union(set_two))
print({1, 2, 3, 4}.difference({1, 2}))