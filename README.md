# E500 Multimedia System

Multimedia system featuring integration with CAN bus, MQTT, Flutter, and Node-RED.

## 📌 Objective
To develop a multimedia system featuring:
- CAN bus integration (reading RPM, speed, steering angle, etc.).
- 360° cameras with overlay.
- TPMS (Tire Pressure Monitoring System).
- GPS and navigation.
- AM/FM radio.
- Voice control.
- Automation via MQTT/Node-RED.

## 🛠️ Technologies
| Area          | Technologies                         |
|---------------|--------------------------------------|
| **Frontend**  | Flutter (Dart)                       |
| **Backend**   | Python, MQTT (Mosquitto), Docker     |
| **Automation**| Node-RED                             |
| **Firmware**  | ESP32 (MicroPython/C++)              |
| **Hardware**  | MCP2515, OBD-II, AHD Cameras         | 

## 📂 Project Structure
```
e500-multimidia/
├── docs/               # Documentation
│   ├── canbus/         # CAN mapping (spreadsheet + DBC)
│   ├── hardware/       # Schematics, pinouts, BOM
│   └── software/       # Backend/frontend architecture
├── src/
│   ├── backend/        # Python services (MQTT, CAN, GPS)
│   ├── frontend/       # Flutter (UI)
│   ├── firmware/       # ESP32 code
│   └── node-red/       # Node-RED flows
├── hardware/           # PCB and wiring files
└── tools/              # Helper scripts
```

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/danielzanatta/can_multimedia.git
   ```
2. Set up the environment:
   - [Backend (Python + MQTT)](docs/software/backend.md)
   - [Frontend (Flutter)](docs/software/frontend.md)
   - [Firmware (ESP32)](docs/firmware/esp32.md)

## 📜 License
This project is licensed under the [MIT License](LICENSE).
