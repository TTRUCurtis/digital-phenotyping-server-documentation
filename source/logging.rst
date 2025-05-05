Logging
=======

Logs are stored at:

- **Qualtrics logs:** `{user}/digital-phenotyping-server/qualtrics-server/logs/qualtrics.log`
- **AWARE logs:** `{user}/digital-phenotyping-server/aware-server/logs/aware.log`
- **Twilio logs:** `{user}/digital-phenotyping-server/twilio-server/logs/twilio.log`
- **Nginx Access logs:** `/var/log/nginx/access.log`
- **Nginx Error logs:** `/var/log/nginx/error.log`

The logs file for the server is rotated daily at 8 AM. With the earilier log file being appended with the date (e.g. `qualtrics.log.2025-04-20`)
