import csv
import random
class Person(object):
	def __init__(self, name, size):
		self.name = name
		self.size = size
	def isSize(self, asked):
		return (asked in self.size)
	def __str__(self):
		return self.name + " sizes: "+self.size


people_list = list(csv.reader(open('raffle.csv')))
people = []
for person in people_list:
	people.append(Person(person[1],person[3]))

if __name__ == "__main__":
	for size in ["Women's Small","Men's Small","Men's Medium","Men's Large","Men's XL"]:
		print size
		sized_people = [i for i in people if i.isSize(size)]
		while len(sized_people)>0 and bool(raw_input("Press enter to go to next")):
			person_who_won = random.choice(sized_people)
			print person_who_won
			people.remove(person_who_won)
			sized_people.remove(person_who_won)


