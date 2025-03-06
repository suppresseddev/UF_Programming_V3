#Data Parsing
def parse_student(input):
    _id = ""
    name = ""
    birthdate = ""
    k = list(input)
    for i, t in enumerate(k):
        #Grab ID
        if i in range(0,8):
            _id += t
        elif i in range((len(k)-4), len(k)):
            birthdate += t
            if i == len(k)-3:
                birthdate += '/'
        else:
            name += t
    result = {
        'id' : int(_id),
        'name' : name,
        'birthdate' : birthdate
    }
    return result
#List Counting
def count_items(input):
    list_input = list(input)
    result = {}
    for i, k in enumerate(list_input):
        result[k] = list_input.count(k)
    return result
#List Fighters
def list_fighters(input):
    k = []
    for fighterdata in input:
        # print(f"Current fighter: {fighterdata}")
        k.append(fighterdata)
        for condition in input[fighterdata]:
            # print(f"Current Condition: {condition}")
            for matchup in input[fighterdata][condition]:
                # print(f"Current matchup: {matchup}")
                k.append(matchup)
    k_corrected = sorted(set(k))
    return  k_corrected