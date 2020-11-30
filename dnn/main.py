import sys

import numpy as np

sys.path.append("./dataset")
sys.path.append("./shared")
import activationfunction as af
import analysistool as atool
import neural_network as nn
import dataset

datasize = 4
batch = 4
logic = "and"
# set data
trainData, trainLabel = dataset.logic(logic, datasize, batch)
testData, testLabel = dataset.logictest(logic, 10)
# ニューラルネットワークの生成
structure = [2 + 1, 5, 2]
myNN = nn.Neural_Network(structure)
# # 学習
epoch = 1
for i in range(epoch):
    myNN.train(trainData, trainLabel)
    myNN.test(testData, testLabel)

atool.draw(myNN.cost)