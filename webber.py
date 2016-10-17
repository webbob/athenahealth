
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''

    inter = {}
    diff  = {}

    for k, v1 in d1.iteritems():
        try:
            inter[k] = f(v1, d2[k]) 
        except KeyError:
            diff[k] = v1

    for k, v2 in d2.iteritems():
        try:
            d1[k]
        except KeyError:
            diff[k] = v2

    return ( inter, diff )

	
