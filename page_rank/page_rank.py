#!env python

"""Calculate the PageRank of the given graph and then perform analysis on inlinks.Also check for the convergence value"""
"""
__created_on__ =  10/16/2015
__author__ = "Umang Mukesh Mehta"
"""
import sys
import os

import argparse
import operator

from collections import defaultdict
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
    """creates the object via the input parsed"""
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
    """ creates inlinks and outlinks for the given input graph"""
    if not pages:
        inlinks[node]
    for page in pages:
        inlinks[node].add(page)
        outlinks[page].add(node)
    if not outlinks.has_key(node):
            outlinks[node]

def setup_links(line):
    """" sets up the nodes and pages in list of lines passed to create links"""
    pages = line.rstrip().split(" ")
    node = pages[0]
    all_pages.add(node)
    if len(pages) == 1:
        source.add(pages[0])
    createlinks(node, pages[1:])

def process_file(input_file):
    """ processes the files as specified by user"""
    with open(input_file, "r") as file:
        for line in file.read().splitlines():
            yield line

def get_sink(outlinks):
    """calculates the sink nodes"""
    for key, value in outlinks.iteritems():
            if value == set([]):
                sink.add(key)

def initialize_pagerank():
    """intializes the default value for page rank"""
    for page in all_pages:
        page_rank[page] = 1.0/len(all_pages)

def calculate_perplexity():
    """Calculates the perplexity for the probablity distribution of pages"""
    entropy = 0.0
    for page in page_rank.keys():
        entropy += page_rank[page] * math.log((1/page_rank[page]), 2)
    return 2**entropy

def isconverged(counter):
    """checks for convergence condition for a given graph"""
    perplexity_value = calculate_perplexity()
    print "Perplextiy Value : " ,perplexity_value
    perplexity.append(perplexity_value)
    if len(perplexity) > 4:
        if (int(perplexity[counter]) == int(perplexity[counter - 1]) == int(perplexity[counter - 2]) == int(perplexity[counter - 3])):
            print "Convergence Value : ",calculate_perplexity(),"\n"
            return False
        else:
            return True
    else:
        return True

def perform_calculations():
    """perform calculation for pageRank for a given graph"""
    counter = 0
    temp = (1.0 - DAMPING_FACTOR)/len(all_pages)
    print "Perplexity Values for the given graph "
    print "-" * 80 + "\n"
    while isconverged(counter):
#Uncomment the line below and comment the line above for the 6 Node graph
##########################################
#    while counter<=100:
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

def printing_page_rank():
    """prints page rank for 6 node graph"""
    sorted_page_ranks = sorted(page_rank.items(), key=operator.itemgetter(0))
    print "Page Rank for 6 Node graph with counter : "
    print "-" * 80 + "\n"
    for key, value in sorted_page_ranks:
        print "Vertex : ", key,"Page Rank for it : ", value

def get_top_fifty_pagerank():
    """gets the top fifty pageranks from the lit of pageranks"""
    top_fifty_page_rank = sorted(page_rank.items(), key=operator.itemgetter(1), reverse=True)
    print "Top Fifty pages sorted Page Rank "
    print "-" * 80 + "\n"
    for each_rank in xrange(50):
        print top_fifty_page_rank[each_rank]

def get_top_fifty_by_inlinks():
    """gets the top fifty inlinks from the lit of pageranks"""
    top_fifty_inlinks = dict()
    for vertex,links in inlinks.iteritems():
        count = 0
        for link in links:
            count+=1
        top_fifty_inlinks[vertex] = count
    sorted_inlinks = sorted(top_fifty_inlinks.items(), key=operator.itemgetter(1), reverse=True)
    print "\n"+"Top Fifty pages sorted by Inlinks count "
    print "-" * 80 + "\n"
    for each_inlink in xrange(50):
        print sorted_inlinks[each_inlink]

def compute_sizeof_difference_in_page_rank():
    """calculates the difference in page rank from the current and initial value"""
    difference_page_rank = dict()
    initial_page_rank = 1.0/183811
    for page,rank in page_rank.iteritems():
        if rank < initial_page_rank:
            difference_page_rank[page] = rank
    return len(difference_page_rank)


def main():
    parser = get_parser()
    args = parser.parse_args()
    if os.path.getsize(args.input_file) > 0:
        for line in list(process_file(args.input_file)):
            setup_links(line)
    else:
        print "[ERROR] the input file to the program is empty"
        sys.exit(1)
    sink_nodes = get_sink(outlinks)
    initialize_pagerank()
    perform_calculations()
    print "Size of the Links based on Calculations : "
    print "-" * 80 + "\n"
    print "size of inlinks: ", len(inlinks)
    print "size of outlinks: ", len(outlinks) - len(sink)
    print "size of Nodes : ", len(all_pages)
    print "size of Sink : ", len(sink)
    print "size of source : ", len(source) , "\n"
    printing_page_rank()
###################################################################
# Comment all the lines below when computing the 6 node graph
    get_top_fifty_pagerank()
    get_top_fifty_by_inlinks()
    difference_page_rank = compute_sizeof_difference_in_page_rank()
    print "\n Size of pages whose page rank is less than the initial page rank :", difference_page_rank

if __name__ == '__main__':
    main()