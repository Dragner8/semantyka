import json

def search(target ,input,json):

    for x in json[target]:
        for x_name in x['name']:
            if (multiple_search(x_name.split(), input)):
                return True, x['id'] , x
    return False,0,0


def levenstain():

    pass

def multiple_search(x, input):

    counter = len(x);

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
                #result += Id
                print(Id+" "+result)
                print (Json["value"])

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
        recognize_command(x.split())



if __name__ == '__main__':
    main()