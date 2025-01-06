# Contains common utilities
# Read data from the excel file
# Read data from the csv, json file
# Set the headers - application/json, application/xml
from wsgiref.validate import header_re


class Utils(object):
    def common_headers_json(self):
        headers = {
            "Content-Type" : "application/json"
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type" : "application/json"
        }
        return headers

    def common_header_put_delete_patch_cookie(self, token):
        headers = {
            "Content-Type" : "application/json",
            "Cookie" : "token=" + str(token),
        }
        return headers


    def common_header_put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {
            "Content-Type" : "aplication/json",
            "Authorization" : "Basic " + str(basic_auth_value),
        }
        return headers