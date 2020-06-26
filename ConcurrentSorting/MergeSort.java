package HW4;

import java.util.Arrays;
import java.util.Random;
import java.util.stream.IntStream;

public class MergeSort {

    private static final Random RNG    = new Random(10982755L);
    private static final int    LENGTH = 8192000;

    public static void main(String... args) {
        int[] arr = randomIntArray();
        long start = System.currentTimeMillis();
        concurrentMergeSort(arr);
        long end = System.currentTimeMillis();
        if (!sorted(arr)) {
            System.err.println("The final array is not sorted");
            System.exit(0);
        }
        System.out.printf("%10d numbers: %6d ms%n", LENGTH, end - start);
 
    	
    }
    public static void concurrentMergeSort(int[] arr, int threadCount) {
    	
    	
    	int n = arr.length;
		if (n<2)
			return;
		
		int[] s1 = Arrays.copyOfRange(arr,0,n/2);
		int[] s2 = Arrays.copyOfRange(arr, n/2, n);
		
		if(threadCount >1) {
			
			
			Thread t1 = new Thread(new Sorting(s1,threadCount/2));
			Thread t2 = new Thread(new Sorting(s2,threadCount/2));
			t1.start();
			t2.start();
			
			try {
				t1.join();
				t2.join();
			}catch(InterruptedException e){
				e.printStackTrace();
			}
		}else {
			if(n<2)
				return;
			concurrentMergeSort(s1,threadCount);
			concurrentMergeSort(s2,threadCount);
			
		}
		swap(s1, s2, arr);
		
		
		
	
		
		
    }
    
    
    public static void concurrentMergeSort(int [] arr) {
		int threadCount = Runtime.getRuntime().availableProcessors();
		
		
		concurrentMergeSort(arr,threadCount);
		
		
		
		
    	
		
    	
    	
    }

    public static void swap(int[] s1, int[]s2, int[]arr ) {
    	int n = s1.length + s2.length;
    	for(int i = 0, j = 0; i + j < n; ) {
    		if(i < s1.length && j < s2.length)
    		arr[i+j] = (s1[i]-s2[j] < 0) ? s1[i++] : s2[j++];
    		else if(i < s1.length)
    		arr[i+j] = s1[i++];
    		else
    		arr[i+j] = s2[j++];
    		}
    	
    }
    
    private static int[] randomIntArray() {
        int[] arr = new int[LENGTH];
        for (int i = 0; i < arr.length; i++)
            arr[i] = RNG.nextInt(LENGTH * 10);
        return arr;
    }

    public static boolean sorted(int[] arr) {
    	  for (int i = 1 ; i< arr.length; i++) {
    	         if(arr[i-1] > arr[i]) {
    	            return false;
    	         }
    	      }
    	      return true;
    }
}
