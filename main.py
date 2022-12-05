class Profile:
    def __init__(self,name,run,email):
        self.name = name
        self.rut = run
        self.email = email
        self.balance = 0
    def deposit(self,ammount):
        self.balance += ammount
        
    def print(self):    
        print("Su nombre:",self.name)
        print("Su rut es :",self.rut)
        print("Su email es: ",self.email)
        print("Su dinero en cuenta es:",self.balance)
        