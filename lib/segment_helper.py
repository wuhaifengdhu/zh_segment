#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import print_function
import re
import io
from dict_helper import DictHelper
from nltk.stem.wordnet import WordNetLemmatizer
from subprocess import call
lemmatizer = WordNetLemmatizer()


class SegmentHelper(object):
    @staticmethod
    def segment_text(text, lemmatization=True):
        """Return a list of words that is the best segmentation of `text`."""
        # remove characters \ and .
        text = re.sub(r'\\|\.', '', text)
        # remove unicode characters
        text = text.decode('unicode_escape').encode('ascii', 'ignore')
        # split words
        word_list = re.split(r'[^a-zA-Z0-9-+]', text)
        return SegmentHelper.lemmatization(word_list) if lemmatization else word_list

    @staticmethod
    def lemmatization(word_list):
        print("Before lemmatization", word_list)
        new_list = []
        for word in word_list:
            word = word.strip()
            if len(word) > 0 and word != '*':
                new_list.append(lemmatizer.lemmatize(word).lower())
        print("After lemmatization", new_list)
        return new_list

    @staticmethod
    def generate_user_dict(excel_name, dict_output):
        """
        Read excel file and generate dict file
        :param excel_name:  excel file name, currently only support xls file
        :param dict_output:  dict output
        :return: None
        """
        # call(['java', '-jar', 'problems.jar', excel_name, dict_output])
        call(['java', '-jar', 'dic_generate.jar', excel_name, dict_output])

    @staticmethod
    def generate_probability_dict(file_content_list):
        # statistics single word and continue two words
        single_word_dict = {}
        two_word_dict = {}
        for file_content in file_content_list:
            for line in file_content.splitlines():
                word_list = SegmentHelper.segment_text(line)
                if len(word_list) == 1:
                    DictHelper.increase_dic_key(single_word_dict, word_list[0])
                else:
                    for i in range(len(word_list) - 1):
                        DictHelper.increase_dic_key(single_word_dict, word_list[i])
                        DictHelper.increase_dic_key(two_word_dict, "%s %s" % (word_list[i], word_list[i + 1]))
                    DictHelper.increase_dic_key(single_word_dict, word_list[-1])
        # compute two word probability
        prob_a_b_dict = {}
        for words, count in two_word_dict.items():
            word_a, word_b = words.split(' ')
            pro_a_b = two_word_dict[words] * 1.0 / single_word_dict[word_b];
            pro_b_a = two_word_dict[words] * 1.0 / single_word_dict[word_a];
            prob_a_b_dict[words] = max(pro_a_b, pro_b_a)
        return prob_a_b_dict

    @staticmethod
    def phase_segment(probability_dict, sentence, threshold):
        word_list = SegmentHelper.segment_text(sentence)
        if len(word_list) <= 1:
            return word_list
        word_list.append('')
        phrase_list = []
        phrase = ''
        for i in range(len(word_list) - 1):
            print (i)
            pair = '{0} {1}'.format(word_list[i], word_list[i + 1])
            phrase += word_list[i] if len(phrase) == 0 else ' ' + word_list[i]
            if pair not in probability_dict or probability_dict[pair] < threshold:
                phrase_list.append(phrase)
                phrase = ''
        if len(phrase) > 0:
            phrase_list.append(phrase)
        return phrase_list

    @staticmethod
    def parse_file(filename):
        "Read `filename` and parse tab-separated file of (word, count) pairs."
        with io.open(filename, encoding='iso-8859-1') as reader:
            lines = (line.split('\t') for line in reader)
            return dict((word.lower(), float(number)) for word, number in lines)


if __name__ == '__main__':
    # print (SegmentHelper.phase_segment({}, "I am wu haifeng", 0.3))
    print (SegmentHelper.generate_probability_dict(["wu haifeng is a good boy.\n wu haifeng is a good phd.\n"]))




