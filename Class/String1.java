package Class;
public class String1 {
    public static void main(String[] args) {
        String s = "Hello World";
        String s1= "hello World";
        System.out.println(s.length());
        System.out.println(s.charAt(0));
        System.out.println(s.charAt(1));
        System.out.println(s.charAt(2));
        System.out.println(s.charAt(0) + s.charAt(1) + s.charAt(2));
        System.out.println(s.substring(0, 5));
        System.out.println(s.substring(6, 11));
        System.out.println(s.substring(6));
        System.out.println(s.substring(0, 1));
        System.out.println(s.equals(s1));
        System.out.println(s.equalsIgnoreCase(s1));
        System.out.println(s.compareTo(s1));
        System.out.println(s.compareToIgnoreCase(s1));
        System.out.println(s.toUpperCase());
        System.out.println(s.toLowerCase());
        System.out.println(s.concat(s1));
        System.out.println(s.contains("o"));
        System.out.println(s.contains("O"));
        System.out.println(s.indexOf("o"));
        System.out.println(s.indexOf("O"));
        System.out.println(s.indexOf("o", 1));
        System.out.println(s.indexOf("O", 1));
        System.out.println(s.startsWith("H"));
        System.out.println(s.startsWith("h"));
        System.out.println(s.endsWith("d"));
        System.out.println(s.endsWith("D"));
        System.out.println(s.replace("o", "a"));
        System.out.println(s.replaceAll("o", "a"));
        System.out.println(s.replaceFirst("o", "a"));
        System.out.println(s.trim());
        System.out.println(s.trim().length());
        System.out.println(s.trim().concat(" ").concat(s1.trim()));
        System.out.println(s.trim().concat(" ").concat(s1.trim()).length());
        System.out.println(s.trim().concat(" ").concat(s1.trim()).replaceAll("\\s+", " "));
    }
}