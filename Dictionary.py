while(True):
    d1={"String":"String is a collection of one or more words", "List":"List is mutable type data type", "Tuple":"tuple is immutable data type", "Set":"Set have only unique elements"}
    x = input("Enter Your Word: ")
    print(d1.get(x))