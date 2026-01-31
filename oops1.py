class employee:
    def __init__(self):
        print("started executing data and atributes")
        self.id = 123
        self.salary = 50000
        self.designation = "data analyst"
        print("finished executing data and atributes")

    def travel(self,destination):
        print("this travel function was called manually")
        print(f"employee is travelling to {destination}")

sam = employee()

print(sam.id)
print(sam.salary)
print(sam.designation)
sam.travel("kerala")
