def intersection(arrays):
    """
    YOUR CODE HERE

    """
    # Your code here
    cache={

    }
    result =[]
    for result_list in arrays:
        result= result + result_list
        # enter numbers in dict
    list_volume = len(arrays)

    for numbers in result:
        if numbers in cache:
            cache[numbers] += 1
        else:
            cache[numbers] = 1

    result = [key for key, value in cache.items() if value == list_volume]#using a list coph
    return result



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
