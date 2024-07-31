#  вернуть позицию загаданного числа из отсортированного списка
#  если такого числа в списке нет, вернуть None

def binary_search(list:list, item:int):
    low_index = 0
    high_index = len(list) - 1

    while low_index <= high_index:
       mid_index = (low_index + high_index) // 2
       if list[mid_index] == item:
           return mid_index
       if list[mid_index] > item:
           high_index = mid_index - 1
       else:
           low_index = mid_index + 1 
    return None
           


#my_list = list(range(1, 101))
my_list = [3, 20, 44, 600, 786, 862, 90000]
my_item = 90000

print(binary_search(my_list, my_item))

