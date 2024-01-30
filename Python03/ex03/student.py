import sys

class Person:
	def __init__(self,nome:str,cognome:str) -> None:
		self.nome = nome
		self.cognome = cognome
	def __str__(self) -> str:
		return(f"{self.nome} {self.cognome}")

class Student(Person):
	def __init__(self, nome: str, cognome: str, corso = None) -> None:
		super().__init__(nome, cognome)
		self.corso = corso
	def __str__(self) -> str:
		if self.corso is None:
			return(f"{self.nome} {self.cognome} is not registered to any course")
		return (f"{super().__str__()} is registered to {self.corso}")

if __name__ == "__main__":

	name = input("Insert first name: ")
	surname = input("Insert last name: ")
	flag = input("Are you a student? (y/n)")
	while True:
		if  flag == "n":
			persona = Person(name,surname)
			print(persona)
			break
		elif flag == "y":
			corso = input("Please insert your degree course: ")
			student = Student(name,surname,corso)
			print(student)
			break
		else:
			flag = input("Please type \"y\" or \"n\": ")
