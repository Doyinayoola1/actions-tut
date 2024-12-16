#This is a test to check minimum

#This checks lesser file
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    
    return max(a,b)
