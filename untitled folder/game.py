from card import card
class game:
    
    def __init__(self):
        self.score = 300
        self.play = True
        
    def things(self):
        while self.score > 0 and self.play:
            self.dothings()
            self.play = input("Play again? (y/n): ")
            if self.play == "n":
                self.play = False

    def dothings(self):
        carda = card()
        cardb = card()

        print ("Card A: " + str(carda.value))
        hilo = input("Higher or lower? (h/l): ")
        print ("Card B: " + str(cardb.value))

        if carda.value < cardb.value and hilo == "h":
            self.score += 100
        elif carda.value > cardb.value and hilo == "l":
            self.score += 100

        print ("Score: " + str(self.score))
