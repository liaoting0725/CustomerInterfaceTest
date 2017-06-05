# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
from tool import configParse


cur_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(cur_dir, 'info.conf')
print cur_dir
print config_path
conf = configParse.ConfParse(config_path)
ming = conf.get_int('1', 'age')
sex = conf.get_value('1', 'sex')
print ming
print sex

conf.set_value('1', 'sex', 'sex')

