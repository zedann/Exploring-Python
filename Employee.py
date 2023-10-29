class Employee:
    def __init__(self , name , age , department , is_manager):
        self.name = name
        self.age = age
        self.depart=department
        self.is_manager=is_manager
    def is_retired(self):
        return True if self.age >= 50 else False
    
class Engineer(Employee):
    def __init__(self , name , age , depart , is_manager , specialization):
        super().__init__(name , age , depart , is_manager)
        self.specialization = specialization
    
