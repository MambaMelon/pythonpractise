# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 下午 09:07
# @Author  : melon

from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.layers.core import RepeatVector, TimeDistributedDense, Activation
from seq2seq.layers.decoders import LSTMDecoder, LSTMDecoder2, AttentionDecoder
import time
import numpy as np
import re 