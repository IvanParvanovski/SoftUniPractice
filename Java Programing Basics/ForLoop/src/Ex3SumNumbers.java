import java.util.Scanner;

public class Ex3SumNumbers {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = Integer.parseInt(scanner.nextLine());
        int sum = 0;

        for (int i = 0 ; i < num; i++){
            int current = Integer.parseInt(scanner.nextLine());
            sum = current + sum;

        }
        System.out.println(sum);

    }
}

