import java.util.Scanner;

public class DayOfWeek2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int day = Integer.parseInt(scanner.nextLine());

        String dayWords = "";
        switch (day) {
            case 1:
                dayWords = "Monday";
                break;
            case 2:
                dayWords = "Tuesday";
                break;
            case 3:
                dayWords = "Wednesday";
                break;
            case 4:
                dayWords = "Thursday";
                break;
            case 5:
                dayWords = "Friday";
                break;
            case 6:
                dayWords = "Saturday";
                break;
            case 7:
                dayWords = "Sunday";
                break;
                default:
                    dayWords = "error";
                    break;


        }
        System.out.println(dayWords);
    }
}
