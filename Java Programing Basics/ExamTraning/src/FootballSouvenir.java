import java.util.Scanner;

public class FootballSouvenir {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String team = scanner.nextLine();
        String souvenir = scanner.nextLine();
        int souvenirCount = Integer.parseInt(scanner.nextLine());

        double sum = 0;


        if (team.equalsIgnoreCase("Brazil") || team.equalsIgnoreCase("Argentina") || team.equalsIgnoreCase("Croatia") || team.equalsIgnoreCase("Denmark")) {
            if (souvenir.equalsIgnoreCase("flags") || souvenir.equalsIgnoreCase("caps") || souvenir.equalsIgnoreCase("posters") || souvenir.equalsIgnoreCase("stickers")) {

                //Argentina!!!!!
                if (team.equalsIgnoreCase("Argentina")) {
                    if (souvenir.equalsIgnoreCase("flags")) {
                        sum += 3.25;
                    } else if (souvenir.equalsIgnoreCase("caps")) {
                        sum += 7.20;
                    } else if (souvenir.equalsIgnoreCase("posters")) {
                        sum += 5.10;
                    } else if (souvenir.equalsIgnoreCase("stickers")) {
                        sum += 1.25;
                    }

                }

                //Brazil!!!!!
                if (team.equalsIgnoreCase("Brazil")) {
                    if (souvenir.equalsIgnoreCase("flags")) {
                        sum += 4.20;
                    } else if (souvenir.equalsIgnoreCase("caps")) {
                        sum += 8.50;
                    } else if (souvenir.equalsIgnoreCase("posters")) {
                        sum += 5.35;
                    } else if (souvenir.equalsIgnoreCase("stickers")) {
                        sum += 1.20;
                    }
                }

                //Croatia
                if (team.equalsIgnoreCase("Croatia")) {
                    if (souvenir.equalsIgnoreCase("flags")) {
                        sum += 2.75;
                    } else if (souvenir.equalsIgnoreCase("caps")) {
                        sum += 6.90;
                    } else if (souvenir.equalsIgnoreCase("posters")) {
                        sum += 4.95;
                    } else if (souvenir.equalsIgnoreCase("stickers")) {
                        sum += 1.10;
                    }
                }
                //Denmark
                if (team.equalsIgnoreCase("Denmark")) {
                    if (souvenir.equalsIgnoreCase("flags")) {
                        sum += 3.10;
                    } else if (souvenir.equalsIgnoreCase("caps")) {
                        sum += 6.50;
                    } else if (souvenir.equalsIgnoreCase("posters")) {
                        sum += 4.80;
                    } else if (souvenir.equalsIgnoreCase("stickers")) {
                        sum += 0.90;
                    }
                }
                sum *= souvenirCount;
            }
        }if (!(team.equalsIgnoreCase("Brazil") || team.equalsIgnoreCase("Denmark") || team.equalsIgnoreCase("Argentina") || team.equalsIgnoreCase("Croatia"))) {
                    System.out.println("Invalid country!");
        }else if (!(souvenir.equalsIgnoreCase("caps") || souvenir.equalsIgnoreCase("stickers") || souvenir.equalsIgnoreCase("flags") || souvenir.equalsIgnoreCase("posters") )){
            System.out.println("Invalid stock!");
        }else
            System.out.printf("Pepi bought %d %s of %s for %.2f lv.", souvenirCount, souvenir, team, sum);

    }
}

