import java.util.*;
 
public class optQuick
{

	private static final int INSERTION_SORT_CUTOFF = 8;

    private static final int MEDIAN_OF_3_CUTOFF = 40;

	/**
     * Rearranges the array in ascending order, using the natural order.
     * @param a the array to be sorted
     */
    public static void quicksort(int [] a) {
        quickly(a, 0, a.length - 1);
    }

    private static void quickly(int [] a, int lo, int hi) { 
        int n = hi - lo + 1;

        // cutoff to insertion sort
        if (n <= INSERTION_SORT_CUTOFF) {
            insertionSort(a, lo, hi);
            return;
        }

        // use median-of-3 as partitioning element
        else if (n <= MEDIAN_OF_3_CUTOFF) {
            int m = median3(a, lo, lo + n/2, hi);
            exch(a, m, lo);
        }

        // use Tukey ninther as partitioning element
        else  {
            int eps = n/8;
            int mid = lo + n/2;
            int m1 = median3(a, lo, lo + eps, lo + eps + eps);
            int m2 = median3(a, mid - eps, mid, mid + eps);
            int m3 = median3(a, hi - eps - eps, hi - eps, hi); 
            int ninther = median3(a, m1, m2, m3);
            exch(a, ninther, lo);
        }

        // Bentley-McIlroy 3-way partitioning
        int i = lo, j = hi+1;
        int p = lo, q = hi+1;
        int v = a[lo];
        while (true) {
            while (less(a[++i], v))
                if (i == hi) break;
            while (less(v, a[--j]))
                if (j == lo) break;

            // pointers cross
            if (i == j && eq(a[i], v))
                exch(a, ++p, i);
            if (i >= j) break;

            exch(a, i, j);
            if (eq(a[i], v)) exch(a, ++p, i);
            if (eq(a[j], v)) exch(a, --q, j);
        }


        i = j + 1;
        for (int k = lo; k <= p; k++)
            exch(a, k, j--);
        for (int k = hi; k >= q; k--)
            exch(a, k, i++);

        quickly(a, lo, j);
        quickly(a, i, hi);
    }


    // sort from a[lo] to a[hi] using insertion sort
    private static void insertionSort(int[] a, int lo, int hi) {
        for (int i = lo; i <= hi; i++)
            for (int j = i; j > lo && less(a[j], a[j-1]); j--)
                exch(a, j, j-1);
    }


    // return the index of the median element among a[i], a[j], and a[k]
    private static int median3(int[] a, int i, int j, int k) {
        return (less(a[i], a[j]) ?
               (less(a[j], a[k]) ? j : less(a[i], a[k]) ? k : i) :
               (less(a[k], a[j]) ? j : less(a[k], a[i]) ? k : i));
    }

   /***************************************************************************
    *  Helper sorting functions.
    ***************************************************************************/
    
    // is v < w ?
    private static boolean less(int v, int w) {
        return v < w;
    }

    // does v == w ?
    private static boolean eq(int v, int w) {
        return v == w;
    }
        
    // exchange a[i] and a[j]
    private static void exch(int[] a, int i, int j) {
        int swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }
 
 
	public static int [] getArray(int size)
	{
		int [] array = new int[size];
		Random r = new Random();
 
		for(int i = 0; i < size; i++) {
			array[i] = r.nextInt(100);
		}
		return array;
	}
 
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
		array = getArray(100000);

		long start, end;
 
		//quicksort Time
		start = System.currentTimeMillis();
		quicksort(array);
		end = System.currentTimeMillis();
	    System.out.printf("Quick sort time: %10f%n", (end-start)/1000000.0);
 
	}
}
