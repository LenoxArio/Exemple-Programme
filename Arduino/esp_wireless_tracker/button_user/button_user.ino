#define BOOT_BUTTON_PIN 0 

void setup() {
  Serial.begin(115200);
  pinMode(BOOT_BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  int buttonState = digitalRead(BOOT_BUTTON_PIN);
  
  if (buttonState == LOW) {
    Serial.println("Button is pressed");
    delay(200);
  }
}
