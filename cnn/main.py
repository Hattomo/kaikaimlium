import sys

import numpy as np

sys.path.append('./dnn')
sys.path.append('./dataset')
import cnn_analysistool as catool
import convolution_layer as cl
import convolutional_neural_network as cnn
import csetting
import fully_connenct_layer as fc
import neural_network as nn
import pooling_layer as pl
import mnist
import logic_circuit as lc

(trainData, trainLabel) = lc.dset("cnn_exs", 1)
(testData, testLabel) = lc.dset("cnn_exs", 1)

conv = cl.Convolution_Layer(in_channel=1, out_channel=3, ksize=3, pad=1)
pool = pl.Pooling_Layer(pooling_size=[2, 2])
# cnnfc = fc.Fully_Connect_Layer([128 + 1, 10, 2])

conv_out = conv.forwardpropagation(trainData)
pool_out = conv.forwardpropagation(conv_out)
print(pool_out)