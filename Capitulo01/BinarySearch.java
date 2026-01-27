package Capitulo01;

public class BinarySearch {
    // Método de Busca Binária em Java
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int guess = arr[mid];

            if (guess == target) {
                return mid;
            }
            if (guess > target) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return -1; 
    }
    public static void main(String[] args) {
        int[] myList =  {1, 3, 5, 7, 9};

        System.out.println(binarySearch(myList, 5));
        System.out.println(binarySearch(myList, 9));
        System.out.println(binarySearch(myList, 8));
    }
}
