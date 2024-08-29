class Odam:
    def __init__(self, ism):
        self.ism=ism

    def kuylash(self):
        print(self.ism)
    def eshitish(self):
        print("Hello "+ self.ism)
    def gapirish(self):
        print("Hello "+ self.ism)


ism=input("Ism kiriting: ")
o1 =Odam(ism)
o1.kuylash()