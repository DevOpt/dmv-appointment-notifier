# dmv-appointment-notifier
Can't get a DMV appointment? Get notified when there's an opening. This python script uses scheduler and Selenium webdriver to go on DMV website to check for Read ID appointment availability. When there is an opening, get notified via SMS from Twilio phone number.

### Prerequisites
You'll need:
* Twilio account with phone number. You can get a phone number with a free trial account.


### Setup
1. Install [Selenium ChromeDriver](https://chromedriver.chromium.org/downloads)
2. Get the token information from Twilio account and update below fields
```
twilio_account_sid = '<twilio_account_sid>'
twilio_auth_token = '<twilio_auth_token>'
```
3. Get `messaging_service_sid` from Twilio phone number, and add your destination phone number and update `to`
```
def send_alert_msg():
    twilio_client.messages.create(
        messaging_service_sid='<messaging_service_sid>',
        body='There is an open slot available. Visit https://telegov.njportal.com/njmvc/AppointmentWizard/12 to schedule your appointment',
        to='+12345678900'
    )
```
4. Run the script
```
python3 snipper.py
```
