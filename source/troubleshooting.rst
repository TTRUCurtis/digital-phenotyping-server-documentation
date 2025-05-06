Common Problems
===============

Unenroll Participants
---------------------

   - SSH into the server and start MySQL shell or use a remote client to connect to the MySQL DB.
   - Confirm the current status of the partipant.

   .. code-block:: sql

      SELECT studyId, enrolled FROM qualtrics_test.enrolled_table WHERE studyId='<PARTICIPANT_STUDY_ID>';

   - Unenroll the participant with the following query.

   .. code-block:: sql

      UPDATE qualtrics_test.enrolled_table SET enrolled='0' WHERE studyId='<PARTICIPANT_STUDY_ID>';

Send/Re-send AWARE Download Notification
----------------------------------------

   - Use the ``curl`` command or use an API platform such as Postman. 
   - **Method**: ``POST`` 
   - **URL**: ``https://ttru-smg.wwbp.org/qualtrics/registration/new-user?studyId=<PARTICIPANT_STUDY_ID>``

Check Notification Status of Sent Message
-----------------------------------------

   - SSH into the server and start MySQL shell or use a remote client to connect to the MySQL DB.
   - Use the following query.

   .. code-block:: sql

      SELECT * FROM qualtrics_test.notified_users WHERE studyId='<PARTICIPANT_STUDY_ID>' AND DATE(createdDate)='<DATE>';

   - A few other filters can also be applied such as:
   
      - ``notificationType`` which can be ``['register', 'baseline', 'welcome', 'daily', 'monthly', 'reminder', 'missed-aware', 'missed-survey']``.
      - ``messageType`` which can be ``['sms', 'email']``


Participant Did Not Receive Baseline Survey Notification
--------------------------------------------------------

   - Participant has successfully completed the AWARE app study registration.
   - Find the date of their initial health signal.

   .. code-block:: sql

      SELECT studyId, MIN(DATE(createdDate)) FROM aware_test.health_check WHERE studyId='<PARTICIPANT_STUDY_ID>';
   
   - Check the AWARE server logs with the date from the above result. 
   - Common Issues to debug this are:

      - Missing Permissions: Participant has not enabled all the required permissions most likely Bluetooth, which causes ``study_eligibility_info`` to contain the ``failed`` flag. Ask participant to re-install the app with all the required permissions enabled.
      - Missing Study Eligibility Info: At times AWARE app is not sending the key ``study_eligibility_info`` along with the initial health signal. Ask participant to re-install AWARE app.
   
Participant Received missed-aware Notification
----------------------------------------------

   - Participant has reached out that AWARE is installed on their phone and they received ``missed-aware`` notification.
   - Check the AWARE DB to see if participant's study ID has any rows in the sensor tables in AWARE DB.
   - Ask them to click the ``Sync`` button in AWARE app and keep WiFi ON.
