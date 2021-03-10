import java.util.Scanner;

public class Point {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x1 = Integer.parseInt(scanner.nextLine());
        int y1 = Integer.parseInt(scanner.nextLine());
        int x2 = Integer.parseInt(scanner.nextLine());
        int y2 = Integer.parseInt(scanner.nextLine());
        int x = Integer.parseInt(scanner.nextLine());
        int y = Integer.parseInt(scanner.nextLine());

        if (x == x1 || x == x2 && y > y1 && y < y2)
            System.out.println("Border");
            else{
                System.out.println("Inside / Outside");}
        }

    }


