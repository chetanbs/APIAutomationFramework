# Payloads

# Create Booking
# Update Booking
# Auth - Token

from dotenv import load_dotenv
import os

def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_update_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_update_booking_patch():
    payload = {
        "firstname": "Test",
        "lastname": "Python"
    }
    return payload


def payload_create_token():
    load_dotenv()
    payload = {
        "username" : os.getenv("USER"),
        "password" : os.getenv("PASSWORD")
    }
    return payload
