void setup() {
  Serial.begin(38400);
  Serial1.begin(38400);
  Serial2.begin(38400);
  Serial3.begin(38400);

}

byte simplexPackage[43];
byte picPackage[39];
char duplexHeader[6];
char duplexPackage[1000];
byte dupPicHeader[6];
char dupPicFileHeader[50];
byte dupPicPackage[1000];
void loop() {

  // Simplex
  if (Serial2.available()) {
    Serial2.readBytes(simplexPackage, 43);

    for (int i = 0; i < 42; i++) {
      Serial.print(simplexPackage[i], HEX);
      Serial.print(",");
    }
    Serial.println();
    Serial.print("Simplex -> Pic");
    Serial.println();
  }


  // PIC - EPS
  if (Serial1.available()) {
    Serial1.readBytes(picPackage, 39);

    Serial.println();
    
    for (int i = 0; i < 39; i++) {
      Serial.print(picPackage[i], HEX);
      Serial.print(",");
    }
    Serial.println();

    Serial.print("Pic -> EPS");
    Serial.println();

  }

  // MOVED TO DIAG LOG ARDUINO SCRIPT
  /*
  // Duplex
  if (Serial2.available()) {
    Serial2.readBytes(duplexHeader, 6);

    int messageLength = duplexHeader[5] - 4;

    Serial2.readBytes(duplexPackage, messageLength);

    for (int i = 0; i < 6; i++) {
      Serial.print(duplexHeader[i], HEX);
      Serial.print(", ");
    }
    
    for (int i = 0; i < messageLength; i++) {
      Serial.print(duplexPackage[i]);
      Serial.print(", ");
    }

    Serial.print("Duplex");
    Serial.println();
  }


  // PIC - Duplex
  if (Serial3.available()) {
    Serial3.readBytes(dupPicHeader, 6);

    int picMessLength = dupPicHeader[5] - 4;

    Serial3.readBytes(dupPicPackage, picMessLength);

    for (int i = 0; i < 6; i++) {
      Serial.print(dupPicHeader[i], HEX);
      Serial.print(", ");
    }
    
    for (int i = 0; i < picMessLength; i++) {
      Serial.print(dupPicPackage[i], HEX);
      Serial.print(", ");
    }
    
    Serial.print("PIC - Duplex");
    Serial.println();

  }*/
}

