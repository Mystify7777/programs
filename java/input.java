import java.util.*;

public class input {
    public static void main(String[] args) {
        // Create a scanner object for user input
        Scanner sc = new Scanner(System.in);

        // Prompt the user to enter their name
        System.out.print("Please enter your name: ");
        String name = sc.nextLine();

        // Print the greeting message
        System.out.println("Hello, " + name + "!");
        
        // Close the scanner
        sc.close();
        }
}
