# Schema Sniffer

This program reads a JSON file, sniffs its schema, and generates an output file containing the schema information. It follows specific rules for data types and attribute padding.

## Requirements

- Python 3.6 or above

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/schema-sniffer.git
   cd schema-sniffer

2. Usage
   Place your input JSON file in the data directory. Ensure that the JSON file follows the required structure and contains the necessary data.
   
   Open the main.py file and modify the file paths for input and output as per your requirements:
   input_file = './data/input.json'
   output_file = './schema/output.json'

3. Run the schema sniffing program:
   python main.py

4. After execution, the output schema will be generated and saved in the specified output file path.

5. Running Tests
   To run the unit tests for the schema sniffing program, execute the following command:
   python -m unittest schema_sniffer_test.py
   
   The test results will be displayed in the console.
