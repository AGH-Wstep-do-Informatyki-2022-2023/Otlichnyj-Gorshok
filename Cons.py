import os
import yaml

ROOT_DIR = str(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
QUEST_FILE = yaml.load(open(f'{ROOT_DIR}/config/quests.yml', 'r'), Loader=yaml.FullLoader)
CONFIG_FILE = yaml.load(open(f'{ROOT_DIR}/config/config.yml', 'r'), Loader=yaml.FullLoader)
USER_FILE = yaml.load(open(f'{ROOT_DIR}/config/user.yml', 'r'), Loader=yaml.FullLoader)

GORSHOK_LIST_IMAGES_TEMP = (os.listdir(f'{ROOT_DIR}/images/._gorshok_images'))
# dict binds emotes and paths to their jpges
GORSHOK_BIND_IMAGES = dict([((GORSHOK_LIST_IMAGES_TEMP[index].split('.'))[0],
                             f'{ROOT_DIR}/images/._gorshok_images/{GORSHOK_LIST_IMAGES_TEMP[index]}')
                            for index in range(0, len(GORSHOK_LIST_IMAGES_TEMP))])
