package BroCode.Java;

import javax.swing.JOptionPane;

public class Class_5 {
    public static void main(String[] args) {
        
        String name = JOptionPane.showInputDialog("What is your name?");
        JOptionPane.showMessageDialog(null, "Hello " +name);
        int age = Integer.parseInt(JOptionPane.showInputDialog("How old are you?"));
        String food = JOptionPane.showInputDialog("What is your favorite food?");

        System.out.println("Hello "+name);
        System.out.println("You are "+age+" years old");
        System.out.println("You like "+food);

    }
}
