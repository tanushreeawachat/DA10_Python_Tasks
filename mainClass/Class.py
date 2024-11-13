
# import statistics
class firstClass:
    val1 = 0
    val2 = 0
    val3 = 0
    val4 = 0
    val5 = 0
    def __init__(self,a,b,c,d,e):
        print('this is constructor')
        self.val1 = a
        self.val2 = b
        self.val3 = c
        self.val4 = d
        self.val5 = e

    def addValue(self):
        print(f'addition = {self.val1 + self.val2 +self.val3 + self.val4 + self.val5}')

    def subValue(self):
        print(f'substract = {self.val1 - self.val2 - self.val3 - self.val4 - self.val5}')

    def mulValue(self):
        print(f'multiply = {self.val1 * self.val2 * self.val3 * self.val4 * self.val5}')

    def divValue(self):
        print(f'division = {self.val1 / self.val2 / self.val3 / self.val4 / self.val5}')

    def modulusValue(self):
        print(f'modulus = {self.val1 // self.val2 // self.val3 // self.val4 // self.val5}')

    def minValue(self):
       print( f'minimum = {min(self.val1 , self.val2 , self.val3 , self.val4 , self.val5)}')
   
    def maxValue(self):
        print(f'maximum = {max(self.val1 , self.val2 , self.val3 , self.val4 , self.val5)}')

    def meanValue(self):
        print(f'mean = {(self.val1 + self.val2 + self.val3 + self.val4 + self.val5) / (5) }')

  


f1 = firstClass(10,2,3,6,5)
f1.addValue()
f1.subValue()
f1.mulValue()
f1.divValue()
f1.modulusValue()
f1.minValue()
f1.maxValue()
f1.meanValue()
# f1.medianValue()


print('f1.val1 = ',f1.val1)
print(f'f1.val2 = ,{f1.val2}')
print(f'f1.val3 = ,{f1.val3}')
print(f'f1.val4 = ,{f1.val4}')
print(f'f1.val5 = ,{f1.val5}')


    


