Setup
=====

**Requirements:**
- OS Packages

    - Python 3.8+

        - pip 24.0
        - virtualenv

    - MySQL 8.x

- Python Packages

    - APScheduler 3.10.4
    - Flask 3.1.0
    - Flask-APScheduler 1.13.1
    - Flask-SQLAlchemy 3.1.1
    - google-api-core 2.24.2
    - google-api-python-client 2.166.0
    - google-auth 2.38.0
    - google-auth-httplib2 0.2.0
    - google-auth-oauthlib 1.2.1
    - googleapis-common-protos 1.69.2
    - gunicorn 23.0.0
    - mysql-connector-python 9.1.0
    - pandas 2.2.3
    - requests 2.32.3
    - sendgrid 6.11.0
    - Sphinx 8.2.3
    - SQLAlchemy 2.0.36
    - twilio 9.3.7

**Steps:**

1. Confirm the OS packages listed above are installed and are working.

2. Create virtual environment:

    .. code-block:: bash

      python3 -m venv <environment_name>
      source <environment_name>/bin/activate

3. Clone the repository:

    .. code-block:: bash

      git clone https://github.com/your-org/your-flask-server.git
      cd your-flask-server

4. Configure environment:

   Copy `.env.example` to `.env` and update credentials.

5. Run the server locally:

   .. code-block:: bash

      flask run
