public class Sum {
	public static void main(String... args) {
		int[] number = {4, 7, 23, 89, 1, 22};

		System.out.println(largest(number));
		System.out.println(smallest(number));
	}

	public static int largest(int[] array) {
		int largest = array[0];

		for (int count = 0; count < array.length; count++) {
			if (array[count] > largest) {
				largest = array[count];
			}
		}
		
		return largest;
	}

	public static int smallest(int[] array) {
		int smallest = array[0];

		for (int count = 0; count < array.length; count++) {
			if (array[count] < smallest) {
				smallest = array[count];
			}
		}
		
		return smallest;
	}
}