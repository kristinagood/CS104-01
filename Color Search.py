first = 0
last = len - 1
found = False
while first <= last and not found:
    mid = (first + last)/2
    if key == data[middle]:
        found = True
    else:
        if (key < data[middle]):
            last = [middle] - 1
else:
        first = [middle] + 1


data = [aqua,brown,chartreuse,darkbrown,green,indigo,lavendaer,magenta,red,violet,yellow]
list1.sort()
print(list1)
key = int(input("enter the key:"))
BinarySearch(list1,key)
