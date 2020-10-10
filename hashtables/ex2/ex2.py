#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    air_route = [None] * length
    for index in range(len(tickets)):
        if tickets[index].source == 'NONE':
            air_route[0] = tickets[index].destination

        if tickets[index].source not in cache:
            cache[tickets[index].source] = tickets[index].destination
    for item in range(length):
        if air_route[item -1] is not None:
            air_route[item] = cache[air_route[item -1]]

    return air_route


