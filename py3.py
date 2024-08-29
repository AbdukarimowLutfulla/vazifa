class Odam:
    def __init__(self, ism):
        self.ism=ism

    def yugurish(self):
        print("Hello "+ self.ism)
    def yiqilish(self):
        print("Hello "+ self.ism)


ism=input("Ism kiriting: ")
o1 =Odam(ism)
o1.yugurish()
o1.yiqilish()
