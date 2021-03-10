import java.util.Scanner;

public class Ex6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int key = Integer.parseInt(scanner.nextLine());
        int sum = 0;
        int mnoj = 0;
        boolean u = false;
        boolean i = false;


        for (int a = 1; a <= 30; a++) {
            for (int b = 1; b <= 30; b++) {
                for (int c = 1; c <= 30; c++) {
                    sum = a + b + c;
                    mnoj = a * b * c;
                    if (a < b && b < c && sum == key) {
                        u = true;
                        System.out.print(a + " + " + b + " + " + c + " = " + key);
                        System.out.println();
                    }
                    if (a > b && b > c && mnoj == key) {
                        i = true;
                        System.out.print(a + " * " + b + " * " + c + " = " + key);
                        System.out.println();
                    }
                }
            }
        }

        if (i == false && u == false ) {
            System.out.println("No!");
        }
    }
}

