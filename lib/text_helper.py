#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import re


class TextHelper(object):
    @staticmethod
    def get_pattern_in_context(context, pattern):
        return re.findall(pattern, context)

    @staticmethod
    def get_years_pattern(context):
        pattern_string = 'one[+ -]+year[s]?|two[+ -]+year[s]?|three[+ -]+year[s]?|four[+ -]+year[s]?|' \
                         'five[+ -]+year[s]?|six[+ -]+year[s]?|seven[+ -]+year[s]?|eight[+ -]+year[s]?|' \
                         'night[+ -]+year[s]?|ten[+ -]+year[s]?'
        match_result = TextHelper.get_pattern_in_context(context, '\d+\s*[+]?\s*years')
        match_result.extend(TextHelper.get_pattern_in_context(context, '\d+\s*-\s*\d+\s*years'))
        match_result.extend(TextHelper.get_pattern_in_context(context, '\d+\s*to\s*\d+\s*years'))
        match_result.extend(TextHelper.get_pattern_in_context(context, pattern_string))
        return match_result

    @staticmethod
    def get_dict_pattern(context, _dict, threshold=100):
        match_result = []
        for key, value in _dict.items():
            if value > threshold and key in context:
                match_result.append(key)
        return match_result

    @staticmethod
    def get_data_length(element):
        try:
            return len(element)
        except TypeError:
            return len(str(element))

    @staticmethod
    def to_string(element):
        try:
            return str(element)
        except UnicodeEncodeError:
            return element

    @staticmethod
    def find_text_between_tag(content, start_tag="<!--\n", end_tag="\n-->"):
        try:
            start_index = content.rindex(start_tag) + len(start_tag)
        except ValueError as TAG_NOT_FOUND_ERROR:
            print ("start tag: " + start_tag + " not found in :" + content)
            return
        content = content[start_index:]

        if len(end_tag) == 0:
            return content
        try:
            end_index = content.index(end_tag)
        except ValueError as TAG_NOT_FOUND_ERROR:
            print ("end tag: " + end_tag + " not found in :" + content)
            return
        return content[:end_index]

    @staticmethod
    def find_pattern_in_content(content, pattern_str):
        pattern = re.compile(pattern_str)
        return re.findall(pattern, content)


if __name__ == '__main__':
    print (TextHelper.get_years_pattern("one+ years one "))