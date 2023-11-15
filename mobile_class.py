# Define a class
class mobile():
    def __init__(self, CompanyName, Storage, SerialNum, Name, dualsim,Support4k):
        self.CompanyName = CompanyName
        self.Storage = Storage
        self.SerialNum = SerialNum
        self.Name = Name
        self.dualsim = dualsim
        self.support4k = Support4k
        

# Function that avoid repetition of the sentence
    def mobiles(self):
        print("CompanyName {} ,Storage {} ,SerialNum {}, Name {}, DualSim {}, support4k {}".format(self.CompanyName ,self.Storage, self.SerialNum, self.Name, self.dualsim, self.support4k))

# Nominate the information of mobile
Iphone = mobile("Iphone", "64Gb","IP14PM", "Iphone 14 pro max",False, True)
Samsung =mobile("Samsung", "64GB","SGS10", "Samsung Glaxy s10",True, False)
Iphone.mobiles()
Samsung.mobiles()
