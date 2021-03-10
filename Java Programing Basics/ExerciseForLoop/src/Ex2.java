import java.util.Scanner;

public class Ex2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num = Integer.parseInt(scanner.nextLine());
        int max = Integer.MIN_VALUE;
        int sum = 0;

        for (int i = 0; i < num; i++){
            int countNum = Integer.parseInt(scanner.nextLine());
            sum += countNum;

            if (countNum > max){
                max = countNum;
            }

        }

        if (sum - max  == max){
            System.out.printf("Yes%nSum = %d", max);
        }else {
            System.out.printf("No%nDiff = %d", Math.abs(2*max - sum));
        }

    }
}
