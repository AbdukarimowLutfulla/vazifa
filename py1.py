class Odam:
    def __init__(self, ism):
        self.ism=ism

    def salomlashish(self):
        print("Hello "+ self.ism)


ism=input("Ism kiriting: ")
odam =Odam(ism)
odam.salomlashish()