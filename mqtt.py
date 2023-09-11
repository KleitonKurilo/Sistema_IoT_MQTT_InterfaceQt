import paho.mqtt.client as mqtt




class MQTTSubscriber:
    def __init__(self, broker_address, topic):
        self.broker_address = broker_address
        self.topic = topic
        self.value = 0
        self.connected = False  # adiciona a variável booleana para rastrear a conexão
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def start(self):
        self.client.connect(self.broker_address)
        self.client.loop_start()
        #print(f'Subcriber {self.topic} START')


    def stop(self):

        self.client.loop_stop()
        #print(f'Subcriber {self.topic} STOP')

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:

            self.connected = True  # atualiza a variável booleana para True
            self.client.subscribe(self.topic)
        else:
            print("Failed to connect to MQTT broker with code "+str(rc))
            self.connected = False

    def on_message(self, client, userdata, msg):
        self.value = msg.payload.decode()

    def get_value(self):

        return self.value


    def is_connected(self):
        return self.connected  # adiciona um método para retornar o estado da conexão
        print(f"Subscriber {self.topic} conectado")

    def publish_message(self, message):
        self.client.publish(self.topic, message)

    def reconnect(self):

            if not self.connected:
                self.client.reconnect()
                self.client.subscribe(self.topic)
                self.connected = True
                print(f"Subscriber {self.topic} reconectado")
            else:
                print(f"Subscriber {self.topic} já está conectado")

    def disconnect(self):

        self.client.disconnect()
        print(f'Subscriber {self.topic} desconectado')


