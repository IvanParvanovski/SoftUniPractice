import java.text.DecimalFormat;
import java.util.Scanner;

public class Ex3 {
    public static void main(String[] args) {
        DecimalFormat df = new DecimalFormat("#.##");
        Scanner scanner = new Scanner(System.in);

        int count = Integer.parseInt(scanner.nextLine());

        double EvenMin = 100000000000.0;
        double EvenMax = -100000000000.0;

        double OddMin = 100000000000.0;
        double OddMax = -100000000000.0;

        double OddSum = 0.0;
        double EvenSum = 0.0;

        if (count == 0) {
            System.out.println("OddSum=" + 0);
            System.out.println("OddMin=" + "No");
            System.out.println("OddMax=" + "No");
            System.out.println("EvenSum=" + 0);
            System.out.println("EvenMin=" + "No");
            System.out.println("EvenMax=" + "No");
            return;
        }

            if (count == 1) {
                double num = Double.parseDouble(scanner.nextLine());
                System.out.printf("OddSum=%s\n", df.format(num));
                System.out.printf("OddMin=%s\n", df.format(num));
                System.out.printf("OddMax=%s\n", df.format(num));
                System.out.println("EvenSum=0,");
                System.out.println("EvenMin=No,");
                System.out.println("EvenMax=No,");
                return;
            }

            for (int i = 1; i <= count; i++) {
                double currentNumber = Double.parseDouble(scanner.nextLine());

                if (i % 2 == 0) {
                    EvenSum += currentNumber;
                    if (currentNumber > EvenMax) {
                        EvenMax = currentNumber;
                    }
                    if (currentNumber < EvenMin) {
                        EvenMin = currentNumber;
                    }
                } else {
                    OddSum += currentNumber;
                    if (currentNumber > OddMax) {
                        OddMax = currentNumber;
                    }
                    if (currentNumber < OddMin) {
                        OddMin = currentNumber;
                    }
                }
            }
            System.out.printf("OddSum=%s" + "OddMin=%s" + "OddMax=%s" + "EvenSum=%s" + "EvenMin=%s" + "EvenMax=%s",
                    df.format(OddSum), df.format(OddMin), df.format(OddMax), df.format(EvenSum), df.format(EvenMin), df.format(EvenMax));


        }
    }



