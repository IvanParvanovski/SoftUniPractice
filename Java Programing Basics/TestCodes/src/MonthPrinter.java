import java.util.Scanner;

public class MonthPrinter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = Integer.parseInt(scanner.nextLine());

        if (num == 1){
            System.out.println("January");
        }

        if (num == 2){
            System.out.println("February");
        }

        if (num == 3){
            System.out.println("March ");
        }

        if (num == 4){
            System.out.println("April ");
        }

        if (num == 5){
            System.out.println("April ");
        }

        if (num == 6){
            System.out.println("June ");
        }

        if (num == 7){
            System.out.println("July ");
        }

        if (num == 8){
            System.out.println("August ");
        }

        if (num == 9){
            System.out.println("September ");
        }

        if (num == 10){
            System.out.println("October ");
        }

        if (num == 11){
            System.out.println("November ");
        }

        if (num == 12){
            System.out.println("December");
        }else if(num < 1 || num > 12) {
            System.out.println("Error!");
        }

    }
}
