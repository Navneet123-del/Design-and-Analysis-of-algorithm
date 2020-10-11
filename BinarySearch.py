import pymysql


connection = pymysql.connect(host="localhost", user="***", passwd="******", db="cse")
#use your mysql username and password in place of ****
mycursor = connection.cursor()
anurag=mycursor.execute("Select Roll_No from electives")
anurag = mycursor.fetchall()
anurag = [int(item[0]) for item in anurag]
anurag.sort()
print('Unsorted list is :',anurag)
x=int(len(anurag))
print('Sorted list is:',anurag)
print('Length of list is :',len(anurag))
a=int(input("Enter Roll_No to search:"))

def binary_search(anurag, x, a):
    start = 0
    end = x - 1
    while True:
        mid = int((start + end) / 2)
        if a == anurag[mid]:
            print("\nEntered Roll_Number %d is present at position: %d" % (a, mid))
            break
        elif a < anurag[mid]:
            end = mid - 1
        elif a > anurag[mid]:
            start = mid + 1
binary_search(anurag, x, a)
