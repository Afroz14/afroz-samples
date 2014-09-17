#How will you find a string a is a rotated string of some string b 

def check_if_rotated(s1,s2):
    return len(s1) == len(s2) and s1 in 2*s2
    
if(__name__ == "__main__"):
    s1 =  "AfrozAlam"
    s2 =  "AlamAfroz"
    if check_if_rotated(s1,s2):
        print("String is rotated")
    else:
        print("String is not rotated" )   
