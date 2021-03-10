import java.util.Scanner;

public class Matrix {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = Integer.parseInt(scanner.nextLine());
        int b = Integer.parseInt(scanner.nextLine());
        int c = Integer.parseInt(scanner.nextLine());
        int d = Integer.parseInt(scanner.nextLine());

        for (int firstRowFirstNum = a; firstRowFirstNum <= b; firstRowFirstNum++){
            for (int firstRowSecondNum = a; firstRowSecondNum <= b; firstRowSecondNum++){
                for (int secondRowFirstNum = c; secondRowFirstNum <= d; secondRowFirstNum++){
                    for (int secondRowSecondNum = c; secondRowSecondNum <= d; secondRowSecondNum++){
                        if ((firstRowFirstNum + secondRowSecondNum) == (firstRowSecondNum + secondRowFirstNum) && (firstRowFirstNum != firstRowSecondNum) && (secondRowFirstNum != secondRowSecondNum)){
                            System.out.printf("%d%d%n", firstRowFirstNum , firstRowSecondNum);
                            System.out.printf("%d%d%n", secondRowFirstNum , secondRowSecondNum);
                            System.out.println();
                        }

                    }
                }
            }
        }
    }
}
