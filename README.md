# Alarm based on hours of sleep

This project provides a wake-up call after a specified amount of sleep has been reached, as measured by a Fitbit device. Alarms based on a specified time of day, are of course, a normal feature. A sleep-based alarm, on the other hand, has been an oft-requested Fitbit feature since 2013 ([Fitbit community feedback](https://community.fitbit.com/t5/Product-Feedback/Alarm-based-on-set-hours-slept-eg-wake-me-up-after-8-hours/idi-p/1696221)). As of 2023, Fitbit has no plans to release such a feature. In fact, as will be explained shortly, this feature would not be possible under their current system.

First steps are to create and then authenticate an application that will access the Fitbit API. There is an excellent tutorial at shanelynn.ie:

[Create a personal Fitbit App](https://www.shanelynn.ie/plot-your-fitbit-data-in-python-api-v1-2/#create-a-personal-fitbit-app)</br>
[Authenticate and get an API token](https://www.shanelynn.ie/plot-your-fitbit-data-in-python-api-v1-2/#authenticate-and-get-an-api-token)

The project is run on a schedule via PythonAnywhere, checking personal sleep data on Fitbit's server. When the desired amount of sleep has been attained, an alert is sent.

Fitbit's API does have an endpoint for setting an alarm directly on the Fitbit device. However, only the very oldest devices are supported ([Fitbit API device support](https://dev.fitbit.com/build/reference/web-api/devices/create-alarm/#Device-support)). As an alternative, the smtplib library is used to send an alert by email.

Several years ago, Fitbit removed the feature where their devices automatically sync whether or not the Fitbit mobile app is open ([Fitbit All-Day Sync](https://community.fitbit.com/t5/iOS-App/All-Day-Sync-doesn-t-work-when-Fitbit-App-is-closed/td-p/4079586)). Currently, the devices sync with the server only when the mobile app is open. For this reason, as Fitbit cannot control when the user opens the app, they are not able to release a sleep-based alarm feature. In order for the server to continuously receive sleep data, two options are readily available:
1. Keeping the app open for the entire sleep duration. This requires keeping the screen on. Turning screen brightness to the lowest setting is recommended.
2. Using Shortcuts (on iPhone) or something similar to automate opening the app at regular intervals. If using Shortcuts, the device passcode must be turned off.
