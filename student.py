class student:
    def __init__(self,Lname,Fname,ssn,email,age):
        self.Lname = Lname
        self.Fname = Fname
        self.ssn   = ssn
        self.email = email
	self.age   = int(age)

    def __eq__(self,other):
        return self.ssn == other.ssn
    
    def __ge__(self,other):
        return self.ssn == other.ssn
    
    def __le__(self,other):
        return self.ssn <= other.ssn

    def __lt__(self,other):
        return self.ssn <= other.ssn

    
