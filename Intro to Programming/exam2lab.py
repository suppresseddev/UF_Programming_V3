def print_backwards(text, final = ""):
    if text == "":
        print(final, end="")
        return
    final += text[-1]
    print_backwards(text[:-1], final)
def format_names(names, i = 0, result = []):
    # print(f"Current Name: {names[i]}")
    if list(names[i]).__contains__(','):
        result.append(names[i])
    else:
        fn_ln = str(names[i]).split(' ')
        result.append(f"{fn_ln[1]}, {fn_ln[0]}")
    # print(f"Current Result: {result}")
    if i >= len(names)-1:
        # print(f"Final Result: {result}")
        return(result)
    else:
        return format_names(names, i+1, result)
def sum_a(k):
    total = 0
    for dic in k:
        for key, value in dic.items():
            if key == 'a':
                total += int(value)
    return(total)
def process_list(k):
    result = []
    for index, item in enumerate(k):
        if index % 2 == 0:
            result.append(str(item))
    for index, item in enumerate(k):
        if index % 2 != 0:
            result.append(item*10)
    return result