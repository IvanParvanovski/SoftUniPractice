import java.util.Scanner;

public class ForLoop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int num = 1; num < 1000; num++){
            if (num % 10 == 7){
                System.out.println(num);
            }
        }
    }
}
