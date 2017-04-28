public class quick_sort {
	private int partion(int[] A, int l, int r){
		int x = A[r];
		int i = l - 1;
		for (int j = l; j < r; j++) {
			if (A[j] <= x) {
				i = i + 1;
				int temp = A[j];
				A[j] = A[i];
				A[i] = temp;
			}
		}
		int temp = A[i + 1];
		A[i + 1] = A[r];
		A[r] = temp;
		return i + 1;
	} 
	
	public void quicksort(int[] A, int l, int r ) {
		if (l < r) {
			int q = partion(A, l, r);
			quicksort(A, l, q -1);
			quicksort(A, q + 1, r);
		}
		
	}
}

