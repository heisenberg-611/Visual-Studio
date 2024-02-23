import java.util.Scanner;
public class HW7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the amount the customer need to pay(Taka)");
        int amount = sc.nextInt();
        System.out.println("Enter the amount, customer gave(Taka)");
        int given = sc.nextInt();
        if(given > amount){
            int change = given - amount;
            int note100 = change/100;
            int note50 = (change%100)/50;
            int note20 = ((change%100)%50)/20;
            int note10 = (((change%100)%50)%20)/10;
            int coin5 = ((((change%100)%50)%20)%10)/5;
            int coin2 = (((((change%100)%50)%20)%10)%5)/2;
            int coin1 = ((((((change%100)%50)%20)%10)%5)%2)/1;
            System.out.println("The returned amount is "+change+" taka.");
            System.out.println("100 taka note: "+note100);
            System.out.println("50 taka note: "+note50);
            System.out.println("20 taka note: "+note20);
            System.out.println("10 taka note: "+note10);
            System.out.println("5 taka coin: "+coin5);
            System.out.println("2 taka coin: "+coin2);
            System.out.println("1 taka coin: "+coin1);
        }
        else if(given < amount){
            int change = amount - given;
            System.out.println("Please pay "+change+" taka more.");
        }
        else{
            System.out.println("The returned amount is 0 taka.");
        }
        sc.close();
    }
}