# отгадать число из указанного диапазона

def binary_search(list:list, item:int):
    midl = list[len(list)//2]
    low = list[0]
    high = list[-1] + 1

    if item < low or item > high:
        return None

    while midl != item:
        if item < midl :
            high = midl
            midl = (low + high) //2
        else:
            low = midl
            midl = (low + high) //2
    return midl

my_list = list(range(1, 101))
my_item = 903

print(binary_search(my_list, my_item))