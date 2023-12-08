import requests
from requests.auth import HTTPBasicAuth

class SysAP :

    GET_CONFIGURATION = "http://{}/fhapi/v1/api/rest/configuration"
    GET_DEVICELIST = "http://{}/fhapi/v1/api/rest/devicelist"
    GET_DEVICE = "http://{}/fhapi/v1/api/rest/device/"
    GET_DATAPOINT = "http://{}/fhapi/v1/api/rest/datapoint/"
    REGISTER_VIRTUAL_DEVICE = "http://{}/fhapi/v1/api/rest/virtualdevice/"

    DEVTYPE_BINARY_SENSOR = "BinarySensor"
    DEVTYPE_SWITCHING_ACTUATOR = "SwitchingActuator"
    DEVTYPE_CEILING_FAN_ACTUATOR = "CeilingFanActuator"
    DEVTYPE_RTC = "RTC"
    DEVTYPE_DIM_ACTUATOR = "DimActuator"
    DEVTYPE_WINDOW_SENSOR = "WindowSensor"
    DEVTYPE_SHUTTER_ACTUATOR = "ShutterActuator"
    DEVTYPE_WEATHER_STATION = "WeatherStation"
    DEVTYPE_WEATHER_TEMPERATURESENSOR = "Weather-TemperatureSensor"
    DEVTYPE_WEATHER_WINDSENSOR = "Weather-WindSensor"
    DEVTYPE_WEATHER_BRIGHTNESSSENSOR = "Weather-BrightnessSensor"
    DEVTYPE_WEATHER_RAINSENSOR = "Weather-RainSensor"
    DEVTYPE_CO_DETECTOR = "CODetector"
    DEVTYPE_FIRE_DETECTOR = "FireDetector"
    DEVTYPE_KNX = "KNX-SwitchSensor"
    DEVTYPE_MEDIA_PLAYER = "MediaPlayer"
    DEVTYPE_ENERGY_BATTERY = "EnergyBattery"
    DEVTYPE_ENERGY_INVERTER = "EnergyInverter"
    DEVTYPE_ENERGY_METER = "EnergyMeter"
    DEVTYPE_ENERGY_INVERTER_BATTERY = "EnergyInverterBattery"
    DEVTYPE_ENERGY_INVERTER_METER = "EnergyInverterMeter"
    DEVTYPE_ENERGY_INVERTER_METER_BATTERY = "EnergyInverterMeterBattery"
    DEVTYPE_ENERGY_METER_BATTERY = "EnergyMeterBattery"
    DEVTYPE_AIR_QUALITY_CO2 = "AirQualityCO2"
    DEVTYPE_AIR_QUALITY_CO = "AirQualityCO"
    DEVTYPE_AIR_QUALITY_FULL = "AirQualityFull"
    DEVTYPE_AIR_QUALITY_HUMIDITY = "AirQualityHumidity"
    DEVTYPE_AIR_QUALITY_NO2 = "AirQualityNO2"
    DEVTYPE_AIR_QUALITY_O3 = "AirQualityO3"
    DEVTYPE_AIR_QUALITY_PM10 = "AirQualityPM10"
    DEVTYPE_AIR_QUALITY_PM25 = "AirQualityPM25"
    DEVTYPE_AIR_QUALITY_PRESSURE = "AirQualityPressure"
    DEVTYPE_AIR_QUALITY_TEMPERATURE = "AirQualityTemperature"
    DEVTYPE_AIR_QUALITY_VOC = "AirQualityVOC"

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

    def __put(self, endpoint, data, json = False) :
        if json :
            headers = { 'Content-Type': 'application/json' }
            if data is not None :
                data = str(data).replace("'", "\"")
        else :
            headers = { 'Content-Type': 'text/plain' }

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
    
    def register_virtual_device(self, serial, type, ttl, displayname) :
        properties = {}
        properties["ttl"] = str(ttl)
        properties["displayname"] = displayname
        data = {}
        data["type"] = type
        data["properties"] = properties
        return self.__put(self.REGISTER_VIRTUAL_DEVICE + self.uuid + "/" + serial, data, json = True)
    
