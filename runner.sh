#!/bin/bash

if [ "$(ls -A sqldir)" ]; then

    file_type=""

    venv_name="virtual_office"

    while [[ "$file_type" != "csv" && "$file_type" != "ods" ]]; do
        echo "Welche Art von Datei möchten Sie erhalten? (CSV/ODS)"
        read file_type
        file_type=$(echo "$file_type" | tr '[:upper:]' '[:lower:]') 
    done

    if [ "$file_type" = "ods" ]; then
        if [ -d "$venv_name" ]; then
            source "$venv_name/bin/activate"
            python3 ./python/sql_to_ods.py && echo "Die OpenDocument Spreadsheets wurden erfolgreich erstellt "
            deactivate
        else
            python3 -m venv "$venv_name"
            source "$venv_name/bin/activate"
            python -m ensurepip --upgrade
            pip install --upgrade pip
            pip install pyexcel_ods3 || { echo "Fehler beim Installieren von pyexcel_ods3"; exit 1; }
            python3 ./python/sql_to_ods.py && echo "Die OpenDocument Spreadsheets wurden erfolgreich erstellt "
            deactivate
        fi
          
    elif [ "$file_type" = "csv" ]; then
        python3 ./python/sql_to_csv.py && echo "Die CSV datein wurden erstellt!"
    fi

else
    echo "Der Ordner sqldir ist leer."
fi

