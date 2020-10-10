def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    # Your code here
    result = []

    # adding all numbers to hash table
    for number in a:
        cache[number] = number
        # searhing for neg numbers
    for number in a:
        if number < 0:
            # if the value is cachce add to results
            if abs(number) in cache:
                result.append(abs(number))

    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
