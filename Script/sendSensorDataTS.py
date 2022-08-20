from mainOksiTem import *
from thingspeak import Thingspeak, sendData

if __name__ == '__main__':
    w_key = 'F04QHPGCK4NWN7UX'
    r_key = '2WI5DIAIWU76CLX5'
    channel_id = 1827388                             # replace with channel id

    ob = Thingspeak(write_api_key=w_key, read_api_key=r_key, channel_id=channel_id)

    dataSensor = mainSensor()
    sendData(dataSensor[0], dataSensor[1], dataSensor[2])

