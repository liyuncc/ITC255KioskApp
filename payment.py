class Payment():
    def __init__(self, amount, type):
        self.amount=amount
        self.type=type
    
    def __str__(self):
        self.amount=round(self.amount,2)
        response="Your payment today will be " + str(self.amount)
        return response

    def getType(self):
        return self.type

    def __str__(self, type):
        return self.type
   
        
    
    
        