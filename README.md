# SQLTabExtract

## CLI Tool
Extract Table data from SQL Script files into .csv or .ods files

## Usage
1. Clone the Repo
'''bash
git clone 
'''
2. Now put a subdir with all SQL Script files into sqldir/
3. Start the runner.sh

### CSV
for every SQL script file in sqldir/subdir/ a .csv file of the same name is generated in csvs

### ODS
For every subdir in sqldir a .ods will be generated in ods_files.
For every file inside said subdir a sheet with the same name will be generated.
