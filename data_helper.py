# -*- coding:utf-8 -*-

from collections import  Counter
import tensorflow.contrib.keras as kr
import numpy as np
import codecs
import re
import jieba

def read_file(filename):
    re_han = re.compile(u"([\u4E00-\u9FD5a-zA-Z]+)")  # the method of cutting text by punctuation
    contents, labels = [], []
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                line = line.strip()
                assert len(line.split('\t')) == 2
                label, content = line.split('\t')
                blocks = re_han.split(content)
                word = []
                for block in blocks:
                    if re_han.match(block):
                        if len(word) >= 2:
                            word.append(word)
                contents.append(word)
            except:
                pass
    return labels, contents


def build_vocabulary(files, vocab_dir, vocab_size=8000):
    all_data = []
    for file in files:
        _, data_train = read_file(file)
        for content in data_train:
            all_data.extend(content)
    counter = Counter(all_data)
    count_paris =counter.most_common(vocab_size - 1)
    words, _ = list(zip(*count_paris))
    words = ['<PAD>'] + list(words)

    with codecs.open(vocab_dir, 'w', encoding='utf-8') as f:
        f.write('\n'.join(words) + '\n')







