Book API Documentation
List Books: GET /api/books/ - Returns a list of all books.

Book Detail: GET /api/books/<id>/ - Returns details of a specific book.

Create Book: POST /api/books/create/ - Requires authentication. Validates title and publication year.

Update Book: PUT /api/books/update/<id>/ - Requires authentication.

Delete Book: DELETE /api/books/delete/<id>/ - Requires authentication.