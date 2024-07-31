def my_sorting(list: list):
    
    for i in range(len(list) - 1):
        if list[i] < list[i + 1]:
            a = list[i]
            list[i] = list[i + 1]
            list[i + 1] = a 

            while list[i] > list[i - 1] and i > 0:
                a = list[i - 1]
                list[i - 1] = list[i]
                list[i] = a
                i -= 1

    print(f"Сортировка чисел по убыванию: {list}")       






def sorting_book(list:list):

    sorted_list = []
    pass



my_list = [-100, 1, 10, 7, 14, 2, 12, -5, 1.2]
my_sorting(my_list)