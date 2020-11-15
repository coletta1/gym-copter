#!/usr/bin/env python3
'''
Test script for NEAT CopterLanderV2

Copyright (C) 2020 Simon D. Levy

MIT License
'''

import visualize

from common import read_file, eval_genome

if __name__ == '__main__':

    genome, config = read_file()

    node_names = {-1:'x', -2:'dx', -3:'y', -4:'dy', -5:'phi', -6:'dphi', 0:'mr', 1:'ml'}
    visualize.draw_net(config, genome, True, node_names = node_names)
