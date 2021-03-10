import java.util.Scanner;

public class Ex4MaxValue {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;


        for (int i = 0; i < n ; i++){
            int currentNumber = Integer.parseInt(scanner.nextLine());


            if (currentNumber > max){
                max = currentNumber;
            }
        }
        System.out.println(max);

    }
}
