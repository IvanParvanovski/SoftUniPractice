import java.util.Scanner;

public class Ex4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int count = Integer.parseInt(scanner.nextLine());
        int currentSum = 0;
        int previousSum = 0;
        int maxDiff = Integer.MIN_VALUE;

        for (int i = 0 ; i < count ; i++){

            int firstNum = Integer.parseInt(scanner.nextLine());
            int secondNum = Integer.parseInt(scanner.nextLine());

            previousSum = currentSum;
            currentSum = firstNum + secondNum;
            int diff = Math.abs(previousSum - currentSum);

            if (diff > maxDiff && i > 0 && previousSum != currentSum) {
                maxDiff = diff;
            }

        }if (maxDiff == Integer.MIN_VALUE){
            System.out.printf("Yes, value=%d", currentSum);
        } else  {
            System.out.printf("No, maxdiff=%d", maxDiff);
        }

    }
}
