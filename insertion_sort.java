import java.io.*;
import java.util.*;

public class insertion_sort {
	 public void insert(int num, int[] a, int i) {
		while ((i > 0) && (a[i - 1] > num)) {
			a[i] = a[i - 1];
			i--;
		}
		a[i] = num;
	}
	public int j = 0;
	
	public void insertionsort(int[] x, int k) {
		for (j = 1; j < k; j++ ) {
			int temp = x[j];
			insert(temp, x, j);
		}
	
	}
	public void printarr(int[] x, int i) {
		for(int j = 0; j < i; j++) {
              	System.out.printf("%d\n", x[j]);
               }     
	}
	
}
