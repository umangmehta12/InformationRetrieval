package web_crawler;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.LinkedList;


import org.jsoup.*;
import org.jsoup.nodes.*;
import org.jsoup.select.Elements;
public class crawlWikipedia {
	
	
	private static HashSet<String> all = new HashSet<String>();
	private static HashSet<String> result = new HashSet<String>();
	private static LinkedList<String> queue = new LinkedList<>();
	private static LinkedList<String> childrenPages = new LinkedList<>();
	private static String keyphrase;
	
	public static void crawler(String seed, String keyphrase) throws IOException{
		Integer counter = 0;
		if (seed.contains("http:")) {
			seed = "https:" + seed.substring(5);
		}
		all.add(seed);
		queue.add(seed);
		//process(seed);
		while (true) {
			if (queue.isEmpty() || result.size() == 1000 || counter > 5) {
				break;
			}
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			process(queue.pop());
			if (queue.isEmpty()) {
				queue.addAll(childrenPages);
				childrenPages.clear();
				counter++;
			}
			
		}
		PrintWriter writer = new PrintWriter("crawledURLS.txt", "utf-8");
	    for (String url : result) {
    	    writer.println(url);
    	}
	    writer.close();
	}
	
	public static void process(String seed) throws IOException {
		String mainPage = "en.wikipedia.org/wiki/Main_Page";
		String PREFIX = "en.wikipedia.org/wiki/";
		
		Document doc = Jsoup.connect(seed).timeout(10000).get();
		String textData = doc.text().toLowerCase();
		
		if (textData.contains(keyphrase)) {
			result.add(seed);
			Elements e = doc.select("a");
		    for (Element single: e){
		    	String link = single.attr("abs:href");
		    	
		    	if (link.contains("#")) {
		    		link = link.substring(0, link.indexOf("#"));
		    	}
		    	if (link.contains("http:")) {
		    		link = "https:" + link.substring(5);
		    	}
		    	if (!all.contains(link)){
		    		String discardColon = single.attr("href");
			    	if (link.contains(PREFIX) && !discardColon.contains(":") && !link.contains(mainPage) && result.size() < 1000){
			    		all.add(link);
			    		childrenPages.add(link);
			    		if(keyphrase == "" || keyphrase == null) {
			    			result.add(link);
			    		}
			    	}	
		    	}
		    }
		}
	}
	
	public static void main(String args[]) throws IOException{
		if (args.length < 1 || args.length > 2){
			System.err.println("Invalid number of Parameters");
			System.exit(1);
		}
		else{
			String seed = args[0];
			keyphrase = "";
			if (args.length==2){
				keyphrase = args[1].toLowerCase();		
			}
			crawler(seed, keyphrase);
				
		}
	}
}
