import java.util.Scanner;

public class Ex6LeftRightSum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());

        int leftSum = 0;
        int rightSum = 0;
        for (int i = 0; i < n * 2; i++) {
            int cNum = Integer.parseInt(scanner.nextLine());
            if (i < n) {
                leftSum = cNum + leftSum;
            } else {
                rightSum += cNum;
            }
        }

        if (leftSum == rightSum) {

            System.out.println("Yes, sum = " + leftSum);
        }else if (leftSum != rightSum) {

            int diff = Math.abs(rightSum - leftSum);

            System.out.println("No, diff = " + diff);
        }
    }
}