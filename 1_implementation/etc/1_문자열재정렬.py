input_data = input()
alphabet_lst = []
num_lst = []

for char in input_data:
    if char.isalpha():
        alphabet_lst.append(char)
    else:
        num_lst.append(int(char))

if alphabet_lst:
    alphabet_lst.sort()
    alphabet_lst = ''.join(alphabet_lst)
else:
    alphabet_lst = ''

if num_lst:
    total = str(sum(num_lst))
else:
    total = ''

result = alphabet_lst + total

print(result)