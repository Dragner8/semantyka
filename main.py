import json

def search(target ,input,json):
    sensivity=2
    for sen in range(sensivity+1):
        for x in json[target]:
            for x_name in x['name']:

                if (multiple_search(x_name.split(), input,sen)):
                    return True, x['id'] , x
    return False,0,0


def invoke_leven(x, input, counter, sensivity):
    for word in x:
        for i in input:
            if levenshtein(word, i) <= sensivity:
                counter -= 1
                x.remove(word)

def multiple_search(x, input,sensivity):
    print(sensivity)
    recognized = []
    counter = len(x);
    tmp=x.copy()
    print(x,tmp)
    for word in x:
        if word in input:
            counter -= 1
            tmp.remove(word)
            recognized.append(word)
            print(x,tmp)
    x=tmp
    print("CIAMCIARAMCIA",tmp)

    #leviatan

    for sen in range(1,sensivity+1):
        tmp=x.copy()
        for word in x:
            for i in input:
                    if levenshtein(word,i) <=sen:
                        counter -= 1
                        print(word)
                        tmp.remove(word)
                        recognized.append(i)
                        break
        x=tmp
    print("trutrutru",x)
    print("TEST" + str(counter))
    if counter == 0:
        print(tmp)
        for word in recognized:
            #input.remove(word)
            print(word)
        return True

    return False

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
                            result="set "+result+" "+Id+" "+value
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



def main():

    while(True):
        x = input('What do you want for me?(write "end" to break)')
        if x=="end":
            break
        print(recognize_command(x.split()))




if __name__ == '__main__':
    main()
