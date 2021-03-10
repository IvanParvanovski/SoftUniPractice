import java.util.Scanner;

public class OnTimeforTheEcam {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int examHour = Integer.parseInt(scanner.nextLine());
        int examMinutes = Integer.parseInt(scanner.nextLine());
        int arrivalHour = Integer.parseInt(scanner.nextLine());
        int arrivalMinute = Integer.parseInt(scanner.nextLine());

        int examTimeInMinutes = arrivalHour * 60  + arrivalMinute;
        int arrivalTimeInMinutes = examHour * 60 + examMinutes;

        int diffHour = 0;
        int diffMinute = 0;
        int diff = arrivalTimeInMinutes - examTimeInMinutes;

        if (diff < 0){
            System.out.println("Late");
            diff = Math.abs(diff);
            if(diff < 60){
                System.out.printf("%d minutes after the start", diff);
            }else {
                diffMinute = diff % 60;
                diffHour = diff / 60;
                if (diffMinute < 10){
                    System.out.printf("%d:0%d hours after the start", diffHour , diffMinute);
                } else{
                    System.out.printf("%d:%d hours after the start", diffHour , diffMinute);
                }
            }
        } else if (diff > 30){
            System.out.println("Early");
            if (diff < 60) {
                System.out.printf("Early %d minutes before the start", diff);
            } else {
                diffMinute = diff % 60;
                diffHour = diff / 60;
                if (diffMinute < 10) {
                    System.out.printf("%d:0%d hours before the start", diffHour, diffMinute);
                }else {
                    System.out.printf("%d:%d hours before the start", diffHour , diffMinute);
                }
            }
        } else {
            System.out.println("On time");
            if (diff > 0){
                System.out.printf("%d minutes before the start", diff);
            }
        }


    }
}
