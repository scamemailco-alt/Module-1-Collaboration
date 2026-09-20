"""
Book CRUD API
A simple RESTful API for managing books using Flask.

Endpoints:
    GET    /books           - Retrieve all books
    GET    /books/<id>      - Retrieve a single book by ID
    POST   /books           - Create a new book
    PUT    /books/<id>      - Update an existing book
    DELETE /books/<id>      - Delete a book
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# ------------------------------------------------------------------
# In-memory "database" (replace with a real DB in production)
# ------------------------------------------------------------------
books = [
    {
        "id": 1,
        "book_name": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "publisher": "Addison-Wesley"
    },
    {
        "id": 2,
        "book_name": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall"
    }
]

# Helper to generate the next available ID
def next_id():
    if not books:
        return 1
    return max(book["id"] for book in books) + 1


# ------------------------------------------------------------------
# READ ALL  ->  GET /books
# ------------------------------------------------------------------
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200


# ------------------------------------------------------------------
# READ ONE  ->  GET /books/<id>
# ------------------------------------------------------------------
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        return jsonify({"error": f"Book with id {book_id} not found"}), 404
    return jsonify(book), 200


# ------------------------------------------------------------------
# CREATE  ->  POST /books
# ------------------------------------------------------------------
@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()

    # Basic validation
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    required_fields = ["book_name", "author", "publisher"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    new_book = {
        "id": next_id(),
        "book_name": data["book_name"],
        "author": data["author"],
        "publisher": data["publisher"]
    }
    books.append(new_book)
    return jsonify(new_book), 201


# ------------------------------------------------------------------
# UPDATE  ->  PUT /books/<id>
# ------------------------------------------------------------------
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        return jsonify({"error": f"Book with id {book_id} not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # Only update fields that were provided
    book["book_name"] = data.get("book_name", book["book_name"])
    book["author"]    = data.get("author",    book["author"])
    book["publisher"] = data.get("publisher", book["publisher"])

    return jsonify(book), 200


# ------------------------------------------------------------------
# DELETE  ->  DELETE /books/<id>
# ------------------------------------------------------------------
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        return jsonify({"error": f"Book with id {book_id} not found"}), 404

    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": f"Book with id {book_id} deleted"}), 200


# ------------------------------------------------------------------
# Run the app
# ------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)