import pymysql
import time

connection = pymysql.connect(host="localhost", user="root", passwd="*****", db="pythonDAA")
mycursor = connection.cursor()
anurag = mycursor.execute("select roll_no from rollno")
anurag = mycursor.fetchall()
anurag = [int(item[0]) for item in anurag]
print('Length of list is:', len(anurag))

def mergeSort(anurag):
    if len(anurag) > 1:
        mid = len(anurag) // 2
        L = anurag[:mid]
        R = anurag[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                anurag[k] = L[i]
                i += 1
            else:
                anurag[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            anurag[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            anurag[k] = R[j]
            j += 1
            k += 1

print("UnSortest list is:",anurag,end="\n")
mergeSort(anurag)
print("Sortest list is:",anurag,end="\n")


print (time.process_time(), "seconds")






