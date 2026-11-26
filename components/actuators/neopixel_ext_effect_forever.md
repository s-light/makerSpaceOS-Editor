---
id: neopixel_ext_effect_forever
blockCategory: Lichter
component: neopixel_strip
subCategory: "Streifen"
label: "✨ Streifen-Effekt endlos"
label_en: "✨ Strip effect forever"
colour: "#EC4899"
tooltip: "Startet einen LED-Effekt, der läuft, bis er gestoppt wird. Das Programm läuft dabei weiter."
tooltip_en: "Starts an LED effect that runs until it is stopped. The program keeps running meanwhile."
blockType: statement
inline: false
inputs:
  - label: "endlos"
    label_en: "forever"
    name: EFFECT
    fieldType: options_dropdown
    options:
      - label: "Komet"
        label_en: "Comet"
        value: "komet"
      - label: "Lauflicht"
        label_en: "Chase"
        value: "lauflicht"
      - label: "Blinken"
        label_en: "Blink"
        value: "blinken"
      - label: "Pulsieren"
        label_en: "Pulse"
        value: "pulsieren"
      - label: "Regenbogen"
        label_en: "Rainbow"
        value: "regenbogen"
  - label: "Port:"
    label_en: "port:"
    name: PORT
    fieldType: grove_dropdown
    groveRole: strip
  - label: "Farbe:"
    label_en: "colour:"
    name: COLOR
    fieldType: colour_picker
    default: "#ff0000"
    newRow: true
  - label: "Tempo:"
    label_en: "speed:"
    name: SPEED
    fieldType: options_dropdown
    options:
      - label: "schnell"
        label_en: "fast"
        value: "3"
      - label: "sehr schnell"
        label_en: "very fast"
        value: "4"
      - label: "mittel"
        label_en: "medium"
        value: "2"
      - label: "langsam"
        label_en: "slow"
        value: "1"
valueInputs:
  - name: COUNT
    label: "LEDs gesamt"
    label_en: "total LEDs"
    check: Number
    defaultValue: 20
hardware:
  commonName: "NeoPixel-Streifen (extern) / WS2812B"
  verbrauch3j: 0
  kitStandard: false
legacyGenerator: true
---

# LED-Streifen – Effekt endlos

Startet einen Effekt, der immer weiter läuft – bis „Effekt stoppen“, ein anderer Effekt oder ein anderer Streifen-Block am selben Port kommt.
Der Block wartet nicht. Er darf auch in FÜR IMMER stehen.

<!-- lang:en -->

# LED strip – effect forever

Starts an effect that keeps running – until “stop effect”, another effect or another strip block on the same port.
The block does not wait. It may also be placed inside FOREVER.
