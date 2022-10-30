import yaml
import Cons

stream = open(Cons.QUEST_FILE, 'r')
dictionary = yaml.load(stream, Loader=yaml.FullLoader)
for key, value in dictionary.items():
    if key == 'StoryLine':
        for k, v in dict(value).items():
            print(f"v type {type(v)}") #sprawdzić czy jest listą jak jest to wybór
            print(f"{k}: {v}")
