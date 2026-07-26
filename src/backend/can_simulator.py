import can
import time
import random

def simulate_can_bus():
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    while True:
        # Simular RPM (CAN ID 0x123)
        rpm = random.randint(800, 6000)
        rpm_msg = can.Message(
            arbitration_id=0x123,
            data=[(rpm >> 8) & 0xFF, rpm & 0xFF],  # Converte RPM para 2 bytes
            is_extended_id=False
        )
        bus.send(rpm_msg)
        print(f"Sent RPM: {rpm}")

        # Simular velocidade (CAN ID 0x456)
        speed = random.randint(0, 200)
        speed_msg = can.Message(
            arbitration_id=0x456,
            data=[speed],
            is_extended_id=False
        )
        bus.send(speed_msg)
        print(f"Sent Speed: {speed} km/h")

        time.sleep(1)

if __name__ == "__main__":
    simulate_can_bus()
