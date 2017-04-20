#!/usr/bin/env python

"""
Define paramters
author: Xiaowei Huang
"""

def usual_configuration(dataset):

        
    if dataset == "mnist": 

        # which image to start with or work with 
        # from the database
        startIndexOfImage = 5424
        
        # the layer to work with 
        # -1 is input layer
        startLayer = -1

        
        ## control by distance
        #controlledSearch = ("euclidean",0.3)
        controlledSearch = ("L1",0.02)
        #controlledSearch = ("Percentage",0.12)
        #controlledSearch = ("NumDiffs",30)
        
        # MCTS_level_maximal_time
        MCTS_level_maximal_time = 60
        MCTS_all_maximal_time = 300
        MCTS_multi_samples = 5
        
        # tunable parameter for MCTS
        explorationRate = 0.5
    
        return (startIndexOfImage,startLayer,explorationRate,controlledSearch,MCTS_all_maximal_time, MCTS_level_maximal_time,MCTS_multi_samples)
        
    elif dataset == "cifar10": 
    
        # which image to start with or work with 
        # from the database
        startIndexOfImage = 385
        
        # the start layer to work from 
        startLayer = -1
        
        ## control by distance
        #controlledSearch = ("euclidean",0.3)
        controlledSearch = ("L1",0.25)
        
        # MCTS_level_maximal_time
        MCTS_level_maximal_time = 300
        MCTS_all_maximal_time = 1800
        MCTS_multi_samples = 3
 
        explorationRate = 0.5

        return (startIndexOfImage,startLayer,explorationRate,controlledSearch,MCTS_all_maximal_time, MCTS_level_maximal_time,MCTS_multi_samples)
        
        
    elif dataset == "gtsrb": 

        # which image to start with or work with 
        # from the database
        startIndexOfImage = 4894
        
        # the layer to work on 
        startLayer = -1

        ## control by distance
        #controlledSearch = ("euclidean",0.3)
        controlledSearch = ("L1",0.15)
        #controlledSearch = ("Percentage",0.12)
        #controlledSearch = ("NumDiffs",30)
        
        # MCTS_level_maximal_time
        MCTS_level_maximal_time = 300
        MCTS_all_maximal_time = 1800
        MCTS_multi_samples = 3

        explorationRate = 0.5

        return (startIndexOfImage,startLayer,explorationRate,controlledSearch,MCTS_all_maximal_time, MCTS_level_maximal_time,MCTS_multi_samples)

    elif dataset == "imageNet": 
    
        # which image to start with or work with 
        # from the database
        startIndexOfImage = 1
        
        # the start layer to work from 
        startLayer = 0

        ## control by distance
        controlledSearch = ("euclidean",0.1)
        #controlledSearch = ("L1",0.05)
        
        # MCTS_level_maximal_time
        MCTS_level_maximal_time = 300
        MCTS_all_maximal_time = 1800
        MCTS_multi_samples = 3

        explorationRate = 0.5
    
        return (startIndexOfImage,startLayer,explorationRate,controlledSearch,MCTS_all_maximal_time, MCTS_level_maximal_time,MCTS_multi_samples)