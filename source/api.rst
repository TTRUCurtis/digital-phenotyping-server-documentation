API Reference
=============

**Base URL:** ``https://ttru-smg.wwbp.org``

To make a request to the specific endpoint, use the format: ``<BASE_URL>/<SERVER_URL>/<ENDPOINT_URL>``

Qualtrics Server
----------------

**Server URL:** ``qualtrics``

**Endpoints:**

Register New User
~~~~~~~~~~~~~~~~~

- **URL**: ``registration/new-user``
- **Method**: ``POST``
- **Description**: Request participant survey responses from Qualtrics, store them in `user_table` and send `AWARE Download Text` to participant.
- **Query Parameters**:

    .. code-block:: python

        studyId: Participant's unique ID.
        limit: The number of users to return per page (optional).

Quit User
~~~~~~~~~

- **URL**: ``registration/quit-user``
- **Method**: ``POST``
- **Description**: Participant request to leave the study.
- **Request Body**:

    .. code-block:: json

        {
            "body": {
                "studyId": "<STUDY_ID>"
            }
        }

Update Participant Phone ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``registration/add-phoneId``
- **Method**: ``POST``
- **Description**: Update participant's phoneId in ``user_table`` after registering for a study inside AWARE app.
- **Request Body**:

    .. code-block:: json

        {
            "body": {
                "studyId": "<STUDY_ID>",
                "phoneId": "<PHONE_ID>"
            }
        }

Check Participant's Enrolled Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``registration/check-user``
- **Method**: ``POST``
- **Description**: Check and return participant's enrolled status if exists.
- **Request Body**:

    .. code-block:: json
        
        {
            "body": {
                "studyId": "<STUDY_ID>"
            }
        }

Check Participant's Duplicate Info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Method**: ``__duplicateInfo``
- **Description**: Checks if new participant's phone, email and/or phoneId already exist in the ``user_table``.
- **Method Parameters**:

    .. code-block:: python
        
        userInfo: UserTable # User Table object with participant info
        phoneId: str|None # New phoneId to be added

Schedule Daily Survey
~~~~~~~~~~~~~~~~~~~~~

- **Method**: ``__dailySurveyReminder``
- **Description**: CRON triggered method at 3 PM EST to schedule daily survey notification for enrolled participants. If participant is on day number 30/60, sends out followup notification instead of daily survey.
- **Method Parameters**: None

Baseline Completed
~~~~~~~~~~~~~~~~~~

- **URL**: ``survey/baseline``
- **Method**: ``POST``
- **Description**: Qualtrics pings endpoint after baseline survey completion. Info added to ``survey_table``.
- **Query Parameters**:

    .. code-block:: python

        studyId: Participant's unique ID.
        responseId: Participant's survey unique code.
        surveyDate: Date when baseline survey was sent.


Validate Daily Survey Link
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``survey/daily-survey-validate``
- **Method**: ``GET``
- **Description**: Server checks participant's enrolled status, timezone and time-window to redirect them to Qualtrics daily survey page for that day or redirect them to survey missed page.
- **Query Parameters**:

    .. code-block:: python

        studyId: Participant's unique ID.

Daily Survey Completed
~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``survey/daily``
- **Method**: ``POST``
- **Description**: Qualtrics pings endpoint after daily survey completion. Info added to ``survey_table``.
- **Query Parameters**:

    .. code-block:: python

        studyId: Participant's unique ID.
        responseId: Participant's survey unique code.
        surveyDate: Date when daily survey was sent.
        weekday: Day of the week.

Validate Monthly Survey Link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``survey/followup-survey-validate``
- **Method**: ``GET``
- **Description**: Server checks participant's enrolled status, timezone and time-window to redirect them to Qualtrics followup survey page for that day or redirect them to survey missed page.
- **Query Parameters**:

    .. code-block:: python

        studyId: Participant's unique ID.

Monthly Survey Completed
~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``survey/monthly``
- **Method**: ``POST``
- **Description**: Qualtrics pings endpoint after followup survey completion. Info added to ``survey_table``.
- **Query Parameters**:

    .. code-block:: python

        studyId: Participant's unique ID.
        responseId: Participant's survey unique code.
        surveyDate: Date when daily survey was sent.
        day_number: Number of days since enrolled (baseline survey completed date).

Send Daily Survey Reminder
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Method**: ``reminderNight``
- **Description**: Checks participant's who have not completed current days survey, then sends them a reminder notification to complete the survey at 9 PM local to their timezone. Only sends reminder for daily surveys.
- **Method Parameters**: None

Send Missed Survey/AWARE Notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``reminder/``
- **Method**: ``POST``
- **Description**: TTRU-AWARE server triggers endpoint daily morning (around 10 AM) with participant studyIDs and whether they missed completing daily survey and/or AWARE data. Sends notification to participant to keep being active in the study. 
- **Request Body**:

    .. code-block:: python

        {
            "data": [
                {
                    "index": "<ROW_NUMBER>",
                    "study_id": "<STUDY_ID>",
                    "AWARE": 0 if missed else 1,
                    "survey": 0 if missed else 1
                }
            ]
        }


Upload Status Report
~~~~~~~~~~~~~~~~~~~~~

