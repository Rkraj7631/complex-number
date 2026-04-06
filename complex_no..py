class Complex:
    def __init__(self,r,i):
        self.real=r
        self.img=i
        self.add=[]

    def addition(self,other):
        #real=self.real+other.real
        #img=self.img+other.img
        return Complex(self.real+other.real,self.img+other.img)
    
    def substraction(self,other):
        #real=self.real-other.real
        #img=self.img - other.img
        return Complex(self.real-other.real,self.img-other.img)

    def multiplication(self,other):
        real=self.real*other.real-self.img*other.img
        img=self.real*other.img+self.img * other.real
        return Complex(real,img)
    
    def division(self,other):
        denominator=(other.real**2)-(other.img**2)
        real=(self.real*other.real+self.img*other.img)/denominator
        img=(self.img*other.real - self.real*other.img)/denominator
        return Complex(real,img)

    def display(self):
        print(f"{self.real}+{self.img}i")


r1=int(input("Enter first real Part : "))
i1=int(input("Enter first img Part : "))

r2=int(input("Enter second real part : "))
i2=int(input("Enter second img part : "))

c1=Complex(r1,i1)
c2=Complex(r2,i2)

c1.addition(c2).display()
c1.substraction(c2).display()
c1.multiplication(c2).display()
c1.division(c2).display()


