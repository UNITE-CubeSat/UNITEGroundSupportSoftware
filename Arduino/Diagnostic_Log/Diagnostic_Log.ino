
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial1.begin(9600);
  Serial2.begin(38400);
  Serial3.begin(38400);
}

char duplexHeader[6];
char duplexPackage[1000];
byte dupPicHeader[6];
char dupPicFileHeader[50];
byte dupPicPackage[1000];

void loop() {
  // put your main code here, to run repeatedly:

  // Diagnostic Logs
  if (Serial1.available()) {

    String diagLog = Serial1.readStringUntil('\n');
    Serial.println(diagLog);
    
  }

  // Pic -> Duplex
  if (Serial2.available()) {
    Serial2.readBytes(dupPicHeader, 6);

    int picMessLength = dupPicHeader[5] - 4;

    Serial2.readBytes(dupPicPackage, picMessLength);

    for (int i = 0; i < 6; i++) {
      Serial.print(dupPicHeader[i], HEX);
      Serial.print(",");
    }
    
    for (int i = 0; i < picMessLength; i++) {
      Serial.print(dupPicPackage[i], HEX);
      Serial.print(",");
    }

    Serial.println();
    Serial.print("Pic -> Duplex");
    Serial.println();

  }

  // Duplex -> PIC
  if (Serial3.available()) {
    Serial3.readBytes(duplexHeader, 6);

    int messageLength = duplexHeader[5] - 4;

    Serial3.readBytes(duplexPackage, messageLength);

    for (int i = 0; i < 6; i++) {
      Serial.print(duplexHeader[i], HEX);
      Serial.print(",");
    }
    
    for (int i = 0; i < messageLength; i++) {
      Serial.print(duplexPackage[i]);
      Serial.print(",");
    }

    Serial.println();
    Serial.print("Duplex -> Pic");
    Serial.println();
  }
}
