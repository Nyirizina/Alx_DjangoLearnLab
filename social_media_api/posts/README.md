## Posts & Comments API

This section details how to interact with the Posts and Comments endpoints. All write operations (`POST`, `PUT`, `PATCH`, `DELETE`) require an authentication token in the headers: `Authorization: Token <your_token>`.

### Posts

* **List Posts:** `GET /api/posts/`
  * *Query Parameters:* `?search=<keyword>` (Searches title and content), `?page=<number>` (Pagination).
  * *Response:* Paginated list of posts, including nested read-only comments.
* **Create Post:** `POST /api/posts/`
  * *Body:* `{ "title": "My First Post", "content": "Hello world!" }`
* **Retrieve Post:** `GET /api/posts/<id>/`
* **Update Post:** `PUT /PATCH /api/posts/<id>/` (Requires author permissions)
* **Delete Post:** `DELETE /api/posts/<id>/` (Requires author permissions)

### Comments

* **List Comments:** `GET /api/comments/`
* **Create Comment:** `POST /api/comments/`
  * *Body:* `{ "post": <post_id>, "content": "Great post!" }`
* **Update Comment:** `PUT /PATCH /api/comments/<id>/` (Requires author permissions)
* **Delete Comment:** `DELETE /api/comments/<id>/` (Requires author permissions)