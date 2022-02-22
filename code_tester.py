set1 = {3, 4, 6, 2, 1}
set2 = {2, 7, 8, 10, 12}
list1 = [3, 4, 6, 2, 1]
list2 = [2, 1, 8, 10, 12]
print(len(set1 & set2))
print(len(set(list1) & set(list2)))
salary = 2363.56
hours = 160
if __name__ == "__main__":
    print(f'stawka godzinowa wynosi {salary / hours:}')
