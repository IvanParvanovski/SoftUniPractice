import java.util.Scanner;

public class MagicNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());

        for (int i = 1; i <= 9; i++){
            for (int a = 1; a <= 9; a++){
                for (int b = 1; b <= 9; b++){
                    for (int v = 1; v <= 9; v++){
                        for (int g = 1; g <= 9; g++){
                            for (int d = 1; d <= 9; d++){
                                long resul = i * a * b * v * g * d;
                                if (resul == n) {
                                    System.out.printf("%d%d%d%d%d%d ", i, a, b, v, g, d);
                                }
                            }
                        }
                    }
                }
            }
        }

    }
}
