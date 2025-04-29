Overview
========

This documentation provides an overview of a multi-server Flask system used for participant tracking, communication, and survey management for the Digital Phenotyping Study. The system consists of three core microservices:

1. **aware-server**
2. **twilio-server**
3. **qualtrics-server**
4. **study-info-page**

Each server is independently deployed using **Gunicorn** behind **NGINX** for scalability and production readiness. They communicate with MySQL database to log, track, and manage participant data.

System Architecture
-------------------

The system is divided into the following components:

**1. aware-server**
~~~~~~~~~~~~~~~~~~~
The `aware-server` handles passive health signal data from participants' mobile phones. Specifically, it receives periodic health signals and device information, for the initial health check, such as phone model, operating system version, android SDK, and other metadata relevant to the participant's mobile environment.

Key functionalities:
- Health ping endpoint for validating device connectivity
- Capture and log mobile device metadata
- Insert data into a dedicated MySQL table for device monitoring

**2. twilio-server**
~~~~~~~~~~~~~~~~~~~~
The `twilio-server` is responsible for all participant-facing communication. It sends SMS and/or email messages using Twilio's API and SendGrid respectively. This server also logs every notification sent, allowing for later auditing and report generation.

Key functionalities:
- Send registration, welcome, baseline, daily, and reminder messages
- Support for both SMS (Twilio) and email (SendGrid)
- Log notification history in a MySQL table for reporting

**3. qualtrics-server**
~~~~~~~~~~~~~~~~~~~~~~~
The `qualtrics-server` is the central logic hub of the system. It manages participant onboarding, survey logic, CRON-based scheduling for daily and follow-up surveys, and validation of survey access. It also tracks participant survey completion by storing study identifiers (studyID) and Qualtrics response IDs.

Key functionalities:
- Participant registration and onboarding
    - checking for fraudulent participants and blocking them
- Daily and monthly survey distribution via scheduled jobs
- Access validation for surveys based on participation criteria
- Store minimal survey metadata for tracking and compliance

**3. study-info-page**
~~~~~~~~~~~~~~~~~~~~~~~
The `study-page-server` is a front-end-focused Flask application that provides participants with access to public-facing study information. It assists new participants in getting started, including installing the Android app, reviewing frequently asked questions, and learning about the study goals.

Key functionalities:
- Web front-end for study instructions and app onboarding
- Displays FAQ, contact info, and overview of the study
- Static and templated pages for easy customization

Deployment Details
------------------

Each server is deployed as a standalone Flask application using the following stack:

- **Gunicorn**: WSGI HTTP server to serve the Flask applications
- **NGINX**: Acts as a reverse proxy and load balancer
- **MySQL**: Central database for storing participant data and system logs

Summary
-------

This architecture allows for modular, scalable, and secure tracking of participant engagement and survey management. Each component is independently deployable, making the system robust to faults and easy to maintain or extend.

