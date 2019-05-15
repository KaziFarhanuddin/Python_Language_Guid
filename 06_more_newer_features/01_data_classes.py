from dataclasses import dataclass

@dataclass
class test_data_frame:
	"""This is a test data frame class"""
	name:str
	age:str


obj_1 = test_data_frame('obj_1', "21")
obj_2 = test_data_frame('obj_2', 21)

print(f'{obj_1.name} is of {obj_1.age} years old', end="\n\n")

print(f'{obj_2.name} is of {obj_2.age} years old')



