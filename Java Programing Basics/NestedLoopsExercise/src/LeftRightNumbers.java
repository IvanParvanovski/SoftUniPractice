import java.util.Scanner;

public class LeftRightNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num1 = Integer.parseInt(scanner.nextLine());
        int num2 = Integer.parseInt(scanner.nextLine());

        for (int i = num1; i <= num2; i++) {
            String lenghtNum = String.valueOf(i);

            int leftSide = lenghtNum.charAt(0) + lenghtNum.charAt(1);
            int rightSide = lenghtNum.charAt(3) + lenghtNum.charAt(4);

            if (leftSide != rightSide) {
                if (leftSide < rightSide) {
                    leftSide += lenghtNum.charAt(2);
                }
                if (rightSide < leftSide) {
                    rightSide += lenghtNum.charAt(2);
                }
            }

            if (leftSide == rightSide) {
                System.out.println(i + " ");
            }

            }

        }
    }


