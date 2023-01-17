Wichtig für das Skript ist dass pyodbc installiert ist.
Dies geht mit folgendem Command:
pip install pyodbc

Auch soll das Skript über PowerShell mit dem Administrator gestartet werden. 

#Aufgabestellung
Es soll eine Eingabe des Datenbankservers/Instanz erfolgen können, wo anschliessend eine Test-Datenbank mit mehreren Test-Tabellen (inkl. Random-Inhalt) erstellt wird.
Jede zweite Sekunde soll ein Verbindungsaufbau stattfinden und ein Datensatz in einer Tabelle geschrieben werden. (Verbindungsaufbau – Schreiben - Verbindungsabbau)
Jede zweite Sekunde soll ein Verbindungsaufbau stattfinden und ein Datensatz in einer Tabelle gelöscht werden. (Verbindungsaufbau – Löschen - Verbindungsabbau)
Sekunde 1: Verbindungsaufbau – Schreiben – Verbindungsabbau
Sekunde 2: Verbindungsaufbau – Löschen – Verbindungsabbau
Sekunde 3 Verbindungsaufbau – Schreiben – Verbindungsabbau
Sekunde 4 Verbindungsaufbau – Löschen – Verbindungsabbau
Sekunde 5 …
In einer Ausgabe soll immer gezeigt werden, ob der Verbindungsaufbau, Schreiben/Löschen, Verbindungsabbau erfolgreich durchgeführt werden konnte.
Sollte der Verbindungsaufbau fehlschlagen, soll er jede Sekunde wiederholt werden, bis es wieder funktioniert.