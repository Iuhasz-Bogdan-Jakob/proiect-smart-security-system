import serial  # Pentru comunicare serială
import json    # Pentru manipularea datelor JSON
from pushbullet import Pushbullet  # Pentru trimiterea notificărilor

# Configurare port serial
serial_port = "COM5"  # Înlocuiește cu portul pe care este conectat Arduino (ex.: COM3 pe Windows, /dev/ttyUSB0 pe Linux)
baud_rate = 9600      # Viteza de comunicare serială
pb_api_key = "o.O18gn1ycb4dK826dtoHoa9jBWVBU7QtR"  # Înlocuiește cu API Key-ul tău Pushbullet

# Inițializare Pushbullet
pb = Pushbullet(pb_api_key)

# Conectare la portul serial
try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Conectat la {serial_port} cu baud rate {baud_rate}")
except serial.SerialException as e:
    print(f"Eroare: Nu se poate conecta la {serial_port}")
    exit()

# Variabile pentru starea sistemului
system_active = False
last_system_active = None  # Păstrăm ultima stare a sistemului

# Funcție pentru trimiterea notificărilor
def send_notification(title, message):
    try:
        pb.push_note(title, message)
        print(f"Notificare trimisă: {title} - {message}")
    except Exception as e:
        print(f"Eroare la trimiterea notificării: {e}")

# Ascultare continuă a datelor de la Arduino
try:
    while True:
        if ser.in_waiting > 0:  # Verificăm dacă sunt date disponibile în buffer
            line = ser.readline().decode("utf-8").strip()  # Citim linia și eliminăm spațiile
            print(f"Date primite: {line}")
            
            try:
                # Convertim datele JSON primite în dicționar Python
                data = json.loads(line)
                
                # Extragem stările senzorilor și starea sistemului
                pir_state = data.get("pir", 0)
                gas_state = data.get("gas", 0)
                reed_state = data.get("reed", 0)
                status = data.get("status", "").lower()  # Preluăm statusul general

                # Verificăm dacă s-a schimbat starea sistemului (activat/dezactivat)
                if status == "sistem activat" and system_active != True:
                    system_active = True
                    send_notification("Status Sistem", "Sistemul a fost activat.")
                elif status == "sistem dezactivat" and system_active != False:
                    system_active = False
                    send_notification("Status Sistem", "Sistemul a fost dezactivat.")

                # Gestionarea notificărilor senzorilor
                if system_active:
                    if reed_state == 1:  # Ușa este deschisă
                        send_notification("Alertă Sistem", "Ușa a fost deschisă!")
                    
                    if pir_state == 1:  # Mișcare detectată
                        send_notification("Alertă Sistem", "Mișcare detectată!")
                    
                    if gas_state > 300:  # Fum detectat
                        send_notification("Alertă Sistem", "Fum detectat!")
                    
                    elif gas_state > 200:  # Gaz detectat
                        send_notification("Alertă Sistem", "Gaz detectat!")

            except json.JSONDecodeError:
                print(f"Eroare la parsarea JSON: {line}")
except KeyboardInterrupt:
    print("Oprire manuală...")
except Exception as e:
    print(f"Eroare: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
    print("Conexiunea serială a fost închisă.")
