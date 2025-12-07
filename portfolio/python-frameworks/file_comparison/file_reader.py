class FixedWidthReader:
    """
    Reader for legacy system fixed-width files (Header, Detail, Trailer).
    Demonstrates manual parsing logic often required in banking/insurance domains.
    """
    
    def __init__(self, file_path, schema):
        """
        schema: list of tuples (field_name, start_index, length)
        start_index is 0-based.
        """
        self.file_path = file_path
        self.schema = schema

    def parse(self):
        parsed_data = []
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    # distinct logic for Header/Trailer could be added here
                    # For demo, assuming all lines follow the schema
                    record = {}
                    for field, start, length in self.schema:
                        val = line[start : start + length].strip()
                        record[field] = val
                    parsed_data.append(record)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            
        return parsed_data

class DelimiterReader:
    """
    Wrapper for CSV/Delimited reading, could extend to use csv module or pandas.
    """
    def __init__(self, file_path, delimiter='|'):
        self.file_path = file_path
        self.delimiter = delimiter

    def parse(self):
        data = []
        with open(self.file_path, 'r') as f:
            headers = f.readline().strip().split(self.delimiter)
            for line in f:
                values = line.strip().split(self.delimiter)
                data.append(dict(zip(headers, values)))
        return data
