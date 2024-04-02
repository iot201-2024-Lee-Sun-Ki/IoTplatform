import sys
import paho.mqtt.client as mqtt
if len(sys.argv) <= 1:
    print("\n\tUsage : "+sys.argv[0]+" devid\n")
    print("run this app with the device id to work with\n")
    exit()
devid = sys.argv[1]
pub_topic = f'iot3/{devid}/cmd/power/fmt/json'
sub_topic = f'iot3/{devid}/evt/status/fmt/json'
server = 'sunkiiotlab101.zapto.org'
def connect_cb(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe(sub_topic)
def message_cb(client, userdata, msg):
    print('>>> ', msg.payload.decode('UTF-8'))

client = mqtt.Client()
client.username_pw_set('app2', '0125')
client.connect(server, 1883, 60)
client.on_connect = connect_cb
client.on_message = message_cb
client.loop_start()
for line in sys.stdin:
    client.publish(pub_topic,line.strip().encode('UTF-8'))