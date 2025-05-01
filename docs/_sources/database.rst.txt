Database Schema
===============

qualtrics_test Database
=======================

user_table
----------

+---------------+--------------------------------------------+------+-----+-------------------+-------------------+
| Field         | Type                                       | Null | Key | Default           | Extra             |
+===============+============================================+======+=====+===================+===================+
| recordId      | int                                        | NO   | PRI | NULL              | auto_increment    |
| studyId       | varchar(17)                                | NO   |     | NULL              |                   |
| createdDate   | datetime                                   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| phone         | varchar(10)                                | NO   |     | NULL              |                   |
| email         | text                                       | NO   |     | NULL              |                   |
| completedDate | datetime                                   | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| contactPref   | enum('sms','email','both')                 | NO   |     | sms               |                   |
| timezone      | enum('EST','MST','PST','CST','AKST','HST') | NO   |     | EST               |                   |
| phoneId       | varchar(16)                                | YES  |     | NULL              |                   |
+---------------+--------------------------------------------+------+-----+-------------------+-------------------+

notified_users
--------------

+-----------------------+----------------------------------------------------------------------------------------------------------+------+-----+-------------------+-------------------+
| Field                 | Type                                                                                                     | Null | Key | Default           | Extra             |
+=======================+==========================================================================================================+======+=====+===================+===================+
| recordId              | int                                                                                                      | NO   | PRI | NULL              | auto_increment    |
| studyId               | varchar(17)                                                                                              | YES  |     | NULL              |                   |
| notificationType      | enum('daily','monthly','reminder','missed-aware','missed-survey','baseline','welcome','register','none') | YES  |     | NULL              |                   |
| createdDate           | datetime                                                                                                 | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| messageSID            | text                                                                                                     | YES  |     | NULL              |                   |
| messageType           | enum('sms','email')                                                                                      | YES  |     | NULL              |                   |
| messageStatus         | text                                                                                                     | YES  |     | NULL              |                   |
| statusUpdateTime      | datetime                                                                                                 | YES  |     | NULL              |                   |
+-----------------------+----------------------------------------------------------------------------------------------------------+------+-----+-------------------+-------------------+

survey_table
------------

+---------------+------------------------------------------------------------------------------+------+-----+---------+----------------+
| Field         | Type                                                                         | Null | Key | Default | Extra          |
+===============+==============================================================================+======+=====+=========+================+
| recordId      | int                                                                          | NO   | PRI | NULL    | auto_increment |
| studyId       | varchar(17)                                                                  | NO   |     | NULL    |                |
| responseId    | varchar(17)                                                                  | YES  |     | NULL    |                |
| completedDate | datetime                                                                     | YES  |     | NULL    |                |
| weekday       | enum('monday','tuesday','wednesday','thursday','friday','saturday','sunday') | YES  |     | NULL    |                |
| type          | enum('consent','baseline','daily','weekly','monthly')                        | YES  |     | NULL    |                |
| surveyDate    | date                                                                         | YES  |     | NULL    |                |
+---------------+------------------------------------------------------------------------------+------+-----+---------+----------------+

enrolled_table
--------------

+-------------+---------------------------+------+-----+-------------------+-----------------------------------------------+
| Field       | Type                      | Null | Key | Default           | Extra                                         |
+=============+===========================+======+=====+===================+===============================================+
| recordId    | int                       | NO   | PRI | NULL              | auto_increment                                |
| studyId     | varchar(17)               | NO   |     | NULL              |                                               |
| updatedDate | datetime                  | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| enrolled    | enum('0','1','2','3','4') | NO   |     | NULL              |                                               |
| createdDate | datetime                  | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
+-------------+---------------------------+------+-----+-------------------+-----------------------------------------------+

aware_test Database
===================

health_check
------------

+--------------------+-------------+------+-----+-------------------+-------------------+
| Field              | Type        | Null | Key | Default           | Extra             |
+====================+=============+======+=====+===================+===================+
| recordId           | int         | NO   | PRI | NULL              | auto_increment    |
| studyId            | varchar(17) | NO   |     | NULL              |                   |
| createdDate        | datetime    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| raw                | text        | NO   |     | NULL              |                   |
| missingPermissions | text        | YES  |     | NULL              |                   |
+--------------------+-------------+------+-----+-------------------+-------------------+

phone_info
----------

+------------------+-------------+------+-----+---------+----------------+
| Field            | Type        | Null | Key | Default | Extra          |
+==================+=============+======+=====+=========+================+
| recordId         | int         | NO   | PRI | NULL    | auto_increment |
| studyId          | varchar(17) | YES  |     | NULL    |                |
| device           | text        | YES  |     | NULL    |                |
| brand            | text        | YES  |     | NULL    |                |
| manufacturer     | text        | YES  |     | NULL    |                |
| model            | text        | YES  |     | NULL    |                |
| product          | text        | YES  |     | NULL    |                |
| releaseVersion   | text        | YES  |     | NULL    |                |
| sdkVersion       | text        | YES  |     | NULL    |                |
| deviceIdentifier | varchar(16) | YES  |     | NULL    |                |
| createdDate      | timestamp   | YES  |     | NULL    |                |
| deviceLocation   | text        | YES  |     | NULL    |                |
+------------------+-------------+------+-----+---------+----------------+
