class person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
class mf(person):
    def setgender(self, gen):
        self.gender = gen
    def getgender(self):
        return(self.gender)

def main():
    avinash = mf(13, "Avinash")
    sadhana = mf(34, "Sadhana")
    print(avinash.age)
    print(sadhana.age)

main()
