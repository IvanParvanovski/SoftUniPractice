import java.util.Scanner;

public class Ex5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = Integer.parseInt(scanner.nextLine());
        int b = Integer.parseInt(scanner.nextLine());

        for (int i = a; i <= b; i++){
            String currentNum = String.valueOf(i);

            if (currentNum.charAt(0) +  currentNum.charAt(2) + currentNum.charAt(4) == currentNum.charAt(1) +  currentNum.charAt(3) + currentNum.charAt(5)){
                System.out.printf("%s ",currentNum);

            }
        }
    }
}
