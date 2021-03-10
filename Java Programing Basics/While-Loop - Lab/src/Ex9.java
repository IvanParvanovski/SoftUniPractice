import java.util.Scanner;

public class Ex9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int w = Integer.parseInt(scanner.nextLine());
        int l = Integer.parseInt(scanner.nextLine());
        int h = Integer.parseInt(scanner.nextLine());

        int roomVolume = w * l * h;

        int boxesVolum = 0;

        while(boxesVolum <= roomVolume){
            String command = scanner.nextLine();

            if(command.equalsIgnoreCase("done")){
                break;
            }
            int currentBoxesCount = Integer.parseInt(command);
            boxesVolum += currentBoxesCount;
        }
        int volumDiffrence = roomVolume - boxesVolum;

        if (volumDiffrence >= 0){
            System.out.printf("%d Cubic meters left", volumDiffrence);
        }else{
            System.out.printf("No more free space! You need %d Cubic meters more.", Math.abs(volumDiffrence));
        }
    }
}
