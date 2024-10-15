def print_str(data_str):
    new_str = "["
    for i in data_str:
        if i != " ":
            new_str += i
        else:
            new_str += "@"
    return new_str+"]"
data_str = "光头强 熊大 熊二 积极国王"
new_str = print_str(data_str)
print(new_str)
