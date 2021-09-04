from selenium import webdriver
from twilio.rest import Client
from selenium.webdriver.common.keys import Keys
import schedule
import time

# Twilio account setup
twilio_account_sid = '<twilio_account_sid>'
twilio_auth_token = '<twilio_auth_token>'
twilio_client = Client(twilio_account_sid, twilio_auth_token)


# Start the web driver
driver = webdriver.Chrome()
driver.get("https://telegov.njportal.com/njmvc/AppointmentWizard")
assert "Select Appointment Type - TeleGov" in driver.title


def send_alert_msg():
    twilio_client.messages.create(
        messaging_service_sid='<messaging_service_sid>',
        body='There is an open slot available. Visit https://telegov.njportal.com/njmvc/AppointmentWizard/12 to schedule your appointment',
        to='+12345678900'
    )


def check_appointment_count():
    title = driver.find_element_by_xpath(
        "//*[@id='step-1']/div/div[3]/div[3]/div[1]/div[2]/a[1]")
    assert "REAL ID" in title.text

    elem = driver.find_element_by_xpath(
        "//*[@id='step-1']/div/div[3]/div[3]/div[1]/div[2]/a[2]")

    print(elem.text)
    index = elem.text.index('Appointments')
    appointment = int(elem.text[:index-1])

    if appointment < 0:
        send_alert_msg()


# schedule job every minute to check for availability
schedule.every(1).minutes.do(check_appointment_count)


while True:
    schedule.run_pending()
    time.sleep(1)

# driver.close()
