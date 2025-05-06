Common Problems
===============

1. **Unenroll Participants**

   - SSH into the server and start MySQL shell or use a remote client to connect to the MySQL DB.
   - Confirm the current status of the partipant.

      .. code::block sql

         SELECT studyId, enrolled FROM qualtrics_test.enrolled_table WHERE studyId='<PARTICIPANT_STUDY_ID>';

   - Unenroll the participant with the following query.

      .. code::block sql

         UPDATE qualtrics_test.enrolled_table SET enrolled='0' WHERE studyId='<PARTICIPANT_STUDY_ID>';

2. **Flask ImportError**

   - Activate virtual environment
   - Reinstall requirements

3. **500 Internal Server Errors**

   - Check logs in `/var/log/flask-server/error.log`

4. **Permission Denied on Logs**

   - Make sure `flask` user has write access to log directory
