from src.python.otlichnyj_gorshok.util import Cons
from src.python.otlichnyj_gorshok.util.Util import Util

util = Util()

for questID, valueQuestID in Cons.QUEST_FILE.items():
    if questID == Cons.USER_FILE['quest']:
        for keyQuest, valueQuest in dict(valueQuestID).items():
            if keyQuest == 'StoryLine':
                print(valueQuestID['ShortDescription'])
                print(valueQuestID['IntroText'])
                for sender, message in dict(valueQuest).items():
                    sender = util.change_sender_name(sender)
                    # only player has choice
                    if type(message) is list:
                        for index in range(0, len(message)):
                            print(f"{index}) {message[index]}")
                        util.time_interval_for_reading(message)
                        choice = int(input("Choose your option: "))
                        print(f"{sender}: {message[choice]}")
                    else:
                        print(f"{sender}: {util.sender_message_analysis(message)[0]}")
                        util.time_interval_for_reading(message)
                        if sender == Cons.CONFIG_FILE['gorshok_ingame_name']:
                            print(f'{sender} emote: {util.sender_message_analysis(message)[1]}')
                            print(f'{sender} emote path: '
                                  f'{Cons.GORSHOK_BIND_IMAGES[util.sender_message_analysis(message)[1]]}')
                        else:
                            pass
                print(valueQuestID['CompletedText'])
