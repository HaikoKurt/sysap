import requests
from requests.auth import HTTPBasicAuth

class SysAP :
    GET_CONFIGURATION = "http://sysap/fhapi/v1/api/rest/configuration"
    GET_DEVICELIST ="http://sysap/fhapi/v1/api/rest/devicelist"
    GET_DEVICE ="http://sysap/fhapi/v1/api/rest/device/"
    GET_DATAPOINT = "http://sysap/fhapi/v1/api/rest/datapoint/"

    def __init__(self, username, passwd, uuid) -> None:
        self.username = username
        self.passwd = passwd
        self.uuid = uuid

    def __get(self, endpoint) :
        response = requests.get(endpoint, auth=HTTPBasicAuth(self.username, self.passwd))

        if response.status_code == 200:
            return response.json()

        return None


    def get_configuration(self) :
        return self.__get(self.GET_CONFIGURATION)

    def get_device_list(self) :
        return self.__get(self.GET_DEVICELIST)
    
    def get_device(self, device_serial) :
        return self.__get(self.GET_DEVICE + self.uuid + "/" + device_serial)
    
    def get_datapoint(self, device_serial, channel, datapoint) :
        return self.__get(self.GET_DATAPOINT + self.uuid + "/" + device_serial + "." + channel + "." + datapoint)
    
if __name__ == "__main__" :
    from dotenv import load_dotenv
    import os

    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWD")

    sysap = SysAP(username, password, "00000000-0000-0000-0000-000000000000")
    print(sysap.get_datapoint("BEEDF44C0004", "ch0000", "idp0000"))
