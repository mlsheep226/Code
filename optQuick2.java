import java.util.*;
import java.util.Arrays;
 
public class optQuick2
{

	private static final int M = 10;
	private static final int MEDIAN_OF_3_CUTOFF = 40;
	/**
     * Rearranges the array in ascending order, using the natural order.
     * @param a the array to be sorted
     */

    public static void quickly(int[] a) { 
		Stack<int[]> stacked = new Stack<int[]>();
		boolean done;
		int i, j, v, p, q;
		int lo = 0;
		int hi = a.length - 1;
		done = (a.length <= M);
		while (!done) {
			int n = hi - lo + 1;
			
			if (n <= M){
				insertion(a, lo, hi);
			}
			else if (n <= MEDIAN_OF_3_CUTOFF) {
				int m = median3(a, lo, lo + n/2, hi);
				swap(a, m, lo);
			}
			else {
				int epper = n/8;
				int mid = lo + n/2;
				int m1 = median3(a, lo, lo + epper, lo + (2 * epper));
				int m2 = median3(a, mid - epper, mid, mid + epper);
				int m3 = median3(a, hi - (2 * epper), hi - epper, hi);
				int ninth = median3(a, m1, m2, m3);
				swap(a, ninth, lo);
			}
			
			i = lo + 1; 
			p = lo + 1;
			j = hi; 
			q = hi;
			v = a[lo];
			while (true) {
				while (a[++i] < v) {
					if(i== hi) break;
				}
				while (a[--j] > v) {
					if(j==lo) break;
		                }
				
				if (i== j && a[i] == v){
					swap(a, ++p, i);
				}
				if (i >= j) { 
					break;
				}
			}
			i = j + 1;
			for (int k = lo; k <= p; k++) {
				swap(a, k, j--);
			}
			for (int k = hi; k >= q; k--){ 
				swap(a, k, i++);
			}
			
			if(max(j-lo, hi-i+1) <= M) {
				if(stacked.empty()){
					done = true;
				}
				else {
					insertion(a, lo, hi);
					int[] b = stacked.pop();
					lo = b[0];
					hi = b[1];
				}
			}
			else {
				if (min(j-lo, hi-i) <= M) {
					if(max(j-lo, hi-i) == j - lo) {
						hi = j;
					}
					else {
						lo = i;
					}
				}
				else {
					int[] large = new int[2];
					if (max(j-lo, hi-i) == j - lo) {
						large = new int[]{lo, j};
						lo = i;
       					}
					else {
						large = new int[]{i, hi};
						hi = j;
					}					
					stacked.push(large);
				}
			}
		}
		System.out.println("\n\ni"); 
	}
		
	public static void insertion(int[] a, int lo, int hi) { 	
		
		for (int i = lo; i < hi; i++) {
			if (a[i] > a[i + 1]) {
				for (int j = i; j < lo && a[j] < a[j-1]; j--) {
					a[j + 1] = a[j];
					j++;
				}
			}
		}
        }
	public static int min(int one, int two) {
		if (one > two) {
			return two;
		}
		else {
			return one;
		}
	}
	public static int max(int one, int two) {
		if (one < two) {
			return two;
		}
		else {
			return one;
		}
	}

        
    private static void swap(int[] a, int i, int j) {
        int swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }
    public static int median3(int[] a, int l, int f, int p){
	return (less(a[l], a[f]) ? 
		(less(a[f], a[p]) ? f : less(a[l], a[p]) ? p : l) : 
		(less(a[p], a[f]) ? f : less(a[p], a[l]) ? p : l));
    }
    public static boolean less(int v, int w) {
	            return v < w;
    }
 
	/* makes array from random numbers 0-100
	* @param int size
	* @return int [] array
	*/
	public static int [] getArray(int size)
	{
		int [] array = new int[size];
		Random r = new Random();
 
		for(int i = 0; i < size; i++) {
			array[i] = r.nextInt(100);
		}
		return array;
	}
	/* displays the array
	 * @param int[] array sorted or unsorted array
	 * @param int right right most position in the array
	 * @param int left leftmost position in the  array
	*/
	public static void display(int [] array, int left, int right)
	{
		for(int i = left; i <= right; i++) {
			System.out.printf("%5d", array[i]);
		}
		System.out.println();
	}
 
	public static void main(String args[])
	{
		int [] array;
		array = getArray(50);
		int [] array2 = array.clone();
		Arrays.sort(array2);
		long start, end;
 		display(array, 0, array.length-1);
		//quicksort Time
		start = System.currentTimeMillis();
		quickly(array);
		end = System.currentTimeMillis();
	    	System.out.printf("Quick sort time: %10f%n", (end-start)/1000000.0);
		if (Arrays.equals(array, array2)){
            		System.out.println("Good");
			display(array, 0, array.length-1);
			display(array2, 0, array2.length-1);
		}
        	else{
            		System.out.println("Not Good");
			display(array, 0, array.length-1);
			display(array2, 0, array2.length-1);
		}
 
	}
}
