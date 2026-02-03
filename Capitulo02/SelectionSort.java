package Capitulo02;

import java.util.Arrays;

public class SelectionSort {
// Function to fin the index of the smallest element (starting from 'start)

    private static int findSmallest(int[] arr, int start) {
        int smallestIndex = start;

        for (int i = start +1; i < arr.length; i++) {
            if (arr[i] < arr[smallestIndex]) {
                smallestIndex = i;
            }
        }
        return smallestIndex;
    }
    
    // Mains Selection Sort function

    public static void selectionSort(int[] arr) {
        for (int i =0; i < arr.length; i++) {
            // Finds the smallest element in the remaining unsorted part.
        int smallestIndex = findSmallest(arr, i);
        
        // ... and swaps it with the current element
        int temp = arr[i];
        arr[i] = arr[smallestIndex];
        arr[smallestIndex] = temp;
        }
    }
    public static void main(String[] arts) {
        int[] myArray = {5, 3, 6, 2, 10};

        System.out.println("Original: " + Arrays.toString(myArray));

        selectionSort(myArray);

        System.out.println("Sorted: " + Arrays.toString(myArray));
    }

}