- **Method**: ``__upload_person_level_stats``
- **Description**: Generates a report of each enrolled participant for the previous day. This method is triggered automatically when ``Send Missed Survey/AWARE Notification`` method is triggered.
- **Method Parameters**: None

Update SMS Notification Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``message/sms-status-check``
- **Method**: ``POST``
- **Description**: Twilio triggers endpoint which is specified as a status callback URL when SMS is attempted. Contains participant info and message SID to update or add record of final status of the attempted SMS notification.
- **Query Parameters**:

    .. code-block:: python

        studyId: Participant's unique ID.
        notification_type: What the notification was for.
        message_sid: Message's unique ID from Twilio.
        message_status: Message status whether delivered or error.

Update Email Notification Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``message/sms-status-check``
- **Method**: ``POST``
- **Description**: Twilio triggers endpoint which is specified as a status callback URL when email is attempted. Contains participant info and message SID to update or add record of final status of attempted email notification.
- **Request Body**:

    .. code-block:: python

        {
            "data": [
                {
                    "studyId": "<STUDY_ID>",
                    "notification": "<NOTIFICATION_TYPE>",
                    "sg_message_id": "<UNIQUE_MESSAGE_ID>",
                    "event": "<MESSAGE_STATUS>"
                }
            ]
        }

Check Enrolled Status
~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``admin/status-check-all``
- **Method**: ``POST``
- **Description**: Returns a JSON body of study IDs and their respective enrolled status and the status updated datetime as values.
- **Request Body**: None

AWARE Server
----------------

**Server URL:** ``aware``

**Endpoints:**

Initial Health Signal
~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``health/check``
- **Method**: ``POST``
- **Description**: Validates participant's device info, enabled permissions, verifies if device was already used previously by another participant. If all checks are satisfied, logs participant info in ``aware_test.health_check`` table and triggers baseline survey notification to participant. 
- **Request Body**: 

    .. code-block:: python

        {
            "data": {
                "device_info": {"JSON device specific information"},
                "permissions_status": "{JSON permission and boolean value if enabled or disabled}",
                "study_eligibility_info": "{JSON with location, bluetooth flag and info about whether participant passed the AWARE app checks}"
            }
        }

Periodic Health Signal
~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``health/check/update``
- **Method**: ``POST``
- **Description**: Validates participant's enabled permissions and logs info in ``aware_test.health_check`` table. Serves as a way to check that participant has AWARE installed on their device. Each participant's device sends a periodic health signal every 10 minutes. 
- **Request Body**: 

    .. code-block:: python

        {
            "data": {
                "pid": "<STUDY_ID>",
                "permissions_status": "{JSON permission and boolean value if enabled or disabled}",
            }
        }

Twilio Server
----------------

**Server URL:** ``twilio``

**Endpoints:**

Register New User
~~~~~~~~~~~~~~~~~

- **URL**: ``notify/register-user``
- **Method**: ``POST``
- **Description**: Attempts to send AWARE download SMS to participant's phone number through Twilio.
- **Request Body**: 

    .. code-block:: python

        {
            "data": {
                "studyId": "<STUDY_ID>",
            }
        }

Send Baseline Survey
~~~~~~~~~~~~~~~~~~~~

- **URL**: ``notify/baseline``
- **Method**: ``POST``
- **Description**: Attempts to send Welcome notification which contains info about onboarding and link to FAQs page, followed by Baseline survey notification after a 30 seconds delay to participant's through Twilio.
- **Request Body**: 

    .. code-block:: python

        {
            "data": {
                "studyId": "<STUDY_ID>",
            }
        }

Send Daily Survey
~~~~~~~~~~~~~~~~~

- **URL**: ``notify/daily-survey``
- **Method**: ``POST``
- **Description**: Attempts to send notification with daily survey redirect link to participant at 5 PM local to their timezone. This method schedules notifications through Twilio.  
- **Request Body**: 

    .. code-block:: python

        {
            "data": {
                "studyId": "<STUDY_ID>",
            }
        }

Send Followup Survey
~~~~~~~~~~~~~~~~~~~~

- **URL**: ``notify/followup-survey``
- **Method**: ``POST``
- **Description**: Attempts to send notification with followup survey redirect link to participant at 5 PM local to their timezone. This method schedules notifications through Twilio.  
- **Request Body**: 

    .. code-block:: python

        {
            "data": {
                "studyId": "<STUDY_ID>",
            }
        }

Send Daily Survey Reminder
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``notify/reminder-night``
- **Method**: ``POST``
- **Description**: Attempts to send a notification reminding participants to complete the daily survey at 9 PM local to their timezone. This method schedules notifications through Twilio.
- **Request Body**: 

    .. code-block:: python

        {
            "data": {
                "studyId": "<STUDY_ID>",
            }
        }

Send Missed AWARE/Survey Notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL**: ``notify/reminder``
- **Method**: ``POST``
- **Description**: Attempts to send a notification to participants to either keep AWARE active or complete daily surveys on time or both. This method triggers notifications through Twilio.
- **Request Body**: 

    .. code-block:: python

        {
            "data": {
                "studyId": "<STUDY_ID>",
                "remind": "<aware|survey|both>"
            }
        }

Refer to `routes.py` for full request/response details in the specific directory.


