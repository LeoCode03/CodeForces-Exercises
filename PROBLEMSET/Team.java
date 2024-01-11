import java.util.Scanner;
public class Team
{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int soluciones = 0;
        for(int i = 0; i < n; i++){
            int peyta = sc.nextInt();
            int vaysa = sc.nextInt();
            int tonya = sc.nextInt();
            if (((peyta != 0) && (peyta != 1)) || ((vaysa != 0) && (vaysa != 1)) || ((tonya != 0) && (tonya != 1))) {
                System.out.println("Solo se puede ingresar 0 o 1");
                break;
            }else if((peyta + vaysa + tonya) >= 2){
                soluciones += 1;
            }
        }
        System.out.println(soluciones);
    }
}
