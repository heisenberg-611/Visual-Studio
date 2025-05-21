public class Spring25_Final {
    public static void main(String[] args) {
        // Example input string
        String input = "99x+15y+23z";
        
        // Call the function to extract and sum the numbers
        int result = sumNumbersFromString(input);
        
        // Print the result
        System.out.println("Sum of numbers: " + result);
    }
    
    public static int sumNumbersFromString(String str) {
        int sum = 0;
        int currentNumber = 0;
        boolean processingNumber = false;
        
        // Iterate through each character in the string
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            
            // Check if the character is a digit
            if (c >= '0' && c <= '9') {
                // Convert character to integer and add to current number
                currentNumber = currentNumber * 10 + (c - '0');
                processingNumber = true;
            } else {
                // If we were processing a number and now hit a non-digit
                if (processingNumber) {
                    // Add the current number to the sum
                    sum += currentNumber;
                    // Reset current number for next potential number
                    currentNumber = 0;
                    processingNumber = false;
                }
            }
        }
        
        // Check if there's a number at the end of the string
        if (processingNumber) {
            sum += currentNumber;
        }
        
        return sum;
    }
}
