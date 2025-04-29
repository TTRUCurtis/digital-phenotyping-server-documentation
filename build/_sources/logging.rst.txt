Logging
=======

Logs are stored at:

- **Access logs:** `/var/log/flask-server/access.log`
- **Error logs:** `/var/log/flask-server/error.log`

Make sure the logs directory is writable by the Flask/Gunicorn process:

.. code-block:: bash

   sudo chown -R www-data:www-data /var/log/flask-server/
