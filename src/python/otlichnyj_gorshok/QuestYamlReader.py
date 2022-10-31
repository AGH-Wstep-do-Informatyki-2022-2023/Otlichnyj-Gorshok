import Cons

for key, value in Cons.QUEST_FILE.items():
    if key == 'StoryLine':
        for k, v in dict(value).items():
            print(f"v type {type(v)}") #sprawdzić czy jest listą jak jest to wybór
            print(f"{k}: {v}")
