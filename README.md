# SQLTabExtract

## CLI Tool

SQLTabExtract is a command-line interface (CLI) tool that extracts table data from SQL script files into .csv or .ods files.

## Usage

1. To get started, clone the repository by running the following command:

```
git clone <https://github.com/JanRipken/SQLTabExtract.git>
```

2. Next, put a subdirectory with all SQL script files into the `sqldir/` directory.
3. Start the `runner.sh` script.

### CSV

For each SQL script file in the `sqldir/subdir/` directory, a corresponding .csv file is generated in the `csvs` directory.

### ODS

For each subdirectory in `sqldir/`, an .ods file is generated in the `ods_files` directory. For each file inside said subdirectory, a sheet with the same name is generated.
