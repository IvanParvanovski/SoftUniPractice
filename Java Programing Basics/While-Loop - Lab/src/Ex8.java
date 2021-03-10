import java.util.Scanner;

public class Ex8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = Integer.parseInt(scanner.nextLine());
        int num = 1;

        while (num <= number){
            System.out.println(num);
            num = (num * 2) + 1;
        }
    }
}
