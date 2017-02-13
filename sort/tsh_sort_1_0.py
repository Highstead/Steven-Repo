#Some kind of a sort
#The sort checks accounts for missing numbers
#and last number in array being smaller
#
# Array to be sorted
a = [10,2,6,7,3,5,8,1,13,15,4]
#
#Initalize variables
minIndex = 0
maxIndex = len(a)
lowestNum = min(a)
highestNum = max(a)
innerIndex = 0
outerIndex = 0
innerBuff = 0
buff = 0
n = 0
#
#Print initial Conditions
print "Inner Loop index is ", innerIndex
print "Outer Loop index is ", outerIndex
print "minIndex is         ", minIndex
print "maxindex is         ", maxIndex
print "lowestNumber is     ", lowestNum
print "highestNumber is    ", highestNum
print "Temp buffer is      ", buff 
#
print "###################################"
print ""
#
#start of sort
print "Array to be sorted"
print a
print ""
#Outer Loop search through array
#Finds the number to be ordered
while outerIndex < maxIndex:
#
#Search for the next lowest number in the array
    while a[innerIndex-1] != lowestNum: #find lowest number
         innerBuff = a[innerIndex] #next value in array
         innerIndex = innerIndex+1 #increment the inner loop array index
#
#Slot the next lowest number in order i the array
    if innerBuff == lowestNum:     #next lowest number found
        buff = a[outerIndex]       #temporary store lowest array location value
        a[outerIndex] = innerBuff  #store the the lowest number found 
        a[innerIndex-1] = buff     #swap the lowest number location with the stored number
    innerIndex = 0             #reset the inner loop to beginning of array
    lowestNum=lowestNum+1      #increase the lowestNum value of search by 1
 #
 #Check for missing number
 #Also, if the lowest number is less than the highest number, exit the loop
    while lowestNum not in a and lowestNum < highestNum:  # Increment if number not in Array
       lowestNum = lowestNum+1
    
    outerIndex = outerIndex + 1 #next pass through the array
    
if outerIndex == maxIndex: #Outer Loop finished?
   print "Array Sorted  ",a
   print "All done"



