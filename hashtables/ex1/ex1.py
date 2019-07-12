#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):

    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
# What if we store each weight in the input list as keys?
#  What would be a useful thing to store as the value for each key?
# If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for limit - weight.
# If it does, then we've found the two items whose weights sum up to the limit!

    for i in range(0, len(weights)):
        # store each weight in input as key, store list index as value
        hash_table_insert(ht, weights[i], i)

    for j in range(0, len(weights)):

        key_check = limit - weights[j]

        # to retreive, check if any key equals limit minus weight for key in ht
        index = hash_table_retrieve(ht, key_check)

        if index:
            return (index, j)

    return None


    # Brute Force approach
    # arr = []
    # for i in range(0, len(weights)):
    #     for j in range(0, len(weights)):
    #         if weights[i] + weights[j] == limit:
    #             arr.append([i, j])
    # return arr
print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
