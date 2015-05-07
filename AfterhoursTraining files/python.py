'''
print ("I am gone")
Print ("so am I")
'''

#print ("I am here")
'''
g = 1
b = 10
print (g + b)

a = "0"
b = "2"
print (a + b)

a = "0"
b = "20"
print (int(a) + int(b))

a = 0
a += 2
print (a)

a = 21
if a >= 22:
	print ("if")
elif a >= 21:
	print ("else if")
else:
	print ("else")

def someFunction(a, b):
	print (a + b)
someFunction(12, 451)

def someFunction():
	print (a)
someFunction()

for a in range (1, 20):
	print (a)

a = 1
if a == 0:
	while a < 10:
		print (a)
#infinate loops for the lulz skipped because its not satisfied 
else:	
	while a < 100:
		print (a)
		a += float(21.9918)

myString = ""
print (type(myString))

a = "string"
print (a[1:3])
print (a[:-1])

sampleList = [1,2,3,4,5,6,7,8]
print (sampleList[1])
'''

'''
sampleList = [1,2,3,4,5,6,7,8]
for a in sampleList:
	print (a)

sampleList = [1,2,3,4,5,6,7,8]
sampleList.reverse()
print (sampleList)

myList2 = [1,2,3]
myList2.append(5)
print (myList2)

myTuple = (1,2,3)
print (myTuple)

myTuple2 = (1,2,3)
myList = list(myTuple2)
myList.append(4)
print (myList)

myExample = {'someItem': 2, 'otherItem': 20}
print(myExample['someItem'])

myExample = {'someItem': 2, 'otherItem': 20}
myExample['newItem'] = 400
for a in myExample:
	print (a, myExample[a])

print('The order total comes to %f' % 123.44)
print('the order total comes to %.1f' % 123.444)

a ="abcdefghijklmnopqrstuvwxyz"
print('%.20s' % a)

var1 = '1'
try:
	var1 = var1 + 1
except:
	print(var1, "is not a number")
print(var1)

'''

'''

var1 = '1'
try:
	var2 = var1 + 1
except:
	var2 = int(var1) + 1
print(var2)

f = open("test.txt", "r")
print (f.read(1))
print (f.read())

f = open("test.txt", "r")
print(f.readline())
print(f.readline())

'''
'''
f = open("test.txt", "r")
myList = []
for line in f:
	myList.append(line)
print(myList)
'''
'''
f = open("test.txt", "r")
print(f.read(1))
print(f.read())
f.close()
'''
'''
f = open("test.txt", "w")
f.write("I am a test file.")
f.write("Maybe someday, he will promote me to a real file.")
f.write("Man, I long to be a real file")
f.write("and hang out with all my new real file friends.")
f.close()
'''

'''
f = open("test.txt", "w")
f.write("Maybe someday, he will promote me to a real file. \n")
'''
'''
f = open("test.txt", "a")
f.write("and can I get some pickles on that")
f.close()
'''

class Calculator(object):
	def __init__ (self):
		self.current = 0
	def add(self, amount):
		self.current += amount
	def getCurrent(self):
		return self.current
