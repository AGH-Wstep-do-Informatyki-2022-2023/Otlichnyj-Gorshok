import Cons


def editSenderName(sender):
    outputsender = ''
    for letter in sender:
        if letter != '_':
            outputsender += letter
        else:
            break
    return outputsender


for questID, valueQuestID in Cons.QUEST_FILE.items():
    if questID == Cons.USER_FILE['quest']:
        for keyQuest, valueQuest in dict(valueQuestID).items():
            if keyQuest == 'StoryLine':
                for sender, message in dict(valueQuest).items():
                    sender = editSenderName(sender)
                    if type(message) is list:
                        for index in range(0, len(message)):
                            print(f"{index+1}) {message[index]}")
                        choice = int(input("Wprowadź opcję wyboru: "))
                        print(f"{sender}: {message[choice]}")
                    else:
                        print(f"{sender}: {message}")

