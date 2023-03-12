import os
import csv

print("Please write out the line after which the table beginns")
table_beginn = input()


print("Please write out the line at which the table ends")
table_end = input()

# Pfad zum Hauptordner
file_dir = 'sqldir/'

# Schleife durch alle Dateien und Ordner im Hauptordner
for subdir, dirs, files in os.walk(file_dir):
    for file in files:
        # Überprüfen, ob es sich um eine SQL-Datei handelt
        if file.endswith('.sql'):
            # Pfad zur SQL-Datei und zum Ordner, in dem das CSV gespeichert werden soll
            sql_file_path = os.path.join(subdir, file)
            csv_dir_path = os.path.join('csvs/', os.path.basename(subdir))
            
            # Überprüfen, ob der CSV-Ordner bereits vorhanden ist, und ihn andernfalls erstellen
            os.makedirs(csv_dir_path, exist_ok=True)
                
            # Pfad zur CSV-Datei
            csv_file_path = os.path.join(csv_dir_path, os.path.splitext(file)[0] + '.csv')
            
            # Öffnen der SQL- und CSV-Dateien und Schreiben der Daten
            with open(csv_file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(['Column Name', 'Data Type', 'Length', 'must be present','comment','example'])

                with open(sql_file_path, 'r') as sqlfile:
                    create_table = False
                    for line in sqlfile:
                        if table_beginn in line:
                            create_table = True
                            continue
                        if create_table:
                            if table_end in line:
                                create_table = False
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
                            writer.writerow([column_name, data_type, length, nullable])
            print(f'Die CSV-Datei für {file} wurde erfolgreich erstellt.')
