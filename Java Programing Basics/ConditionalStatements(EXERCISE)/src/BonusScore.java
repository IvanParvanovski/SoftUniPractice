import java.util.Scanner;

public class BonusScore {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int score = Integer.parseInt(scanner.nextLine());
        double bonus = 0;

        if (score <= 100){
             bonus = 5;
        }else if (score < 1000){
             bonus = (20 / 100.0) * score;
        }else {
             bonus = (10 / 100.0) * score;
        }
        if (score % 2 == 0){
            bonus = bonus + 1;

        }else {
            if (score % 10 == 5){
                bonus += 2;
            }
        }
        System.out.println(bonus);
        System.out.println(score + bonus);



    }
}
