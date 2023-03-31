def check_palidrom(sample):
    """
    Boolean function. Checks if a string is a palindrome.
    Arguments:
    String
    Return:
    False/True
    """
    sample=sample.lower().replace(" ","")
    return  sample==sample[::-1];
words=['Anna','sedes','123456123456','koza','zaraz','kajak','kuweta i żwirek','owocowo','A to kanapa pana Kota']
print("Słowa do sprawdzenia:",*words,sep="\n")
palidrom=[word for word in words if check_palidrom(word)]
print("\nPalindromami są:",*palidrom,sep="\n")