# proiect-smart-security-system
Sistem de Securitate IoT pentru Casă

Acest proiect reprezintă un sistem de securitate inteligent bazat pe platforma Arduino, conceput pentru a monitoriza mișcarea, prezența gazelor periculoase și starea punctelor de acces (uși/ferestre). Sistemul integrează tehnologii IoT pentru a trimite notificări în timp real direct pe smartphone-ul utilizatorului.
Caracteristici principale

    Monitorizare Multi-Senzor: Detectează mișcarea (PIR), scurgerile de gaze sau fumul (MQ-2) și deschiderea ușilor (senzor magnetic Reed).

    Alerte în Timp Real: Trimite notificări instantanee pe telefon prin intermediul aplicației PushBullet.

    Interfață Locală: Afișează starea senzorilor și a sistemului pe un ecran LCD cu protocol I2C.

    Server Python Personalizat: Include un script Python care preia datele JSON de pe portul serial și gestionează logica de notificare.

    Mod Silențios: Permite activarea/dezactivarea alertelor sonore sau a stării de veghe prin butoane fizice cu algoritm de debouncing.
    
Tehnologii și Componente

    Hardware:

        Arduino UNO.

        Senzor mișcare PIR (Passive Infrared).

        Senzor gaz MQ-2.

        Switch magnetic Reed.

        Display LCD I2C (driver HD44780).

        LED-uri de semnalizare (roșu/verde).

    Software:

        C++/Arduino: Pentru controlul hardware-ului și transmiterea datelor seriale.

        Python 3: Pentru serverul de procesare a datelor și integrarea API-ului PushBullet.

        JSON: Formatul utilizat pentru schimbul de date între Arduino și server.

Arhitectura Sistemului

    Arduino colectează date de la senzori și le ambalează într-un obiect JSON.

    Datele sunt trimise prin Serial (USB) către un calculator la o viteză de 9600 baud.

    Serverul Python parsează JSON-ul și verifică pragurile critice (ex: concentrație gaz > 300 ppm).

    Dacă o condiție de alertă este îndeplinită, este apelat API-ul PushBullet pentru trimiterea notificării.

Probleme Rezolvate (Troubleshooting)

    Librărie LCD: Înlocuirea librăriei standard cu hd44780.h pentru compatibilitatea cu driverul specific.

    Debouncing: Implementarea unui interval de minim 200ms pentru a elimina semnalele false la apăsarea butoanelor.

    Conexiuni Hardware: Conectorizarea senzorului Reed prin lipire (soldering) pentru stabilitatea pe breadboard.
