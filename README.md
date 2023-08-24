# Alarm based on hours of sleep

This project provides a wake-up call after a specified amount of sleep has been reached. Alarms based on a specified time of day, are of course, a normal feature. A sleep-based alarm, on the other hand, has been an oft-requested Fitbit feature since 2013 ([Fitbit community feedback](https://community.fitbit.com/t5/Product-Feedback/Alarm-based-on-set-hours-slept-eg-wake-me-up-after-8-hours/idi-p/1696221)). As of 2023, Fitbit has no plans to release such a feature. In fact, as will be explained shortly, this feature would not be possible under their current system.

First steps are to create and then authenticate an application that will access the Fitbit API. There is an excellent tutorial at shanelynn.ie:

[Create a personal Fitbit App](https://www.shanelynn.ie/plot-your-fitbit-data-in-python-api-v1-2/#create-a-personal-fitbit-app)

[Authenticate and get an API token](https://www.shanelynn.ie/plot-your-fitbit-data-in-python-api-v1-2/#authenticate-and-get-an-api-token)

The project is run on a schedule, periodically checking personal sleep data on Fitbit's server. When the desired amount of sleep has been attained, an alert is sent.

Fitbit's API does have an endpoint for setting an alarm directly on the Fitbit device. However, only the very oldest devices are supported ([Fitbit API device support](https://dev.fitbit.com/build/reference/web-api/devices/create-alarm/#Device-support)). As an alternative, the smtplib library is used to send an alert by email.
