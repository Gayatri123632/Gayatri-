class car:
    def __init__(self,carname,model,cost,colour):
        self.carname=carname
        self.model=model
        self.cost=cost
        self.colour=colour
    def display(self):
        print("car name is:",self.carname)
        print("model is :",self.model)
        print("cost is :",self.cost)
        print("colour  is :",self.colour)
s1=car("hyndai","venue",1500000,"blue")
s1.display()
    
