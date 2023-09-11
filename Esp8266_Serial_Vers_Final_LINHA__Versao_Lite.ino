#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#include <ModbusRtu.h>


 const char* ssid = "WiFi Alufrost";
 const char* password = "8^eHPyXg6*Ey";
 const char* mqtt_server = "192.168.3.172";
 const char* mqtt_topic = "Mesa3";
 const char* mqtt_topic1 = "EstA3";
 const char* mqtt_topic2 = "EstR3";
 const char* mqtt_topic3 = "PreA3";
 const char* mqtt_topic4 = "PreR3";
 const char* mqtt_topic5 = "HyA3";
 const char* mqtt_topic6 = "HyP3";
 


WiFiClient espClient;
PubSubClient client(espClient);



// data array for modbus network sharing
uint16_t au16data[16] = {
  3, 1415, 9265, 4, 2, 7182, 28182, 8, 0, 0, 0, 0, 0, 0, 1, -1 };


uint16_t leitura_registro;
/**
 *  Modbus object declaration
 *  u8id : node id = 0 for master, = 1..247 for slave
 *  port : serial port
 *  u8txenpin : 0 for RS-232 and USB-FTDI 
 *               or any pin number > 1 for RS-485
 */
Modbus slave(1,Serial,0); // this is slave @1 and RS-232 or USB-FTDI





void setup() {


  ESP.wdtDisable();//Desabilita o SW WDT.


  Serial.begin(9600);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(2500);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  client.setServer(mqtt_server, 1883);

  // Configurar a conexão com o servidor MQTT


  while (!client.connected()) {
    Serial.println("Conectando ao servidor MQTT...");
    if (client.connect("ESP8266_Linha3")) {
      Serial.println("Conexão MQTT estabelecida!");
    } else {
      Serial.print("Falha na conexão ao servidor MQTT, rc=");
      Serial.print(client.state());
      Serial.println(" Tentando novamente em 5 segundos...");
      delay(2000);
    }
  }

    slave.start();

}

void loop() {
  slave.poll(au16data, 16);

  ESP.wdtFeed();

  for (int i = 0; i < 1; i++) {


    
   if (au16data[i] != leitura_registro){

    if (au16data[i] >= 1000 and au16data[i] < 2000) {
      int Mesa1 = au16data[i];

      // Publicar o valor de Mesa1 no servidor MQTT
      char msg[10];
      sprintf(msg, "%d", Mesa1);
      client.publish(mqtt_topic, msg);
     
    }

    if (au16data[i] >= 2000 and au16data[i] < 4000) {
      int VazaoApr1 = au16data[i];
      
      // Publicar o valor de VazaoApr1 no servidor MQTT
      char msg[10];
      sprintf(msg, "%d", VazaoApr1);
      client.publish(mqtt_topic1, msg);
      
    }

   
      if (au16data[i] >= 4000 and au16data[i] < 6000){
      int VazaoRep1 = au16data[i];
      //Serial.print("Vazão Reprovadas = ");
      char msg[10];
      sprintf(msg, "%d", VazaoRep1);
      client.publish(mqtt_topic2, msg);
      
    }

    
  if (au16data[i] >= 6000 and au16data[i] < 8000){
      int PresApr1 = au16data[i];
      char msg[10];
      sprintf(msg, "%d", PresApr1);
      client.publish(mqtt_topic3, msg);
     
    }

    if (au16data[i] >= 8000 and au16data[i] < 10000){
      int PresRep1 = au16data[i];
      char msg[10];
      sprintf(msg, "%d", PresRep1);
      client.publish(mqtt_topic4, msg);
      
    }

    if (au16data[i] >= 10000 and au16data[i] < 12000){
      int HypApr1 = au16data[i];
      char msg[10];
      sprintf(msg, "%d", HypApr1);
      client.publish(mqtt_topic5, msg);
    
    }
    
    if (au16data[i] >= 12000 and au16data[i] < 14000){
      int HypRep1 = au16data[i];
     char msg[10];
      sprintf(msg, "%d", HypRep1);
      client.publish(mqtt_topic6, msg);
     

    }}

    
    leitura_registro = au16data[i];
    
    ESP.wdtFeed();
  }


  delay(250);
  Serial.flush();
  
  if (!client.connected()) {
    reconnect();
  }




}


void reconnect() {


   if (WiFi.status() != WL_CONNECTED) { // verifica se perdeu conexão com o WiFi
    Serial.println("Perda de conexão WiFi, tentando reconectar...");
    WiFi.reconnect(); // tenta reconectar ao WiFi
    while (WiFi.status() != WL_CONNECTED) {
      delay(2000);
      
      Serial.println("Reconectando ao WiFi...");
    }
    Serial.println("Conectado novamente ao WiFi");
  }

  
  while (!client.connected()) {

    Serial.println("Conectando ao broker MQTT...");
    if (client.connect("ESP8266_Linha3")) {
      Serial.println("Connecting to MQTT broker...");
      client.connect("ESP8266_Linha3");
     
      delay(2000);
    }
  }
}
  
  
