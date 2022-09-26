class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        myscoop = []
        for x in self.ingredients:
            for y in self.toppings:
               myscoop.append([x,y])
        return myscoop

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]