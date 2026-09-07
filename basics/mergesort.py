
def debug_print(debug_msg=None, **kwargs):

    if debug_msg:
        print(debug_msg)

    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


def mergesort(array):
    if len(array) <= 1:
        return array

    m = len(array) // 2

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)


def merge(left, right):
<<<<<<< HEAD
    debug_print(debug_msg="Merging...", left=left, right=right)

=======
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        merged += left
    else:
        merged += right

<<<<<<< HEAD
    debug_print(merged=merged)
=======
>>>>>>> upstream/master
    return merged


if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")
<<<<<<< HEAD

    input_list = input_str.split(",")
    debug_print(input_list=input_list)

=======
    input_list = input_str.split(",")
>>>>>>> upstream/master
    value_list = []
    for x in input_list:
        try:
            value_list.append(int(x))
        except ValueError as err:
            print("Invalid input.")
            quit(1)

<<<<<<< HEAD
    debug_print(value_list=value_list)

=======
>>>>>>> upstream/master
    sorted_list = mergesort(value_list)
    print(sorted_list)
