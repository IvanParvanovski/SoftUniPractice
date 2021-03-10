import java.util.Scanner;

public class voleyball {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String year = scanner.nextLine();
        int holidays = Integer.parseInt(scanner.nextLine());
        int weekendsInHome = Integer.parseInt(scanner.nextLine());

        int weekendInSofia = 48 - weekendsInHome;
        double countGamesInSofia = weekendInSofia * 3.0 / 4;
        double countGamesHoliday = holidays * 2.0 / 3;
        double CountGames = countGamesHoliday + countGamesInSofia + weekendsInHome;

        if (year.equalsIgnoreCase("leap")){
            CountGames = CountGames * 1.15;
        }

        System.out.printf("%.0f%n", Math.floor(CountGames));
    }
}
