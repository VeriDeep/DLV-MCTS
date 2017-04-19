#!/usr/bin/env python

"""
Define paramters
author: Xiaowei Huang
"""

from network_configuration import *

from usual_configuration import * 


#######################################################
#
#  The following are parameters to indicate how to work 
#   with a problem
#
#######################################################

# which dataset to work with
dataset = "mnist"
#dataset = "gtsrb"
#dataset = "cifar10"
#dataset = "imageNet"

# the network is trained from scratch
#  or read from the saved files
whichMode = "read"
#whichMode = "train"

# which model to train
trainingModel = "autoencoder"
#trainingModel = "normal"

# work with a single image or a batch of images 
#dataProcessing = "single"
dataProcessing = "batch"
dataProcessingBatchNum = 1


#######################################################
#  get parameters from network_configuration
#######################################################

(featureDims,span,numSpan,NN,dataBasics,directory_model_string,directory_statistics_string,directory_pic_string,filterSize) = network_parameters(dataset)


#######################################################
#  specific parameters for datasets
#######################################################


(startIndexOfImage,startLayer, numOfFeatures,explorationRate,controlledSearch,MCTS_all_maximal_time, MCTS_level_maximal_time,MCTS_multi_samples) = usual_configuration(dataset)
    

#######################################################
#
#  show detailedInformation or not
#  FIXME: check to see if they are really needed/used
#
#######################################################

def nprint(str):
    return      
        