import java.util.Scanner;

public class BackIn30Minutes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int hours = Integer.parseInt(scanner.nextLine());
        int minutes = Integer.parseInt(scanner.nextLine());

        int minutes2 = minutes+30;

        if (minutes2 >= 60){
            minutes2 %= 60;
            hours++;
        }

        if (hours == 24){
            hours = 0;
        }

        if (minutes2 < 10){
            System.out.println(hours + ":0" + minutes2);
        }else
        System.out.println(hours + ":" + minutes2);




    }
}
