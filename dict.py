def run(letters):
    keys = []
    values = []
    for key in letters.keys():
        keys.append(key)
    print letters.keys()
    for value in letters.values():
        values.append(value)
    print letters.values()
    return (keys,values)

#This is just for you to see what happens when the function is called
run({"a": 1, "b": 2, "c": 3, "d": 4})