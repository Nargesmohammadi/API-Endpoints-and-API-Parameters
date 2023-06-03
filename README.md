# API-Endpoints-and-API-Parameters
Sure, here's a README that describes all three scripts in your repository:

# SMS Sending, GUI Quiz, and ISS Overhead Notifier

This repository contains three different Python scripts that provide functionality for sending SMS messages, taking a multiple-choice quiz via a GUI, and notifying the user of upcoming International Space Station (ISS) overhead passes.

## `send_sms.py`

The `send_sms.py` script provides functions that use various APIs to send SMS messages. The available functions are:

- `send_sms_twilio`: Uses the Twilio API to send an SMS message.
- `send_sms_nexmo`: Uses the Nexmo API to send an SMS message.
- `send_sms_msg91`: Uses the MSG91 API to send an SMS message.
- `send_sms_fast2sms`: Uses the Fast2SMS API to send an SMS message.

These functions take in different parameters depending on which API is being used, but generally require authentication credentials and information about the sender and recipient of the SMS message.

## `quiz_app.py`

The `quiz_app.py` script provides a graphical user interface for taking a multiple-choice quiz. The quiz questions and answers are stored in a separate CSV file (`quiz.csv`) which can be easily modified to include additional questions.

When the application is launched, the user is presented with a welcome screen. They can click on the "Start Quiz" button to begin the quiz or "Quit" to exit the application.

Once the quiz has started, the user is presented with one question at a time and must select one of the provided answer choices. The user can move forward and backward through the quiz using the "Next" and "Previous" buttons. The "Submit" button must be clicked once all questions have been answered, after which the user is presented with their score and an option to either quit the quiz or retake it.

The GUI was designed to be simple and intuitive, with user-friendly navigation buttons and clear instructions on each screen. The code makes use of the tkinter library to create the GUI elements and handle user input.

## `iss_overhead.py`

The `iss_overhead.py` script provides a command-line utility that notifies the user when the International Space Station (ISS) will be passing overhead. It uses the Open Notify API to retrieve the current location of the ISS and the Google Geocoding API to convert the user's location into latitude and longitude coordinates.

When run, the script prompts the user for their location (either as a city name or zip code). It then retrieves the user's latitude and longitude using the Google Geocoding API and calculates the next time the ISS will pass overhead. If the ISS is set to pass overhead within the next 15 minutes, the script sends an SMS message to the user's phone number (which must be specified in the code).

## Dependencies

The SMS sending script requires authentication credentials for the chosen API and may require additional package installations depending on the API used.

The GUI quiz script requires Python 3.x and the tkinter library to be installed on your system.

The ISS overhead notifier script requires Python 3.x and several external APIs, including Open Notify and Google Geocoding.

Overall, these scripts provide useful functionality for sending SMS messages, taking quizzes via a GUI, and receiving notifications about the ISS. Developers can use these scripts as a starting point to add similar functionality to their own projects.
