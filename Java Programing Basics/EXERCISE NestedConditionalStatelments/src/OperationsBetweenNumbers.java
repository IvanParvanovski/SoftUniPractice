import java.util.Scanner;

public class OperationsBetweenNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N1 = Integer.parseInt(scanner.nextLine());
        int N2 = Integer.parseInt(scanner.nextLine());
        String Char = scanner.nextLine();

        int sumNumbers = N1 + N2;
        int izvajdane = N1 - N2;
        int delene = (N1 / N2);
        int AbsoliutnaSt = N1 % N2;
        int umnojenie = N1 * N2;

        if (Char.equalsIgnoreCase("+")) {
            if (sumNumbers % 2 == 0) {
                System.out.println(N1 + " + " + N2 + " = " + sumNumbers + " - even");
            } else
                System.out.println(N1 + " + " + N2 + " = " + sumNumbers + " - odd");
        }


        if (Char.equalsIgnoreCase("/")) {
            if (N2 == 0) {
                System.out.println("Cannot divide " + N1 + " by zero");

            } else

                System.out.printf(N1 + " / " + N2 + " = %.2f", delene);
        }


        if (Char.equalsIgnoreCase("%")) {
            System.out.println(N1 + " % " + N2 + " = " + AbsoliutnaSt);
        }


        if (Char.equalsIgnoreCase("*")) {
            if (umnojenie % 2 == 0) {
                System.out.printf(N1 + " * " + N2 + " = " + umnojenie + " - even");
            } else
                System.out.println(N1 + " * " + N2 + " = " + umnojenie + " - odd");
        }

        if (Char.equalsIgnoreCase("-")) {
            if (izvajdane % 2 == 0) {
                System.out.printf(N1 + " - " + N2 + " = " + izvajdane + " - even");
            } else
                System.out.println(N1 + " - " + N2 + " = " + izvajdane + " - odd");

        }
    }
}
