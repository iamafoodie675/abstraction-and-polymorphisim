class India():
    def capital(self):
        print("New Delhi is the capital of India.")
        
    def Language(self):
        print("Hindi is the most widely spoken language in India. ")
        
    def type(self):
        print("India is a developing country.")
        
        
class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")
        
    def Language(self):
        print("Bengali is the mother language in India. ")
        
    def type(self):
        print("Bangladesh is a developing country.")
        
        
objInd =India()
objBD = Bangladesh()

for country in (objInd,objBD):
    country.capital()
    country.Language()
    country.type()
    print()