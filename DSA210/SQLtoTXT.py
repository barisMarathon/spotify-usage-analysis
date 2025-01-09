import re

def extract_values_from_sql(sql_content):
    # This regex will match the values inside the INSERT INTO statements
    pattern = re.compile(r"INSERT INTO .*? VALUES\s*\((.*?)(?<!\\)\);", re.IGNORECASE | re.DOTALL)
    matches = pattern.findall(sql_content)
    values = []
    for match in matches:
        # Extract the date-time part from each value
        date_time_matches = re.findall(r"'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'", match)
        values.extend(date_time_matches)
    return values

def convert_sql_to_txt(sql_file_path, txt_file_path):
    try:
        with open(sql_file_path, 'r') as sql_file:
            sql_content = sql_file.read()
        
        values = extract_values_from_sql(sql_content)
        
        with open(txt_file_path, 'w') as txt_file:
            for value in values:
                txt_file.write(value + '\n')
        
        print(f"Converted {sql_file_path} to {txt_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    sql_files = [
        ("D:\\Downloads\\SQL for DSA\\car.sql", "D:\\Downloads\\SQL for DSA\\car.txt"),
        ("D:\\Downloads\\SQL for DSA\\spotify.sql", "D:\\Downloads\\SQL for DSA\\spotify.txt")
    ]
    
    for sql_file, txt_file in sql_files:
        convert_sql_to_txt(sql_file, txt_file)

if __name__ == "__main__":
    main()
