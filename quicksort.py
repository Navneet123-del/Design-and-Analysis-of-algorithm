import pymysql
import time

connection = pymysql.connect(host="localhost", user="root", passwd="Anurag@123", db="pythonDAA")
mycursor = connection.cursor()
list = mycursor.execute("select roll_no from rollno")
list = mycursor.fetchall()
list = [int(item[0]) for item in list]
print('Length of list is:', len(list))
print('Unsorted array is:',list)



def partition(list, low, high):
    i = (low - 1)  # index of smaller element
    pivot = list[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if list[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[high] = list[high], list[i + 1]
    return (i + 1)


def quickSort(list, low, high):
    if low < high:
        pi = partition(list, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(list, low, pi - 1)
        quickSort(list, pi + 1, high)


n = len(list)
quickSort(list, 0, n - 1)
print("Sorted array is:",list)

print(time.process_time(), "seconds")
