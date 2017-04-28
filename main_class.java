import java.io.*;
import java.util.*;

public class main_class {
        public static void main(String[] args) {
                File infile = null;
                if (args.length > 0) {
                        infile = new File(args[0]);
                  //      System.out.printf("%s\n%s", args[0], args[1]);
                }
                else
                        System.out.println("so sorry");
                
                int[] arr = new int[1000];
                Scanner x = null;
                Formatter y = null; 
                try {
                	x = new Scanner(new File(args[0]));
                }
                
                catch (Exception e) {
                	System.out.println("enter valid file name");
                }
                
                int i = 0;
                while (x.hasNextInt()) {
                	arr[i] = x.nextInt();
                	i++;
                }
                x.close();
              //  System.out.printf("%d", arr[1]);
		try {
			y = new Formatter(new File(args[0]));
		}
		catch (Exception e1){
			System.out.println("file unable to open to write");
		}

		if (args[1].equals("insertion_sort")) {
                    //    System.out.println("so sorry");
			insertion_sort jayo = new insertion_sort();
			jayo.insertionsort(arr, i);
			for(int j = 0; j < i; j++) {
                  //		System.out.printf("%d\n", arr[j]);
				y.format("%d\n", arr[j]);
			}
		}
		if (args[1].equals("quick_sort")) {
			quick_sort jayo = new quick_sort();
			jayo.quicksort(arr, 0, i - 1);
			for(int j = 0; j < i; j++) {
                 // 		System.out.printf("%d\n", arr[j]);
				y.format("%d\n", arr[j]);
                   	}
		}
		
		if (args[1].equals("merge_sort")) {
			merge_sort jayo = new merge_sort();
			jayo.mergesort(arr, 0, i-1);
			for(int j = 0; j < i; j++) {
                  		System.out.printf("%d\n", arr[j]);
				y.format("%d\n", arr[j]);
                   	}
		}
		
		System.out.println("Sorted successfully!!!\nselect next file");     
		y.close();
		
              	
        
      }
        
}
