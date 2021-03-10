import java.util.Scanner;

public class PyramideMe {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = Integer.parseInt(scanner.nextLine());
        for (int row = num; row >= 1; row--){
            for (int col = row; col >= row; col--){
                System.out.println(num);
                num++;
                System.out.println();
            }
        }
    }
}
