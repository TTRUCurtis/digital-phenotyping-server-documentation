Common Problems
===============

1. **MySQL Connection Errors**

   - Check `.env` credentials
   - Ensure MySQL is running

2. **Flask ImportError**

   - Activate virtual environment
   - Reinstall requirements

3. **500 Internal Server Errors**

   - Check logs in `/var/log/flask-server/error.log`

4. **Permission Denied on Logs**

   - Make sure `flask` user has write access to log directory
