import os
import pyexcel_ods3

# Ordner mit SQL-Dateien und Ordner für ODS-Dateien definieren
sql_dir = 'sqldir/'
ods_dir = 'ods_files/'

# Liste aller Unterordner im SQL-Ordner abrufen
subdirs = [f for f in os.listdir(sql_dir) if os.path.isdir(os.path.join(sql_dir, f))]

# Für jeden Unterordner ein separates ODS-Datei erstellen
for subdir in subdirs:
    # Den Namen des ODS-Datei auf den Namen des Unterordners setzen
    ods_file_name = os.path.join(ods_dir, subdir + '.ods')
    data = {}
    header = ['Attribut', 'Datatype', 'Len', 'Must Have', 'Comment', 'Example']

    # Alle SQL-Dateien im aktuellen Unterordner abrufen
    subdir_path = os.path.join(sql_dir, subdir)
    files = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]

    # Daten aus den SQL-Dateien lesen und im entsprechenden Sheet speichern
    for file in files:
        sql_file_name = os.path.join(subdir_path, file)
        sheet_name = os.path.splitext(file)[0]

        with open(sql_file_name, 'r') as sqlfile:
            for line in sqlfile:
                if 'CREATE TABLE' in line:
                    break
            for line in sqlfile:
                if 'ON [PRIMARY]' in line:
                    break
                column_name = line.split('[')[1].split(']')[0]
                data_type = line.split('[')[2].split(']')[0]
                if '(' in line:
                    length = line.split('(')[1].split(')')[0]
                else:
                    length = ''
                if 'NOT NULL' in line:
                    nullable = ' '
                else:
                    nullable = 'x'
                if data_type == "nvarchar":
                    data_type = "string"

                if sheet_name not in data:
                    data[sheet_name] = []

                data[sheet_name].append([column_name, data_type, length, nullable])

        # Header-Daten in das Sheet einfügen
        data[sheet_name].insert(0, header)

    # Daten in das ODS-Datei schreiben
    pyexcel_ods3.save_data(ods_file_name, data)
