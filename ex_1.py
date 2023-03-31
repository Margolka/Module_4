words=['Anna','sedes','123456123456','koza','zaraz','kajak','kuweta i żwirek','owocowo','A to kanapa pana Kota',]
def check_palidrom(sample):
    """
    Boolean function. Checks if a string is a palindrome.
    Arguments:
    String
    Return:
    False/True
    """
    sample=sample.lower().replace(" ","")
    for i in range(len(sample)-1):
        if sample[i]!=sample[-(i+1)]:
            return False
    return True;
print("Słowa do sprawdzenia:",*words,sep="\n")
palidrom=[word for word in words if check_palidrom(word)==True]
print("\nPalindromami są:",*palidrom,sep="\n")