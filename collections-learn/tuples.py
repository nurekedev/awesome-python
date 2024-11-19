travelers_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
values = (10, 20)

# Unpacking tuples
min, max = values
print(min, max)

quotient, remainder = divmod(*values)
print(quotient, remainder)

import os
_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
print(filename)


a, b, c, *rest = range(5)
print(rest)