import json


def main():
    hero_list = []
    with open('json-fake-data.json') as json_file:
        data = json.load(json_file)
        for item in data:
            name = item['name']
            heroclass = item['class']
            race = item['race']

            hero = {
                'name': name,
                'class': heroclass,
                'race': race
            }
            hero_list.append(hero)
    print(hero_list)





if __name__ == "__main__":
    main()
