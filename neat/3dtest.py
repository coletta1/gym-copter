#!/usr/bin/env python3
'''
Test script for using NEAT with gym-copter 3D environments

Copyright (C) 2020 Simon D. Levy

MIT License
'''

import neat
from neat_gym import read_file, eval_net

if __name__ == '__main__':

    # Load genome and configuration from pickled file
    genome, config = read_file()

    net = neat.nn.FeedForwardNetwork.create(genome, config)

    # Run the network
    print('%6.6f' % eval_net(net, config.env, render=True))
