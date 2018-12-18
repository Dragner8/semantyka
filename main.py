import json

def search(target ,input,json):

    for x in json[target]:
        for x_name in x['name']:
            if (multiple_search(x_name.split(), input)):
                return True, x['id'] , x
    return False,0,0




def multiple_search(x, input):

    counter = len(x);
    tmp=[]
    for word in x:
        if word in input:
            counter -= 1

    if counter == 0:
        for word in x:
            input.remove(word)
        return True

    return False

def recognize_command(input):
    with open('dom.json', "r") as f:
        data = json.load(f)

    result = ''

    placeFound, Id, Json = search('places', input, data)
    if placeFound:
        result += Id
        deviceFound, Id, Json = search('devices', input, Json)
        if deviceFound:
            result += str(Id)
            actionFound, Id, Json = search('actions', input, Json)
            if actionFound:

                if(Json["value"]):

                    for value in Json["value"]:
                        if value in input:
                            result=Id+" "+result+" "+value
                            return result
                    print("error set value is unavailable")
                    return None
                else:
                    result=Id+" "+result
                    return result


            else:
                print("error unknown action")
                return None
        else:
            print("error unknown device")
            return None
    else:
        print("error unknown place")
        return None

    return result


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]
def main():
    a = "wlacz"
    b = "wylacz"

    print(levenshtein(a, b))


    while(True):
        x = input('What do you want for me?(write "end" to break)')
        if x=="end":
            break
        print(recognize_command(x.split()))




if __name__ == '__main__':
    main()