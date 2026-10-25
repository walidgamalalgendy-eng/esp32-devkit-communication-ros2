#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "Linardos";
const char* password = "xdnk5448";
const int localPort = 8888;

WiFiUDP udp;
char packetBuffer[255];

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("\nConnected! IP Address: ");
  Serial.println(WiFi.localIP());
  
  udp.begin(localPort);
}

void loop() {
  int packetSize = udp.parsePacket();
  if (packetSize) {
    int len = udp.read(packetBuffer, 255);
    if (len > 0) packetBuffer[len] = 0;
    
    String data = String(packetBuffer);

    int commaIndex = data.indexOf(',');
    if (commaIndex != -1) {
      float num1 = data.substring(0, commaIndex).toFloat();
      float num2 = data.substring(commaIndex + 1).toFloat();
      float result = num1 + num2;
      

      udp.beginPacket(udp.remoteIP(), udp.remotePort());
      udp.print(String(result, 2));
      udp.endPacket();
    }
  }
}