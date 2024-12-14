class Bank:
    def __init__(self,acc_no,bal):
        self.acc_no =acc_no
        self.bal = bal

    def setAcc_no(self,no):
        self.acc_no = no

    def setBal(self,bal):
        self.acc_no = bal

    def getAcc_no(self):
        return self.acc_no
    
    def getBal(self):
        return self.bal


print("Im going to Bank and set Vijay' acc no and Balance directly, without any valdiation of who i am")
vijay = Bank(12345,100)
print(f"Directly going to Bank and accesing Vijay's account no and balance, without any secutiy Acc No: {vijay.acc_no}, Balance: {vijay.bal}")
print("*"*20)
print("Using Getters and Setters")
vijay.setAcc_no(7891)
vijay.setBal(500)
print(f"vijay's acc no and bal can't be just accessed directly, going to teh Bank, its secured now, we can access it onyl usign getter and setter methods. Acc no:{vijay.getAcc_no()} Bal: {vijay.getBal()}")
print("Encapsulation is hiding data inside methods. Getter and setter methods helps to achvie that, by not allowing direct access of the isntance variables, iwth just ref variable. We ened respective getter and setter methods. ALthpopoguh we didn;t set here any security, but we can include valdiation and security conditions inside the getter and setter methods, scuh that not eveyone woul eb able toa ccess Viajy's acc no and Balance, so that accessing the instance variable becomes more secure. We create  'n' getters and setters methods, for 'n' instance variables individualy, i.e good coding practice,instead of creating by combining all into a singel method. Althouhg ensupation provides secuirt, usign it , makes the code longer, slower execution")
