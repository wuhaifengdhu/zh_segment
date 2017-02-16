Python Word Segmentation
========================

`zh_segment`_ is an Apache2 licensed module for English word
segmentation, written in pure-Python, and based on a trillion-word corpus.

Based on code from the chapter "`Natural Language Corpus Data`_" by Peter
Norvig from the book "`Beautiful Data`_" (Segaran and Hammerbacher, 2009).

Data files are derived from the `Google Web Trillion Word Corpus`_, as
described by Thorsten Brants and Alex Franz, and `distributed`_ by the
Linguistic Data Consortium. This module contains only a subset of that
data. The unigram data includes only the most common 333,000 words. Similarly,
bigram data includes only the most common 250,000 phrases. Every word and
phrase is lowercased with punctuation removed.

.. _`zh_segment`: https://github.com/wuhaifengdhu/zh_segment/tree/master/docs
.. _`Natural Language Corpus Data`: http://norvig.com/ngrams/
.. _`Beautiful Data`: http://oreilly.com/catalog/9780596157111/
.. _`Google Web Trillion Word Corpus`: http://googleresearch.blogspot.com/2006/08/all-our-n-gram-are-belong-to-you.html
.. _`distributed`: https://catalog.ldc.upenn.edu/LDC2006T13

Features
--------

- Pure-Python
- Fully documented
- 100% Test Coverage
- Includes unigram and bigram data
- Command line interface for batch processing
- Easy to hack (e.g. different scoring, new data, different language)
- Developed on Python 2.7
- Tested on CPython 2.6, 2.7, 3.2, 3.3, 3.4 and PyPy 2.5+, PyPy3 2.4+

.. image:: https://github.com/wuhaifengdhu/zh_segment/blob/master/docs/_static/zh_segment.png?raw=true
    :target: https://github.com/wuhaifengdhu/zh_segment

Quickstart
----------

Installing zh_segment is simple with
`pip <http://www.pip-installer.org/>`_::

    $ pip install zh_segment

You can access documentation in the interpreter with Python's built-in help
function::

    >>> import zh_segment
    >>> help(zh_segment)

Tutorial
--------

In your own Python programs, you'll mostly want to use `segment` to divide a
phrase into a list of its parts::

    >>> from zh_segment import segment
    >>> segment('1077501; 1296599; 5000; 5000; 4975; 36 months; 10.64%; 162.87; B; B2;;10+ years;RENT')
    ['1077501', '1296599', '5000', '5000', '4975', '36', 'months', '10.64%', '162.87', 'B', 'B', '2', '10+', 'years', 'RENT']

zh_segment also provides a command-line interface for batch processing. This
interface accepts two arguments: in-file and out-file. Lines from in-file are
iteratively segmented, joined by a space, and written to out-file. Input and
output default to stdin and stdout respectively. ::

    $ echo thisisatest | python -m zh_segment
    this is a test

The maximum segmented word length is 24 characters. Neither the unigram nor
bigram data contain words exceeding that length. The corpus also excludes
punctuation and all letters have been lowercased. Before segmenting text,
`clean` is called to transform the input to a canonical form::

    >>> from zh_segment import clean
    >>> clean('She said, "Python rocks!"')
    'shesaidpythonrocks'
    >>> segment('She said, "Python rocks!"')
    ['she', 'said', 'python', 'rocks']

Sometimes its interesting to explore the unigram and bigram counts
themselves. These are stored in Python dictionaries mapping word to count. ::

    >>> import zh_segment as ws
    >>> ws.load()
    >>> ws.UNIGRAMS['the']
    23135851162.0
    >>> ws.UNIGRAMS['gray']
    21424658.0
    >>> ws.UNIGRAMS['grey']
    18276942.0

Above we see that the spelling `gray` is more common than the spelling `grey`.

Bigrams are joined by a space::

    >>> import heapq
    >>> from pprint import pprint
    >>> from operator import itemgetter
    >>> pprint(heapq.nlargest(10, ws.BIGRAMS.items(), itemgetter(1)))
    [('of the', 2766332391.0),
     ('in the', 1628795324.0),
     ('to the', 1139248999.0),
     ('on the', 800328815.0),
     ('for the', 692874802.0),
     ('and the', 629726893.0),
     ('to be', 505148997.0),
     ('is a', 476718990.0),
     ('with the', 461331348.0),
     ('from the', 428303219.0)]

Some bigrams begin with `<s>`. This is to indicate the start of a bigram::

    >>> ws.BIGRAMS['<s> where']
    15419048.0
    >>> ws.BIGRAMS['<s> what']
    11779290.0

The unigrams and bigrams data is stored in the `zh_segment_data` directory in
the `unigrams.txt` and `bigrams.txt` files respectively.

Reference and Indices
---------------------

* `zh_segment Documentation`_
* `zh_segment at PyPI`_
* `zh_segment at Github`_
* `zh_segment Issue Tracker`_

.. _`zh_segment Documentation`: https://github.com/wuhaifengdhu/zh_segment/tree/master/docs/docs
.. _`zh_segment at PyPI`: https://pypi.python.org/pypi/zh_segment
.. _`zh_segment at Github`: https://github.com/wuhaifengdhu/zh_segment
.. _`zh_segment Issue Tracker`: https://github.com/wuhaifengdhu/zh_segment/issues

zh_segment License
-------------------

Copyright 2017 Z&H

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
