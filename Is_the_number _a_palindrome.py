import collections

my_input = input("Введи число: ")
my_list = list(my_input)
 
def divide_list(list):
    lists_len = len(list) // 2

    list1 = []
    list2 = []

    for i in range(lists_len):
        list1.append(list[i])
    
    j = -1
    while j >= -lists_len:
        list2.append(list[j])
        j -= 1

    return list1, list2          

def compare_lists(list1, list2):
   if collections.Counter(list1) == collections.Counter(list2):
       return True
   else:
       return False

list1 = divide_list(my_input)[0]
list2 = divide_list(my_input)[1]

comparison = compare_lists(list1, list2)

if comparison == True:
    print(f"The number {my_input} is a palindrom")
else:
    print(f"The number {my_input} is not a palindrom")
