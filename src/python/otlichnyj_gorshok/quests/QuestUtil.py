import re
from time import sleep
from src.python.otlichnyj_gorshok.util import Cons


class QuestUtil:
    # removes the string '_index' from the sender's name in quests.yml
    # e.g. Gorshok_11 -> Gorshok
    @staticmethod
    def change_sender_name(sender):
        output_sender = ''
        for letter in sender:
            if letter != '_':
                output_sender += letter
            else:
                break
        return output_sender

    @staticmethod
    def message_analysis(message):
        clean_message = ''
        emote_message = ''
        for word in str(message).split(' '):
            game_var = re.search('<(.*)>', word)
            # only emotes has len == 2
            if game_var is None:
                clean_message += word + ' '
            else:
                # only emotes has len == 2
                if len(str(game_var.group(1))) > 2:
                    clean_message += Cons.CONFIG_FILE[str(game_var.group(1))] + ' '
                else:
                    emote_message += str(game_var.group(1))
        return clean_message, emote_message

    @staticmethod
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

    @staticmethod
    def quest_end():
        return True

    @staticmethod
    def get_rewards():
        return False
