zh_segment API Reference
=========================

.. py:function:: clean(text)
   :module: zh_segment

    Return `text` lower-cased with non-alphanumeric characters removed.

.. py:function:: divide(text, limit=24)
   :module: zh_segment

    Yield (prefix, suffix) pairs from `text` with len(prefix) not
    exceeding `limit`.

.. py:function:: load()
   :module: zh_segment

    Load unigram and bigram counts from disk.

.. py:function:: score(word, prev=None)
   :module: zh_segment

    Score a `word` in the context of the previous word, `prev`.

.. py:function:: isegment(text)
   :module: zh_segment

    Return iterator of words that is the best segmenation of `text`.

.. py:function:: segment(text)
   :module: zh_segment

    Return a list of words that is the best segmenation of `text`.

.. py:data:: UNIGRAMS
   :module: zh_segment

    Mapping of (unigram, count) pairs.
    Loaded from the file 'zh_segment_data/unigrams.txt'.

.. py:data:: BIGRAMS
   :module: zh_segment

    Mapping of (bigram, count) pairs.
    Bigram keys are joined by a space.
    Loaded from the file 'zh_segment_data/bigrams.txt'.

.. py:data:: TOTAL
   :module: zh_segment

    Total number of unigrams in the corpus.
    Need not match `sum(UNIGRAMS.values())`.
    Defaults to 1,024,908,267,229.
