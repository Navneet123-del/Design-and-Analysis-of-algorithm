import pymysql

connection = pymysql.connect(host="localhost", user="root", passwd="Anurag@123", db="pythonDAA")
mycursor = connection.cursor()
val = mycursor.execute("select val from knapsack")
val = mycursor.fetchall()
val = [int(item[0]) for item in val]
weight = mycursor.execute("select weight from knapsack")
weight = mycursor.fetchall()
weight = [int(item[0]) for item in weight]

print(val,weight)


def fractional_knapsack(value, weight, capacity):

    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v / w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
    print(index)

    max_value = 0
    fractions = [0] * len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break

    return max_value, fractions


n =len(weight)       # int(input('Enter number of items: '))
value = val              #input('Enter the values of the {} item(s) : '
                       #.format(n)).split()
value = [int(v) for v in value]
weight =weight          #input('Enter the p weights of the {} item(s) in order: '
                      #.format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input('Enter maximum weight: '))

max_value, fractions = fractional_knapsack(value, weight, capacity)
print('The maximum value of items that can be carried:', max_value)
print('The fractions in which the items should be taken:', fractions)
