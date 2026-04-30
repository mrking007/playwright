text ="Mathankumar"
print("Before reverse the string",text[::-1])
newText =""
for i in text:
    newText = i+ newText
print(newText)

#swap two numbers without using thrid variable:
a,b=10,20
print("Before swap",a,b)
a,b=b,a
print("after swap",a,b)

#check  its polindrome or not
def func(text):
    if text == text[::-1]:
        print("its Polindrom")
    else:
        print("its not polindrome")
func("AMMA")

#factorialNumber:
a=int(input("Enter a number"))
def fact(a):
    if a ==1:
        return a
    else:
        return (a*fact(a-1))
obj=fact(a)
print(fact(a))
