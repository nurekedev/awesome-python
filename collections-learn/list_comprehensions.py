a = 'ABC'

b_list = [first := ord(x) for x in a]

# print(first)

capacities = [1, 2, 3,]
juices = ['apple', 'orange', 'grape',]

to_sell = [(capacity, juice) for capacity in capacities for juice in juices]
for i in to_sell:
    print(i)

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols]
print(beyond_ascii)
