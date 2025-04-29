Database Schema
===============

**Database:** `flask_app_db`

**Tables:**
- `users`: Stores user information
- `orders`: Transaction details
- `notifications`: Sent messages and delivery statuses

Relationships:
- One-to-many between `users` and `orders`
- One-to-many between `users` and `notifications`

Refer to `models.py` for ORM definitions.
