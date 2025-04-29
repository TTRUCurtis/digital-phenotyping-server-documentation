Deployment
==========

To deploy changes:

1. Ensure changes are committed and pushed:

   .. code-block:: bash

      git add .
      git commit -m "Your message"
      git push origin main

2. On the server:

   .. code-block:: bash

      git pull origin main
      source venv/bin/activate
      pip install -r requirements.txt
      systemctl restart flask-server.service  # Or your deployment method

**Hosting Environment:**
- Ubuntu 22.04
- Gunicorn + Nginx
- Systemd for service management
