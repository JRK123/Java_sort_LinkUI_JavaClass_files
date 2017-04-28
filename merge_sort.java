import java.io.*;
public class merge_sort {
	public int[] L;
	public int[] R;
	public void merge(int[] A, int p, int q,int r) {
		int n1 = q - p;
		int n2 = r - q;
		L = new int[n1 +1];
		R = new int[n2+1];
		for (int i = 0; i < n1 +1; i++ ) {
			L[i] = A[p + i];
		}
		for (int j = 0; j < n2 +1; j++) {
			R[j] = A[q +j];
		}
		L[n1] = Integer.MAX_VALUE;
		R[n2] = Integer.MAX_VALUE;
		int i = 0, j = 0;
		for (int k = p; p < r; p++) {
			if(L[i] < R[j]) {
				A[k] = L[i];
				i = i + 1;
			}
			else {
				A[k] = R[j];
				j = j + 1;
				
			}
		
		}
		
		
	}
	
	public void mergesort(int[] A, int p, int r) {
		if (p < r) {
			int q = (p+r)/2;
			mergesort(A, p, q);
			mergesort(A, q+1,r);
			merge(A,p,q,r);
		}
		A = L;
	} 
	
	
}

