print("hello world")

noofcars=0
noofbikes=0
noofcars=input("Enter the no of cars ")
print (noofcars)

noofbikes=input("Enter the no of bikes ")
print (noofbikes)
bikes=int(20*int(noofbikes))
print(bikes)
revenue=int(noofbikes)*20+int(noofcars)*40
print ("Total revenues is collected - " +str(revenue))

if(revenue > 500):
    print("today is profitable day")
else:
    print("today is loss")
inital=input("please enter initial value")
final=input("please last number")
for index in range (int(inital),int(final)):
    if (index%2==0):
      print(index, "is even")
    else:
      print(index, "is odd")
    print(index)


marks=[45,47,48]
names=["ajit","abc","qwe"]

for index in marks:
    if (marks[index]<=30):
        print(names[index] +"is falied")
    else:
        print(names[index] +"is passed")
        total=total+marks[index]
        print(total)