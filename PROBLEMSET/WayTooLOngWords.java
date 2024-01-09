import java.util.Scanner;
public class WayTooLongWords
{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int words = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < words; i++) {
            String word = sc.nextLine();
            System.out.println(shortWord(word));
        }
    }

    private static String shortWord(String word) {
        if(word.length() > 10) {
            return word.charAt(0) + String.valueOf(word.length() - 2) + word.charAt(word.length() - 1);
        }else {
            return word;
        }
    }
}
