Setup
=====

Requirements
------------

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

Steps
-----

1. Confirm the OS packages listed above are installed and are working.

2. Create virtual environment:

    .. code-block:: bash

      python3 -m venv <environment_name>
      source <environment_name>/bin/activate
      <environment_name>/bin/python -m pip install -r <optional_path>/requirements.txt

3. Clone the repository:

    .. code-block:: bash

      git clone https://github.com/TTRUCurtis/digital-phenotyping-server.git
      cd digital-phenotyping-server
      git checkout dev

4. Create services for each of the servers:

    .. code-block:: bash

        cd /etc/systemd/system/
        sudo nano <server_name>.service
    
    * Copy the following code inside the file:

        .. code-block:: bash

            [Unit]
            Description=Gunicorn instance to serve <server_name> flask app
            After=network.target

            [Service]
            User=<user>
            WorkingDirectory=/home/<user>/digital-phenotyping-server/<server_name>
            Environment="TZ=America/New_York"
            ExecStart=/home/<user>/dps-env/bin/gunicorn --bind 127.0.0.1:<port_number> --preload run:app

            [Install]
            WantedBy=multi-user.target
    
    * Once all the required service files have been created

        .. code-block:: bash

            sudo systemctl daemon-reload
            sudo systemctl start <server_name> # To start the server
            sudo systemctl status <server_name> # To check the status of the server
            sudo systemctl restart <server_name> # To deploy any changes made to the server
    
    * Logs are captured in the logs directory inside each server's directory. To view all logs or crashes use the following command

        .. code-block:: bash
            
            journalctl -u <server_name>.service -n <optional_number_of_lines>

6. In Nginx create a proxy pass for each of the server's port_number. Below is a sample proxy pass. For a better guide on this please refer to `Configuring HTTPS Servers in NGINX <https://nginx.org/en/docs/http/configuring_https_servers.html>`_

    .. code-block:: bash

        ...
        location /<server>/ {
            proxy_pass http://127.0.0.1:<port_number>/;
        }
        ...
