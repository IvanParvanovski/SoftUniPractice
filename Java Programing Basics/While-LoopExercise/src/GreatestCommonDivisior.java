import java.util.Scanner;

public class GreatestCommonDivisior {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = Integer.parseInt(scanner.nextLine());
        int b = Integer.parseInt(scanner.nextLine());
        int resault = 0;

        if (b == 0){
            resault = a;
        }else
            {while (b != 0 ){
            resault = b;
            b = a % b;
            a = resault;
        }
            System.out.println(resault);

        }
    }
}
