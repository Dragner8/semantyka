import json

def search(target ,input,json):

    for x in json[target]:
        for x_name in x['name']:
            if x_name in input:
                return True, x['id'] , x
    return False,0,0

def main():

    path = 'D:/Semantyka'

    with open('dom.json', "r") as f:
        data = json.load(f)

    input = ['lazienka', 'oswieltlenie gorne', 'wlacz']

    result = ''

    placeFound, Id, Json = search('places', input, data)
    if placeFound:
        result += Id
        deviceFound, Id ,Json = search('devices', input, Json)
        if deviceFound:
            result += str(Id)
            actionFound, Id ,Json = search('actions', input, Json)
            if actionFound:
                result += Id
                print(result)
            else:
                print("error unknown action")
        else:
            print("error unknown device")
    else:
        print("error unknown place")

    pass

if __name__ == '__main__':
    main()