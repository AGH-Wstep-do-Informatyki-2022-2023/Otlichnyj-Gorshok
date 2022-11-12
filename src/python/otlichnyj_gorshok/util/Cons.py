import os
import yaml

# returns the path to the root directory (distinguishes between initial installation paths)
# ROOT_DIR = <initial_installation_path>/Otlichnyj-Gorshok/
ROOT_DIR = str(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/').\
    replace('src/python/otlichnyj_gorshok/util', '')

# returns the path to the quests configuration file - quests.yml
QUEST_FILE = yaml.load(open(f'{ROOT_DIR}/config/quests.yml', 'r'), Loader=yaml.FullLoader)

# returns the path to the configuration file - config.yml
CONFIG_FILE = yaml.load(open(f'{ROOT_DIR}/config/config.yml', 'r'), Loader=yaml.FullLoader)

# returns the path to the user configuration file - user.yml
USER_FILE = yaml.load(open(f'{ROOT_DIR}/config/user.yml', 'r'), Loader=yaml.FullLoader)


# creates a string list of all images in a directory Otlichnyj-Gorshok/images/._gorshok_images
GORSHOK_LIST_IMAGES_TEMP = (os.listdir(f'{ROOT_DIR}/images/._gorshok_images'))

# dict binds emotes and paths to their jpges
# each image in Otlichnyj-Gorshok/images/._gorshok_images is described as <emote>.jpg/jpeg
GORSHOK_BIND_IMAGES = dict([((GORSHOK_LIST_IMAGES_TEMP[index].split('.'))[0],
                             f'{ROOT_DIR}/images/._gorshok_images/{GORSHOK_LIST_IMAGES_TEMP[index]}')
                            for index in range(0, len(GORSHOK_LIST_IMAGES_TEMP))])