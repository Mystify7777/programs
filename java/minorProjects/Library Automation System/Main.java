import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Library library = new Library();
        Scanner scanner = new Scanner(System.in);

        // Add sample books and members
        library.addBook(new Book("1984", "George Orwell", "1234567890"));
        library.addBook(new Book("To Kill a Mockingbird", "Harper Lee", "0987654321"));
        library.addMember(new Member("Alice", "M001", "alice@example.com"));
        library.addMember(new Member("Bob", "M002", "bob@example.com"));

        int choice;
        do {
            System.out.println("\nLibrary Automation System");
            System.out.println("1. View Books");
            System.out.println("2. View Members");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Books in the Library:");
                    for (Book book : library.getBooks()) {
                        System.out.println(book);
                    }
                    break;
                case 2:
                    System.out.println("Members in the Library:");
                    for (Member member : library.getMembers()) {
                        System.out.println(member);
                    }
                    break;
                case 3:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 3);

        scanner.close();
    }
}
