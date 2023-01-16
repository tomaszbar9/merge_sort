def recursive_merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        div_point = len(my_list) // 2
        new1, new2 = my_list[:div_point], my_list[div_point:]
        new1, new2 = recursive_merge_sort(new1), recursive_merge_sort(new2)
        new = []
        while new1 and new2:
            if new1[0] < new2[0]:
                new.append(new1.pop(0))
            else:
                new.append(new2.pop(0))
        new += new1 or new2
        return new

