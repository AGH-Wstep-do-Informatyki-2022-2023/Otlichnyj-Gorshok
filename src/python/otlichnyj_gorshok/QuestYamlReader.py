from time import sleep

import Cons
import re


# this function removes the string '_index' from the sender's name in quests.yml
# e.g. Gorshok_11 -> Gorshok
def change_sender_name(sender):
    outputsender = ''
    for letter in sender:
        if letter != '_':
            outputsender += letter
        else:
            break
    return outputsender


def sender_message_analysis(message):
    cleanMessage = ''
    emoteMessage = ''
    for word in str(message).split(' '):
        emote = re.search('<(.*)>', word)
        if emote is None:
            cleanMessage += word + ' '
        else:
            emoteMessage += str(emote.group(1))
    return cleanMessage, emoteMessage


def time_interval_for_reading(message):
    word_per_minute = 300
    second_per_word = 60 / word_per_minute
    words = 0
    if type(message) is list:
        for choice in message:
            words += len(str(choice).split(' '))
    else:
        words = len(str(message).split(' '))
    return sleep(second_per_word * words)


def quest_end():
    return True


def get_rewards():
    return False


for questID, valueQuestID in Cons.QUEST_FILE.items():
    if questID == Cons.USER_FILE['quest']:
        for keyQuest, valueQuest in dict(valueQuestID).items():
            if keyQuest == 'StoryLine':
                print(valueQuestID['ShortDescription'])
                print(valueQuestID['IntroText'])
                for sender, message in dict(valueQuest).items():
                    sender = change_sender_name(sender)
                    # only player has choice
                    if type(message) is list:
                        for index in range(0, len(message)):
                            print(f"{index}) {message[index]}")
                        time_interval_for_reading(message)
                        choice = int(input("Choose your option: "))
                        print(f"{sender}: {message[choice]}")
                    else:
                        print(f"{sender}: {sender_message_analysis(message)[0]}")
                        time_interval_for_reading(message)
                        if sender == Cons.CONFIG_FILE['gorshok_ingame_name']:
                            print(f'{sender} emote: {sender_message_analysis(message)[1]}')
                            print(f'{sender} emote path: '
                                  f'{Cons.GORSHOK_BIND_IMAGES[sender_message_analysis(message)[1]]}')
                        else:
                            pass
                print(valueQuestID['CompletedText'])
