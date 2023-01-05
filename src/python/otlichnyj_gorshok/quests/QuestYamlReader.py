from src.python.otlichnyj_gorshok.quests.QuestUtil import QuestUtil
from src.python.otlichnyj_gorshok.util import Cons

util = QuestUtil()

def get_quest():
    questStoryLineList = []
    for questID, valueQuestID in Cons.QUEST_FILE.items():
        if questID == Cons.USER_FILE['quest']:
            for keyQuest, valueQuest in dict(valueQuestID).items():
                if keyQuest == 'StoryLine':
                    questStoryLineList.append(valueQuestID['IntroText'])
                    for sender, message in dict(valueQuest).items():
                        sender = util.change_sender_name(sender)
                        if type(message) is list:
                            for index in range(0, len(message)):
                                print(f"{index}) {message[index]}")
                            choice = int(input("Choose your option: "))
                            print(f"{sender}: {message[choice]}")
                        else:
                            print(f"{sender}: {util.sender_message_analysis(message)[0]}")
                            if sender == Cons.CONFIG_FILE['gorshok_ingame_name']:
                                print(f'{sender} emote: {util.sender_message_analysis(message)[1]}')
                                print(f'{sender} emote path: '
                                      f'{Cons.GORSHOK_BIND_IMAGES[util.sender_message_analysis(message)[1]]}')
                            else:
                                pass
                    print(valueQuestID['CompletedText'])
