from src.python.otlichnyj_gorshok.quests.QuestUtil import QuestUtil
from src.python.otlichnyj_gorshok.util import Cons


class QuestYamlReader:

    def get_quest_dialog(self):
        questUtil = QuestUtil()
        questStorylineList = []
        for questID, valueQuestID in Cons.QUEST_FILE.items():
            if questID == Cons.USER_FILE['quest']:
                for keyQuest, valueQuest in dict(valueQuestID).items():
                    if keyQuest == 'StoryLine':
                        questStorylineList.append(
                            ("(" + questUtil.message_analysis(valueQuestID['IntroText'])[0] + ")", ''))
                        for sender, message in dict(valueQuest).items():
                            sender = questUtil.change_sender_name(sender)
                            if sender == 'Player':
                                sender = Cons.CONFIG_FILE['player_ingame_name']

                            if sender == Cons.CONFIG_FILE['gorshok_ingame_name']:
                                questStorylineList.append((sender + ": " + questUtil.message_analysis(message)[0],
                                                           Cons.GORSHOK_BIND_IMAGES[
                                                               questUtil.message_analysis(message)[1]]))
                            elif sender == '':
                                questStorylineList.append(
                                    ("(" + questUtil.message_analysis(message)[0] + ")", ''))

                            else:
                                questStorylineList.append(
                                    (sender + ": " + questUtil.message_analysis(message)[0], 'path'))
                        questStorylineList.append(
                            ("(" + questUtil.message_analysis(valueQuestID['CompletedText'])[0] + ")", ''))
                        questStorylineList.append((' ', ''))
        # List: [(sender_1, message_1, path_to_image_1), (...), ...]
        return questStorylineList
