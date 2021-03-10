import java.util.Scanner;

public class TicketCombination {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());
        int j = 1;



                for (char B = 'B'; B <= 'L'; B += 2) {
                    for (char f = 'f'; f >= 'a'; f--) {
                        for (char A = 'A'; A <= 'C'; A++) {
                            for (int num1 = 1; num1 <= 10; num1++) {
                                for (int num2 = 10; num2 >= 1; num2--) {
                                        if (j == n ){
                                            double money = B + f + A + num1 + num2;
                                            System.out.printf("Ticket combination: %s%s%s%d%d%n",B , f, A , num1 , num2 );
                                            System.out.printf("Prize: %.0f lv.", money);
                                            return;
                                        }
                                        j++;
                                }
                            }
                        }
                    }
                }
            }
        }


