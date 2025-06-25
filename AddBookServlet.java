import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.IOException;

public class AddBookServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        int id = Integer.parseInt(req.getParameter("id"));
        String title = req.getParameter("title");
        String author = req.getParameter("author");

        Book book = new Book(id, title, author);
        LibraryDAO dao = new LibraryDAO();
        dao.addBook(book);

        resp.setContentType("text/plain");
        resp.getWriter().write("Book added successfully.");
    }
}
