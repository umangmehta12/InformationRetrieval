#!env python
import sys
import os

import argparse

from collections import defaultdict
from decimal import *
import math

DAMPING_FACTOR = 0.85
outlinks = defaultdict(set)
inlinks = defaultdict(set)
all_pages = set()
sink = set()
source = set()
page_rank = dict()
new_page_rank = dict()
perplexity = list()

def get_parser():
    parser = argparse.ArgumentParser(
    description='calculate the pageRanks of given pages'
    )
    parser.add_argument(
    '-i',
    '--input-file',
    metavar='file',
    required=True,
    help='containing real web graph'
    )
    return parser

def createlinks(node, pages):
    if not pages:
        inlinks[node]
    for page in pages:
        inlinks[node].add(page)
        outlinks[page].add(node)
    if not outlinks.has_key(node):
            outlinks[node]

def setup_links(line):
    pages = line.rstrip().split(" ")
    node = pages[0]
    all_pages.add(node)
    if len(pages) == 1:
#            print "No inlinks for: ", pages
        source.add(pages[0])
#    sorted_inlinks[node].add(len(pages)-1)
    createlinks(node, pages[1:])

def process_file(input_file):
    with open(input_file, "r") as file:
        for line in file.read().splitlines():
            yield line

def get_sink(outlinks):
    for key, value in outlinks.iteritems():
            if value == set([]):
                sink.add(key)

def initialize_pagerank():
    for page in all_pages:
        page_rank[page] = 1.0/len(all_pages)

def calculate_perplexity():
    entropy = 0.0
    for page in page_rank.keys():
        entropy += page_rank[page] * math.log((1/page_rank[page]), 2)
#    entropy = -entropy
    return 2**entropy

def isconverged(counter):
    perplexity_value = calculate_perplexity()
    print "Counter ", counter+1,"Perplextiy Value : " ,perplexity_value
    print "Value : ", perplexity_value
    perplexity.append(perplexity_value)
    print len(perplexity)
    if len(perplexity) > 4:
        if (int(perplexity[counter]) == int(perplexity[counter - 1]) == int(perplexity[counter - 2]) == int(perplexity[counter - 3])):
            print counter + 1," ",calculate_perplexity(),"\n"
            return False
        else:
            return True
    else:
        return True

def perform_calculations():
    counter = 0
    temp = (1.0 - DAMPING_FACTOR)/len(all_pages)
    while isconverged(counter):
#    while counter<=1:
        sink_page_rank = 0
        for sink_page in sink:
            sink_page_rank += page_rank[sink_page]
        for page in all_pages:
            temp1 = DAMPING_FACTOR * sink_page_rank/len(all_pages)
            new_page_rank[page] = temp + temp1
            if inlinks.get(page) is not None:
                for outlink_page in inlinks.get(page):
                    new_page_rank[page] += DAMPING_FACTOR * page_rank[outlink_page]/len(outlinks.get(outlink_page))
        for pages in all_pages:
            page_rank[pages] = new_page_rank[pages]
        counter +=1

def main():
    parser = get_parser()
    args = parser.parse_args()
    if os.path.getsize(args.input_file) > 0:
#        lines = list(process_file(args.input_file))
        for line in list(process_file(args.input_file)):
            setup_links(line)
    else:
        print "[ERROR] the input file to the program is empty"
        sys.exit(1)
    sink_nodes = get_sink(outlinks)
    initialize_pagerank()
    perform_calculations()
    print "Length of inlinks: ", len(inlinks)
    print "Length of outlinks: ", len(outlinks) - len(sink)
    print "Length of Nodes : ", len(all_pages)
    print "Length of Sink : ", len(sink)
    print "Length of source : ", len(source)

if __name__ == '__main__':
    main()