import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class LibraryDAO {

    public void addBook(Book book) {
        String sql = "INSERT INTO books (id, title, author, issued) VALUES (?, ?, ?, ?)";
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, book.getId());
            stmt.setString(2, book.getTitle());
            stmt.setString(3, book.getAuthor());
            stmt.setBoolean(4, book.isIssued());

            int rowsInserted = stmt.executeUpdate();
            if (rowsInserted > 0) System.out.println("✅ Book added successfully!");
            else System.out.println("❌ Failed to add book.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Book> getAllBooks() {
        List<Book> books = new ArrayList<>();
        String sql = "SELECT * FROM books";

        try (Connection conn = DBUtil.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                Book book = new Book(
                        rs.getInt("id"),
                        rs.getString("title"),
                        rs.getString("author")
                );
                book.setIssued(rs.getBoolean("issued"));
                books.add(book);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return books;
    }

    public void removeBook(int id) {
        String sql = "DELETE FROM books WHERE id = ?";

        try (Connection conn = DBUtil.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            int rowsDeleted = stmt.executeUpdate();
            if (rowsDeleted > 0) System.out.println("✅ Book removed successfully!");
            else System.out.println("❌ Book not found.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void issueBook(int id) {
        String sql = "UPDATE books SET issued = true WHERE id = ? AND issued = false";

        try (Connection conn = DBUtil.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            int rowsUpdated = stmt.executeUpdate();
            if (rowsUpdated > 0) System.out.println("✅ Book issued successfully!");
            else System.out.println("❌ Book not found or already issued.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void returnBook(int id) {
        String sql = "UPDATE books SET issued = false WHERE id = ? AND issued = true";

        try (Connection conn = DBUtil.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            int rowsUpdated = stmt.executeUpdate();
            if (rowsUpdated > 0) System.out.println("✅ Book returned successfully!");
            else System.out.println("❌ Book not found or not issued.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}