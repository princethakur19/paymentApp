class hooby:
    def car(self, name=None):
        if name:
            print(f"{name} is nice car!!")
        else:
            print("Which car you own?")

h = hooby()
h.car()
h.car("Brezza")
