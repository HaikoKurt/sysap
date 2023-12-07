import requests
from requests.auth import HTTPBasicAuth

class SysAP :

    GET_CONFIGURATION = "http://{}/fhapi/v1/api/rest/configuration"
    GET_DEVICELIST = "http://{}/fhapi/v1/api/rest/devicelist"
    GET_DEVICE = "http://{}/fhapi/v1/api/rest/device/"
    GET_DATAPOINT = "http://{}/fhapi/v1/api/rest/datapoint/"

    def __init__(self, hostname, username, passwd, uuid) -> None:
        self.hostname = hostname
        self.username = username
        self.passwd = passwd
        self.uuid = uuid

    def __get(self, endpoint) :

        response = requests.get(endpoint.format(self.hostname), auth=HTTPBasicAuth(self.username, self.passwd))

        if response.status_code == 200:
            return response.json()

        return None

    def __put(self, endpoint, data) :

        headers = {
            'Content-Type': 'text/plain',
        }

        response = requests.put(endpoint.format(self.hostname), auth=HTTPBasicAuth(self.username, self.passwd), data=data, headers=headers)

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
    
    def set_datapoint(self, device_serial, channel, datapoint, value) :
        return self.__put(self.GET_DATAPOINT + self.uuid + "/" + device_serial + "." + channel + "." + datapoint, value)
    
if __name__ == "__main__" :
    from dotenv import load_dotenv
    import os

    load_dotenv()

    hostname = os.getenv("SYSAP")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWD")

    sysap = SysAP(hostname, username, password, "00000000-0000-0000-0000-000000000000")
    # print(sysap.get_datapoint("ABB2889C2851", "ch0010", "idp0000"))
    # print(sysap.get_device("ABB2889C2851"))
    print(sysap.set_datapoint("ABB2889C2851", "ch0010", "idp0000","0"))
    # print(sysap.get_device("6000A1CA6FE6"))
    # print(sysap.set_datapoint("6000A1CA6FE6", "ch0000", "odp0000","0"))
    # print(sysap.set_datapoint("6000A1CA6FE6", "ch0000", "odp0000","0"))
