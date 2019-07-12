#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # build ht like in ex1 example
    for i in range(0, length):
        # add tickets to ht
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        # if source = none, starting point is route[0] and thats where you start, set equal to destination
        if tickets[i].source == 'NONE':
            start = tickets[i].destination
            # now you know your first destination, must be at 0th index of route
            route[0] = start

    for j in range(1, length):  # start at 1 because you already have 0 ('LAX' in this problem)
        # if tickets[i].destination == 'NONE':
        #     break
        # return destination(value) at my previous start(key) Lax->Sfo->Bhm etc..
        end = hash_table_retrieve(hashtable, start)
        # print(end)
        route[j] = end
        start = end

    return route


ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
print(reconstruct_trip(tickets, 10))
# The crux of this problem requires us to 'link' tickets together to reconstruct the entire trip. For example, if we have a ticket ('SJC', 'BOS') that has us flying from San Jose to Boston, then there exists another ticket where Boston is the starting location, ('BOS', 'JFK').
# We can hash each ticket such that the starting location is the key and the destination is the value. Then, when constructing the entire route, the ith location in the route can be found by checking the hash table for the i-1th location.
# print(reconstruct_trip([
#     {"PIT",  "ORD"},
#     {"XNA",  "CID"},
#     {"SFO",  "BHM"},
#     {"FLG",  "XNA"},
#     {"NONE",  "LAX"},
#     {"LAX",  "SFO"},
#     {"CID",  "SLC"},
#     {"ORD",  "NONE"},
#     {"SLC",  "PIT"},
#     {"BHM",  "FLG"}], 9))

# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
