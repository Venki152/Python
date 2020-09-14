# Unit 3 1a lists lab

sportsL = ["Cricket", "Badminton", "Squash", "Racquetball", "Tennis"]

print(sportsL)

l = len(sportsL)
print('Length of the list is', l)
sportsL[2] = "Football" #replace index 2 element with Football
print('Below is the updated list\n',sportsL)


# sportsL.insert(2,"Football")
# sportsL.pop(3)


#r = sportsL[2]
#print(r)
#sportsL.replace(r, "Football")



# ------------------ Lab 1b

#import statistics as st
NumList = [2, 3, 4, 88, 525, 345, 1, 16]  #create NumList
sum = 0  #initiate sum with 0

for i in NumList:
    sum = sum + i

avg = sum/ len(NumList)     # average by diving total sum with number of elements
print(avg)

NumList.remove(525)
print(NumList)

sum = 0         #set sum to 0 as we recalculate for the elements of list
for i in NumList:
    sum = sum + i

avg = sum/ len(NumList)     # average by diving total sum with number of elements
print(round(avg,2))

