class class_reverse:
    
    def __init__(self, s):
        self.s = s
        
    def revStr(self):
        return self.s[::-1]
    
str = input("Enter the word to be reversed: ")
o1 = class_reverse(str)
print("Reversed String is:", o1.revStr())
