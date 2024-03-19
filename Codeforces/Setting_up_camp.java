package Codeforces;
import java.util.Scanner;
public class Setting_up_camp {
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        int num_of_tent=0;
        for(int i=1;i<=t;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            int c=sc.nextInt();
            num_of_tent=a+(b/3)+(((b%3)+c)/3)+1;
            if(((b%3)+c)%3==0){
                num_of_tent=a+(b/3)+(((b%3)+c)/3);
            }
            else if(b%3!=0 && (b%3)+c<3){
                num_of_tent=-1;
            }
            else if(a==0 && b==0 && c==0){
                num_of_tent=0;
            }
            else if(b==0 && c==0){
                num_of_tent=a;
            }
            else if(a==0 && c==0){
                num_of_tent=b/3;
            }
            System.out.println(num_of_tent);
            num_of_tent=0;  
        }
        sc.close();
    }
}