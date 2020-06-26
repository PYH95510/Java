package HW4;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class WordCounter{

    // The following are the ONLY variables we will modify for grading.
    // The rest of your code must run with no changes.
    public static final Path FOLDER_OF_TEXT_FILES  = Paths.get("C:/textfiles/"); // path to the folder where input text files are located
    public static final Path WORD_COUNT_TABLE_FILE = Paths.get("C:/Users/pyh95/output.txt/"); // path to the output plain-text (.txt) file
    public static final int  NUMBER_OF_THREADS     = 2;                // max. number of threads to spawn 
    
    public static void main(String... args) {
        // your implementation of how to run the WordCounter as a stand-alone multi-threaded program
       WordCounter newCounter = new WordCounter();
       LinkedList<LinkedList> FinList = new LinkedList<LinkedList>();
       List theFileNames = new ArrayList();
       int numOfFiles = new File(FOLDER_OF_TEXT_FILES.toString()).list().length; // number of files in the folder
       newCounter.FilesList(FOLDER_OF_TEXT_FILES, FinList, theFileNames, NUMBER_OF_THREADS);
        newCounter.addNums(FinList);
        newCounter.writeNewFile(FinList, theFileNames);
      
    }

    

    public void FilesList(Path path, LinkedList<LinkedList> aList, List theFileNames, int numberofThreads){
        theFileNames.add(path.toString());
        try(Stream<Path> paths = Files.walk(path)) {
            final AtomicInteger count = new AtomicInteger();
            paths.forEach(filePath -> {
                if (Files.isRegularFile(filePath)) {
                    try {
                        count.incrementAndGet();
                        FileReading(filePath, aList, count, theFileNames);
                    } catch (Exception e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                }
            });
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public void FileReading(Path theFilePath, LinkedList<LinkedList> aList, AtomicInteger counter, List theFileNames) throws IOException{
        String aPathStr = theFilePath.toString().substring(theFileNames.get(0).toString().length() + 1, theFilePath.toString().length() - 4);
        theFileNames.add(aPathStr);
        List<String> theFileList = Files.readAllLines(theFilePath);
        String[] theSplitArray = theFileList.get(0).split(" ");
        for(int i = 0; i < theSplitArray.length; i++){
            theSplitArray[i] = theSplitArray[i].replaceAll("[\\W]", "");
            theSplitArray[i] = theSplitArray[i].toLowerCase();
          
           LinkedList newList = new LinkedList();
           newList.add(theSplitArray[i]);
           for(int j = 0; j < counter.get() - 1; j++){
               newList.add(0);
            }
           newList.add(1);

           Winsert(aList, newList, counter);
        }
       

    }

    public int getLength(LinkedList<LinkedList> aList){
        int longestLength = 0;
        for(int i = 0; i < aList.size(); i++){
            if(aList.get(i).get(0).toString().length() > longestLength){
                longestLength = aList.get(i).get(0).toString().length();
            }
        }
        return longestLength;
    }

    public void addNums(LinkedList<LinkedList> aList){
        for(int i = 0; i < aList.size(); i++){
            int theResult = 0;
            for(int j = 1; j < aList.get(i).size(); j++){
                theResult = theResult + (int)aList.get(i).get(j);
            }
            aList.get(i).addLast(theResult);
        }

    }

    public LinkedList<LinkedList>  Winsert(LinkedList<LinkedList> aList, LinkedList newList, AtomicInteger counter){
        String newText = newList.getFirst().toString();
        if(aList.size() == 0){
            aList.add(newList);
        }
        else{
            int a = 0;

            while(a < aList.size() && aList.get(a).get(0).toString().compareTo(newText) < 0){
                a++;
            }
            if(a == aList.size()){
                aList.addLast(newList);
            }
            else if(aList.get(a).get(0).toString().compareTo(newText) == 0){
                if(aList.get(a).size() - 1 == counter.get()){
                    aList.get(a).set(aList.get(a).size() - 1, (int)aList.get(a).getLast() + 1);
                }else{
                    for(int i = 1; i < counter.get() + 1; i++){
                        newList.set(i, aList.get(a).get(i));
                        aList.set(a, newList);
                    }
                }
            }
            else {
                aList.add(a, newList);
            }

        }
        for(int i = 0; i < aList.size(); i++){
            if(aList.get(i).size() - 1 < counter.get()){
                aList.get(i).add(0);
            }
        }
        return aList;
    }

    public synchronized void writeNewFile(LinkedList<LinkedList> aList, List theFileNames){
        int theLongestPlusOne = getLength(aList) + 1;
        FileWriter fileWriter = null;
        try {
            fileWriter = new FileWriter(String.valueOf(WORD_COUNT_TABLE_FILE));
        } catch (IOException e) {
            e.printStackTrace();
        }
        PrintWriter printWriter = new PrintWriter(fileWriter);

        String Width1c = "%-" + theLongestPlusOne + "s";

        printWriter.printf(Width1c, "");
        for(int i = 1; i < theFileNames.size(); i++){
            printWriter.printf("%-8s", theFileNames.get(i));
        }
        printWriter.printf("%-8s", "total");
        printWriter.printf("%n");

        

        for(int i = 0; i < aList.size(); i++){
            printWriter.printf(Width1c, aList.get(i).get(0));
            for(int j = 1; j < aList.get(i).size(); j++){
                printWriter.printf("%-8s", aList.get(i).get(j));
            }
            printWriter.printf("%n");
        }
        printWriter.close();
    }
    
   
}