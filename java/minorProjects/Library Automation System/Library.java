import java.util.ArrayList;
import java.util.List;





public class Library {
    private List<Book> books;
    private List<Member> members;

    public Library() {
        books = new ArrayList<>();
        members = new ArrayList<>();
    }

    // Methods to add, remove, and update books
    public void addBook(Book book) {
        books.add(book);
        System.out.println("Book added: " + book.getTitle());
    }

    public void removeBook(String isbn) {
        books.removeIf(book -> book.getIsbn().equals(isbn));
        System.out.println("Book removed with ISBN: " + isbn);
    }

    public void updateBook(String isbn, String title, String author) {
        for (Book book : books) {
            if (book.getIsbn().equals(isbn)) {
                book.setTitle(title);
                book.setAuthor(author);
                System.out.println("Book updated: " + book.getTitle());
            }
        }
    }

    // Methods to add, remove, and update members
    public void addMember(Member member) {
        members.add(member);
        System.out.println("Member added: " + member.getName());
    }

    public void removeMember(String memberId) {
        members.removeIf(member -> member.getMemberId().equals(memberId));
        System.out.println("Member removed with ID: " + memberId);
    }

    public void updateMember(String memberId, String name, String contact) {
        for (Member member : members) {
            if (member.getMemberId().equals(memberId)) {
                member.setName(name);
                member.setContact(contact);
                System.out.println("Member updated: " + member.getName());
            }
        }
    }

    // Method to issue books to members
    public void issueBook(String isbn, String memberId) {
        Book book = findBook(isbn);
        if (book != null && book.isAvailable()) {
            book.setAvailable(false);
            System.out.println("Book issued: " + book.getTitle() + " to member ID: " + memberId);
        } else {
            System.out.println("Book not available for issuing.");
        }
    }

    // Method to return books
    public void returnBook(String isbn) {
        Book book = findBook(isbn);
        if (book != null && !book.isAvailable()) {
            book.setAvailable(true);
            System.out.println("Book returned: " + book.getTitle());
        } else {
            System.out.println("Book is not issued.");
        }
    }

    // Helper method to find books by ISBN
    private Book findBook(String isbn) {
        for (Book book : books) {
            if (book.getIsbn().equals(isbn)) {
                return book;
            }
        }
        System.out.println("Book not found with ISBN: " + isbn);
        return null;
    }

    // Method to display all books
    public void displayBooks() {
        System.out.println("\nBooks in Library:");
        for (Book book : books) {
            System.out.println(book);
        }
    }

    // Method to display all members
    public void displayMembers() {
        System.out.println("\nMembers in Library:");
        for (Member member : members) {
            System.out.println(member);
        }
    }
}
