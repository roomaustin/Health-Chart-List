class Person:
    def __init__(self, name):
        self.name = name
        self.mental_conditions = []
        self.physical_conditions = []
        
    def add_mental_condition(self, condition):
        if condition not in self.mental_conditions:
            if condition.lower() in ["stress", "anxiety", "depression"]:
                self.mental_conditions.append(condition)
                print(f"{condition} added to {self.name}'s mental conditions.")
            else:
                print(f"{condition} is not recognized as a valid mental condition in this system.")
        else:
            print(f"{self.name} already has a diagnosis of {condition}.")

    def add_physical_condition(self, condition):
        if condition not in self.physical_conditions:
            self.physical_conditions.append(condition)
            print(f"{condition} added to {self.name}'s physical conditions.")
        else:
            print(f"{self.name} already has a diagnosis of {condition}.")
            
    def get_conditions(self):
        print(f"{self.name}'s mental conditions: {self.mental_conditions}")
        print(f"{self.name}'s physical conditions: {self.physical_conditions}")


# usage
person = Person("John Doe")
person.add_mental_condition("stress")
person.add_mental_condition("anxiety")
person.add_mental_condition("lung cancer")  # not a recognized mental condition in this system
person.add_physical_condition("lung cancer")
person.get_conditions()
