import os
import sys

GAME_NAME = 'Otlichnyj-Gorshok'
SYSTEM_NAME_LINUX = 'Linux'
SYSTEM_NAME_MACOS = 'OS X'
SYSTEM_NAME_WINDOWS = 'Windows'


def getOperatingSystem():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]


def getGameDirectory():
    path = os.getcwd().split('\\')
    home_path = ''
    if getOperatingSystem() == SYSTEM_NAME_WINDOWS:
        for dir in path:
            home_path += f'{dir}/'
            if dir == GAME_NAME:
                break
    else:
        for dir in path[1:]:
            home_path += f'/{dir}'
            if dir == GAME_NAME:
                break
    return home_path


QUEST_FILE = f'{getGameDirectory()}/config/quests.yml'
CONFIG_FILE = f'{getGameDirectory()}/config/config.yml'
