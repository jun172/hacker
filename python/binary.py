def binary_search(data_list, target):
    low = 0
    high = len(data_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = data_list[mid]

        if guess == target:
            return mid
        
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return None

my_list = [1,3,5,7,9,11,13,15]
print(f"9のインデックスは: {binary_search(my_list, 9)}")
print(f"100の結果は: {binary_search(my_list, 100)}") 