import java.util.Scanner;

public class Ex5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int etaps = Integer.parseInt(scanner.nextLine());
        double moneyFor1Point = Double.parseDouble(scanner.nextLine());
        double sum = 0;
        double sum1 = 0;
        int currentpoint = 0;

        for (int i = 1; i <= etaps ; i++){
            int point = Integer.parseInt(scanner.nextLine());
            if (i % 2 == 0){
                point = point * 2;
            }
            sum =  point + sum;
        }
        double money = sum * moneyFor1Point;

        System.out.printf("The project prize was %.2f lv.", money);

    }
}
