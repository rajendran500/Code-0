import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        LibraryDAO library = new LibraryDAO();
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n--- Library Menu ---");
            System.out.println("1. Add Book");
            System.out.println("2. Remove Book");
            System.out.println("3. Issue Book");
            System.out.println("4. Return Book");
            System.out.println("5. Show All Books");
            System.out.println("0. Exit");
            System.out.print("Enter choice: ");

            while (!sc.hasNextInt()) {
                System.out.println("Invalid input. Please enter a number.");
                sc.next();
            }

            choice = sc.nextInt();

            switch (choice) {
                case 1 -> {
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Enter Title: ");
                    String title = sc.nextLine();

                    System.out.print("Enter Author: ");
                    String author = sc.nextLine();

                    library.addBook(new Book(id, title, author));
                }
                case 2 -> {
                    System.out.print("Enter Book ID to Remove: ");
                    int id = sc.nextInt();
                    library.removeBook(id);
                }
                case 3 -> {
                    System.out.print("Enter Book ID to Issue: ");
                    int id = sc.nextInt();
                    library.issueBook(id);
                }
                case 4 -> {
                    System.out.print("Enter Book ID to Return: ");
                    int id = sc.nextInt();
                    library.returnBook(id);
                }
                case 5 -> {
                    List<Book> books = library.getAllBooks();
                    if (books.isEmpty()) {
                        System.out.println("No books in the library.");
                    } else {
                        for (Book book : books) {
                            System.out.println(book);
                        }
                    }
                }
                case 0 -> System.out.println("Exiting...");
                default -> System.out.println("Invalid choice!");
            }
        } while (choice != 0);

        sc.close();
    }
}
