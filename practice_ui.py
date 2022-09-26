class TextInput:
    def __init__(self):
        self.cvalue = ''
    def add(self,character) : 
           self.cvalue = self.cvalue + character    
    def get_value(self):  
        return self.cvalue 
        
class NumericInput(TextInput):
    def add(self,character):
        if not character.isalpha():
           self.cvalue = self.cvalue + character      
        
if __name__== '__main__':
    input = NumericInput()
    input.add("1")     
    input.add("a")   
    input.add("0") 
    print(input.get_value())      