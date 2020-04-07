# with open('Labs\contact.csv', 'r') as file:
#     lines = file.read().split('\n')
#     print(lines)


# contacts = []

# for i in range(len(lines)):

#     for line in lines:
#         if i < 3:
#             contacts.append(dict(line))
#         if i > 3 and i < 5:
#             contacts.append(dict(line))
#         if i > 5 and i < 8:
#             contacts.append(dict(line))
# print(contacts)

# def read_contacts():
#     with open('Labs\contact.csv', 'r') as file:
#         lines = file.read().split('\n')
#     header = lines.pop(0).split(', ')
#     contacts = []
#     for line in lines:
#         data = line.split(', ')
#         item = {}
#         for index in range(len(data)):
#             item.update({header[index]: data[index]})
#         contacts.append(item)
#     return contacts

# print(read_contacts())
# name, fruit, color
# mathew, strawberry, yellow
# bob, mango, green
# laura, banana, orange


# import csv
# import collections
# def main():
#     with open('Labs\contact.csv') as f:
#         reader = csv.DictReader(f)
#         contact_list = [r for r in reader]
#         x = 0
#         dict_list = []
#         while x <= len(contact_list):
#             for i in contact_list:
#                 dict_list.append(dict(collections.OrderedDict(i)))
#             x += 1
#         return dict_list

# x = main()
# print(x[1])
