# sysap

Python Bibliothek zum Ansprechen des SysAP von Busch Jaeger Free@Home über das Lokale API.

Ziel ist eine minimalistische Implementierung der Schnittslelle, um virtuelle Geräte in free@home zu registrieren und diese zu benutzen. Ziel ist nicht die komplette Haus-Konfiguration einzulesen und abzubilden. Deswegen sind zunächst auch nur die notwendigen Schnittstellenaufrufe (get und put) implementiert.

Die Informationen zum Login werden in der `.env` Datei eingetragen und vom `dotenv`-modul eingelesen (siehe `dotenv.template`)