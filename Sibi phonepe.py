class phonepe:
    def __init__(self):
        print("WELCOME TO PHONEPE")
        self.phno=input("Enter Your Phone No:")
        self.email=input("Enter Your Email Address:")
        self.username=input("Enter Your Username:")
        self.bankdetails=int(input("Enter Your Bank Details:"))
        self.otp=int(input("Enter Your OTP:"))
        self.setpin=int(input("Enter Your PIN:"))
        #self.firsttransaction=happy

    def openphonepe(self):
        print("WELCOME TO PHONEPE")

     
    def phonenumber(self):
         if len(self.phno)==10:
             print("phonenumber verified")
         else:
             raise ValueError("incorrect phno")


    def emailverification(self):
         if len(self.email)<=30:
             if type(self.email)==str:
                 print("email verified")
             else:
                 raise TypeError("email is not valid")
         else:
             raise ValueError("email should contain only 30 character")


    def usernameverification(self):
         if type(self.username)==str:
             if len(self.username)<=20:
                 print("username verified")
             else:
                 raise ValueError("username is not valid")
         else:
             raise TypeError("the printed name cannot be used")


    def bankdetailsverification(self):
        print("enter bank name")
        if type(self.bankname)==str:
            print("bankname verified")
        else:
            raise TypeError("The bank name is not valid")

    def setotp(self):
        if (type(self.otp)==int):
            print("otp verified")
        else:
            raise ValueError("otp not correct")


        

anu=phonepe()
anu.openphonepe()
anu.phonenumber()
anu.emailverification()
anu.usernameverification()
anu.bankdetailsverification()
anu.setotp()        
