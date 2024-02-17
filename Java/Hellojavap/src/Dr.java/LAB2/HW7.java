public class HW7 {
    public static void main(String[] args) {
        float h=5f, m=56f, s=23f;
        float h1 = m/60;
        float h2 = s/(60*60);
        float hf=h+h1+h2;
        float distance=(2500f/1000f);
        float Speed1=distance/hf;
        System.out.printf("Your velocity in km/h is %.7f\n",Speed1);
        System.out.printf("Your velocity in miles/h is %.7f\n",Speed1/1.609);
    }   
}
/* 7. You have been traveling on a bike for 5 hours, 56 minutes, and 23 seconds. 
Assuming the distance covered is (Last 4 digits of your student ID) meter. 
Write a Java code to display the velocity of your bike in kilometers per hour
and miles per hour. 
[Hint: 1 mile = 1609 meters]
Test Data:
Input distance in meters: 2500 // Assuming the last 4 digits are 2500
Expected Output:
Your velocity in km/h is 0.4208951 Your velocity in miles/h is 0.2615880 */