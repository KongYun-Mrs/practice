import yaml
import os
import time

dir_path = os.path.dirname(os.path.abspath(__file__))
yam_path = os.path.join(dir_path, 'user.yml')

with open(yam_path, 'r+')as fp:
    data = fp.read()
    print(yaml.load(data, Loader=yaml.FullLoader))
