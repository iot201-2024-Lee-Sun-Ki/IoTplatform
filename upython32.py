import ComMgr
from umqtt.simple import MQTTClient
import time
from machine import reset, Pin
led = Pin(2, Pin.OUT)
nic = ComMgr.startWiFi('lab01')
server = 'sunkiiotlab101.zapto.org'
devid = 'dev2'
sub_topic = f'iot3/{devid}/cmd/power/fmt/json'
pub_topic = f'iot3/{devid}/evt/status/fmt/json'
def on_message(topic, msg):
    msg = msg.decode('utf-8')
    topic = topic.decode('utf-8')
    print(f'msg {msg} on topic {topic} arrived')
    if msg == 'stop':
        reset()
    elif msg == 'on':
        led.on()
    elif msg == 'off':
        led.off()
    client.publish(pub_topic, f'relay is {msg}')
client = MQTTClient(devid, server, 1883, user='dev2', password='0125')
client.set_callback(on_message)
client.connect()
client.subscribe(sub_topic)
time.sleep(1)
client.publish(pub_topic, f'{devid} is ready to talk')
try:
    while True:
        client.wait_msg()
finally:
    client.disconnect()
