CS6200 Information Retrieval Homework 02 README - Umang Mukesh Mehta - 001991047

- The zip folder contains : 
1. page_rank.py
   One python script that prints out :
   * the perplexity values
   * page ranks for each document
   * Size f inlinks,outlinks,sinks and sources
   * top fifty documents sorted by page_rank
   * top fifty documents sorted bby inlinks count

2. results.txt:
   * Answers to the questions in Section 01 which is finding the page_ranks for the 6 Node graph 
   * Answers to Section 02 question for calculating the perplexity value and convergence
   * Answers to questions :
         1. a list of the document IDs of the top 50 pages as sorted by PageRank, together with their PageRank values;
         2. a list of the document IDs of the top 50 pages by in-link count, together with their in-link counts;
         3. the proportion of pages with no in-links (sources);
         4. the proportion of pages with no out-links (sinks); and
         5. the proportion of pages whose PageRank is less than their initial, uniform values.

3. question04.pdf
    This file is the analysis of the top 10 page ranks and top 10 inlinks Analysis on the Lemur web interface
    Short Description of the Analysis:
    All the top10 pages by inlinks and by pageranks seem to be important so they have good page rank. 
    The analysis shows that
    • some page’s documents have higher inlink count whereas some documents are important considering peoples’ queries.
    • some are homepages that has financial, news and web content which the user is always interested in.
    • some have a very large number of outlinks that gets them good pagerank.
    • some are General disclaimers and have health related government information giving
      them high pagerank. Some pages are important from the point of view of user queries.
      So all factors determine the pagerank for a particular web page.

- Installation of python module:
You will have to install the following python modules for executing the script
   * argparse
Python 2.7.6 defaults you wont have to install these if you have version of python 2.7 +
   * sys
   * os
   * collections
   * math
   * operator

- Executing the script

$ python page_rank.py -h
  usage: page_rank.py [-h] -i file

  calculate the pageRanks of given pages

  optional arguments:
    -h, --help            show this help message and exit
    -i file, --input-file file
                          containing real web graph

* For 6 Node graphs:
  $ python page_rank.py -i input.txt
  Specify the counter for number of iteration 1,10,100 by default it is 100
  
  You will have to comment out :
  Line 104:  while isconverged(counter):
  Line 183-186  (Since these are function call for Section 02)
    get_top_fifty_pagerank()
    get_top_fifty_by_inlinks()
    difference_page_rank = compute_sizeof_difference_in_page_rank()
    print "\n Size of pages whose page rank is less than the initial page rank :", difference_page_rank

  
  You will have to uncomment:
  Line 107:  while counter<=100:
  
Example for default counter 100:
Input: $ python page_rank.py -i input.txt
Output:

Perplexity Values for the given graph
--------------------------------------------------------------------------------

Size of the Links based on Calculations :
--------------------------------------------------------------------------------

size of inlinks:  6
size of outlinks:  6
size of Nodes :  6
size of Sink :  0
size of source :  0

Page Rank for 6 Node graph with counter :
--------------------------------------------------------------------------------

Vertex :  A Page Rank for it :  0.252127105375
Vertex :  B Page Rank for it :  0.139306185319
Vertex :  C Page Rank for it :  0.151306489867
Vertex :  D Page Rank for it :  0.118907822574
Vertex :  E Page Rank for it :  0.187045906999
Vertex :  F Page Rank for it :  0.151306489867

Run Time:
  real	0m0.041s
  user	0m0.025s
  sys	0m0.013s


* For section 02 and Section 03
 $ python page_rank.py -i wt2g_inlinks.txt
 
 The default behaivour after you unzip the folder executes this phase
 It prints out:
   * Perplexity Value into the graph converges
   * Each Node and its page rank value
   * Size of Inlinks,outlinks,all_nodes,sinks and source
   * Top 50 sorted pages based on page rank
   * Top 50 sorted pages based on inlinks count
   * Size of difference value from intital page rank from final page rank

Run Time:
  real	0m40.748s
  user	0m39.849s
  sys	0m0.471s

-Assumptions:
* The program is checked to be running on CCIS Machine (I used ssh to loginto remote ccs machine)
* The program would be executed from the Homework02_UmangMukeshMehta folder
* The [in-links_page] needs to be a valid file, else the program might stop abruptly without starting the execution throwing exception.
