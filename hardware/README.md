# Hardware for Fair Talk

This repo contains the physical hardware specifications for the Fair Talk project. 

The current Fair Talk system consists of two main components:

 * cell phones
 * boost stations

The boost stations contain a couple main components:

 * boost stations
   * power
   * Wifi
   * LoRa
   * case

Each component of the boost stations are made of sub-components:

 * boost stations
   * power
     * solar panel
     * solar charger/battery charger
     * LiPo Battery
     * wall plug    
   * Wifi
     * ESP8266 Thing Board
     * uFL antenna adapter
     * WiFi
   * LoRa
     * Feather M0 RFM95
     * uFL SMD antenna connector
     * uFL antenna adapter
     * LoRa antenna
   * case
     * case lid
     * case base
     * attachment hardware

## Communication Scheme

The basic Fair Talk communication scheme is:

cell phone --> ESP8266 --> LoRa --> LoRa --> ESP8266 --> cell phone
