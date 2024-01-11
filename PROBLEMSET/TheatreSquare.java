import java.util.*;
public class TheatreSquare{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int a = sc.nextInt();
        System.out.print((n+a-1L)/a*((m+a-1)/a));
    }
}