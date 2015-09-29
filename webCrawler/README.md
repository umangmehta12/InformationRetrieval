#Web Crawler
CS6200 Information Retrieval Homework 1 README - Umang Mukesh Mehta - 001991047

##The zip folder contains : 
	1) A folder : web_crawler - An Eclipse Project that implements Homework 01
	2) webCrawler.jar : I have converted the web crawler into an executable jar file that makes it easy to execute.
		To execute using delay of 10 second, this jar comes to the rescue.
			usage : java -jar webCrawler.jar [seed_page] [key_phrase]
			usage : java -jar webCrawler.jar "http://en.wikipedia.org/wiki/Hugh_of_Saint-Cher" "concordance" 
	3) A folder crawledURLS which contains 2 txt files 
   		1. crawledURLS_Unfocussed.txt which is list of urls done without keyphrase
   		2. crawledURLS_Focussed.txt which is list of urls clubbed with keyphrase "concordance"
	4) A text file Homework1.txt which contains answer to Homework 1 Question for proportion of total pages retrieved for keyphrase "concordance"
	5) jsoup-1.8.3.jar used by the program for HTML parsing

##Executing the program :
	1) Unzip the "Homework01_UmangMukeshMehta.zip" file into "Homework01_UmangMukeshMehta" folder.
	2) Open the command prompt at this folder.
	3) Ensure you open the command prompt with administrator privileges (Although not required, but it is better to do so)
	4) You can run the program in two ways.You will need to specify the seed url in both the ways else the program will terminate with an exit message for "Invalid number of Parameters"
	  1. You can run the executable webCrawler.jar directly which will take care of all the dependencies for jsoup-1.8.3.jar and produce list of crawledURLS.The crawledURLS can 	be either with/ without keyphrase based on the input provided by you.
	     usage : java -jar webCrawler.jar [seed_page] [key_phrase]
		 usage : java -jar webCrawler.jar "http://en.wikipedia.org/wiki/Hugh_of_Saint-Cher" "concordance"
	  2. You can run crawlWikipedia.java directly
         usage:
         javac -cp jsoup-1.8.3.jar crawlWikipedia.java
         java -cp .:jsoup-1.8.3.jar crawlWikipedia "http://en.wikipedia.org/wiki/Hugh_of_Saint-Cher" "concordance"
         This requires that you have jsoup-1.8.3.jar in the same directory as crawlWikipedia.java.This would also produce list of crawledURLS.The crawledURLS can 	be either with/ without keyphrase based on the input provided by you.

##Assumptions : 
	1) The program is checked to be running on CCIS Linux Machine.
	2) The program would be executed from the "Homework01_UmangMukeshMehta" folder.
	3) The [seed_page] needs to be a valid page/link, else the program might stop abruptly without starting the execution with the Invalid Parameter message.
	4) I have explicitly specified the socket time out to 10 seconds. The program could stop even if there is no internet connection availbe. 
	5) Since the homework requirement is to have a delay of atleast a second before requesting for a page to the server, the program might run a little longer than expected.
	   The running time may go uptil 90 mins for crawling around 23659 pages. This would generally happen when running the program using keyphrase "concordance"
