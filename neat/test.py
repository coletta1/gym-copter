#!/usr/bin/env python3
'''
Test script for NEAT CopterLanderV2

Copyright (C) 2020 Simon D. Levy

MIT License
'''

import pickle
import argparse

from common import eval_genome

if __name__ == '__main__':

    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', metavar='FILENAME', help='input file')
    args = parser.parse_args()

     # Load genome and configuration from pickled file
    genome, config = pickle.load(open(args.filename, 'rb'))

    # Training uses multiple repetitions, testing only one
    config.reps = 1 
    print('%6.6f' % eval_genome(genome, config, True))
