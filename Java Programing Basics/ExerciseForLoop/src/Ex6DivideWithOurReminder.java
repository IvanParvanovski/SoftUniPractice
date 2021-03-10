import java.util.Scanner;

public class Ex6DivideWithOurReminder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        int counterrN = Integer.parseInt(scanner.nextLine());
        int procent = 0;
        double p1 = 0;
        double p2 = 0;
        double p3 = 0;


        for (int i = 0; i < counterrN; i++) {
            int number = Integer.parseInt(scanner.nextLine());

            if (number % 4 == 0){
                p3++;
            }

            if (number % 3 == 0){
                p2++;
            }

            if (number % 2 == 0){
                p1++;
            }

        }

        double prP1 = p1 / counterrN * 100;
        double prP2 = p2 / counterrN * 100;
        double prP3 = p3 / counterrN * 100;

        System.out.printf("%.2f%%\n", prP1);
        System.out.printf("%.2f%%\n", prP2);
        System.out.printf("%.2f%%\n", prP3);


    }
}
