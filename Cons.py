import os
import yaml

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
QUEST_FILE = yaml.load(open(f'{ROOT_DIR}/config/quests.yml', 'r'), Loader=yaml.FullLoader)
CONFIG_FILE = yaml.load(open(f'{ROOT_DIR}/config/config.yml', 'r'), Loader=yaml.FullLoader)

