#include "HT_st7735.h"
#include "Arduino.h"
HT_st7735 st7735;


void setup()
{  
    Serial.begin(115200);
    st7735.st7735_init();
    Serial.printf("Ready!\r\n");

    st7735.st7735_fill_screen(ST7735_BLACK);
    st7735.st7735_write_str(0, 0, "ESP Connected", Font_7x10, ST7735_WHITE, ST7735_BLACK);
    delay(3000);
    st7735.st7735_fill_screen(ST7735_BLACK);
}

void loop() {
    

    uint16_t customColor = color565(255, 189, 0);

    st7735.st7735_write_str(0, 0, "ESP Info", Font_11x18, customColor, ST7735_BLACK);
    delay(1000);
    st7735.st7735_write_str(0, 0, "ESP Info", Font_11x18, ST7735_GREEN, ST7735_BLACK);
    delay(1000);
}

uint16_t color565(uint8_t r, uint8_t g, uint8_t b) {
    return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3);
}