my_list = 1,2,3,4,5,6,7,8,9

def even_number(num):
    if num % 2 == 0:
        return True
    else:
        return False

"""_s
    In [1]: my_list_of_int = ["Gig0/0", "Fa0/0", "Gig 0/1", "Gig0/2", "Loopback0", "Portchannel1"]

In [2]: my_gig = list(filter(lambda x: x.startswith("Gig"),  my_list_of_int))

In [3]: my_gig = list(filter(lambda x: x.startswith("Gig"),  my_list_of_int))

In [4]: my_gig
Out[4]: ['Gig0/0', 'Gig 0/1', 'Gig0/2']

In [5]: ummary_
    """
    
    