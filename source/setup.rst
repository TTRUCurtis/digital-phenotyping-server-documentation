Setup
=====

**Requirements:**
- Python 3.8+
- MySQL 8.x
- virtualenv (recommended)

**Steps:**

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/your-org/your-flask-server.git
      cd your-flask-server

2. Create virtual environment:

   .. code-block:: bash

      python3 -m venv venv
      source venv/bin/activate

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Configure environment:

   Copy `.env.example` to `.env` and update credentials.

5. Run the server locally:

   .. code-block:: bash

      flask run
