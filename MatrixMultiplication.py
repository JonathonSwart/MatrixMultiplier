#Jonathon Swart
#This program will determine the product of 2 matrices
#May 17, 2020

#Open Matrix file
filename = "MatrixAandB.txt"
inFile = open(filename, "r")

#Creates list for each matrix
def Matrix():
    #Read line with borders of the matrix
    border = inFile.readline()
    #seperate the border into its own variables
    height, width = border.split(" ")

    #Main array
    matrixlist = []
    for x in range(0,int(height)):
        line = inFile.readline().rstrip()
        #mini list to be appended to main array
        fakelist = []
        for y in range(0,int(width)):
            #append each individual number to its proper list
            position = line.find(" ")
            if position == -1:   #checks there is only one number left in the line
                num = line
            else:
                num = line[0:position]
                line = line.lstrip(num)
                line = line.lstrip(" ")
            fakelist.append(int(num))
        #Append the little lists to the main array
        matrixlist.append(fakelist)
        
    return matrixlist

#Call function
m1 = Matrix()
m2 = Matrix()
m3 = []

#MULTIPLYING THE MATRICES
for x in range(len(m1)):
    fakem3 = []  #mini list to append to array
    for y in range(len(m2[0])):
        total = 0
        for z in range(len(m1[0])):
           num = m1[x][z]*m2[z][y]
           total = total + num  
        fakem3.append(total)
    m3.append(fakem3)  #final matrix product

#Print first matrix
for i in range(len(m1)):
    print ("| ".ljust(3),end="")
    for j in range(len(m1[0])):
        print (str(m1[i][j]).ljust(3),end=" ")
    print ("|")
    
#Show that we are multiplying matrices
print ()
print ("X".center(20," "))
print ()

#Print second matrix 
for i in range(len(m2)):
    print ("| ".ljust(3),end="")
    for j in range(len(m2[0])):
        print (str(m2[i][j]).ljust(3),end=" ")
    print ("|")
    
#Print equals sign
print ()
print ("=".center(20," "))
print ()

#Print the third matrix
for i in range(len(m3)):
    print ("| ".ljust(3),end="")
    for j in range(len(m3[0])):
        print (str(m3[i][j]).ljust(3),end=" ")
    print ("|")
