# !/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser


class ConfParse(object):
    """该类用于解析config/ini文件"""
    def __init__(self, os_path):
        self.os_path = os_path
        self.parse = ConfigParser.ConfigParser()
        self.parse.read(os_path)

    def has_section(self, section):
        return self.parse.has_section(section)

    def has_option(self, section, option):
        return self.parse.has_option(section, option)

    def get_sections(self):
        return self.parse.sections()

    def get_items(self, section):
        return self.parse.items(section)

    def get_int(self, section, option):
        """获取int值"""
        return self.parse.getint(section, option)

    def get_float(self, section, option):
        """获取float值"""
        return self.parse.getfloat(section, option)

    def get_boolen(self, section, option):
        """获取boolen值"""
        return self.parse.getboolean(section, option)

    def get_value(self, section, option):
        return self.parse.get(section, option)

    def set_value(self, section, option, value):
        """update option值"""
        self.parse.set(section, option, value)
        fp = open(self.os_path, 'w')
        self.parse.write(fp)

    def add_section(self, section):
        self.parse.add_section(section)

    def remove_section(self, section):
        self.parse.remove_section(section)

    def remove_option(self, section, option):
        self.parse.remove_option(section, option)
