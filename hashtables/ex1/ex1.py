def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
#if the length is les the 2
    # if length < 2: first pass
    #     return None
    # #adding to cache
    # for item in range(length):
    #     cache[weights[item]] = item
    # for items in range(length):
    #     result = limit - weights[items]
    #     if result in cache:
    #         two = items
    #         one = cache[result]
    #         result= [one, two]
    #         result.sort(reverse=True)
    #
    #
    #         return result[0], result[1]

    cache = {}
    if length < 2:# if lenght is less then 2
        return None
    for item in range(length):
        if limit - weights[item] in cache:
            return [item, cache[limit - weights[item]]]
        else:
            cache[weights[item]] = item#Same speed much less code
