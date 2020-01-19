def valid_list_exist(arg):
    """
    this method is checking if a list exists
    """
    if arg == None:
        return False
    return True

def valid_list_type(arg):
    """
    this method is checking if the bubble sorting is doing what it need to do.
    """
    for i in range(1, len(arg)):
        if type(arg[i - 1]) != type(arg[i]):
            return False
    return True

def valid_output(arg):
    """
    this method is checking if the output is exist.
    """
    if arg == None:
        return False
    return True



def valid_equal(lst1, lst2):
    """
    this method is checking if each element in the output list exist in the unsorted list.
    """
    if len(lst1) != len(lst2):
        return False
    for elem in lst1:
        if elem not in lst2:
            return False
    return True

def is_sorted(arg):
    """
    this method is checking if the output is sorted properly
    """
    f1, f2 = True, True
    for i in range(1, len(arg)):
        if arg[i - 1] > arg[i]:
            f1 = False
    if f1:
        return True
    for i in range(1, len(arg)):
        if arg[i - 1] < arg[i]:
            f2 = False
    if f2:
        return True

