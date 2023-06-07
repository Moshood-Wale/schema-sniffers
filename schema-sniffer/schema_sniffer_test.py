import unittest
import json
from main import sniff_schema

class SchemaSnifferTestCase(unittest.TestCase):
    def test_sniff_schema(self):
        input_file = './data/data_1.json'
        output_file = './schema/schema_1.json'
        
        # Run the schema sniffing process
        sniff_schema(input_file, output_file)
        
        # Read the output schema file
        with open(output_file, 'r') as file:
            schema = json.load(file)
        
        # Assert specific attributes and values in the schema
        self.assertIn('battle', schema)
        self.assertIn('name', schema['battle'])
        self.assertEqual(schema['battle']['name']['type'], 'string')
        self.assertEqual(schema['battle']['status']['required'], False)
        self.assertIn('minParticipants', schema['battle']['settings'])
        self.assertEqual(schema['battle']['settings']['minParticipants']['type'], 'integer')
        self.assertIn('archetype', schema['battle']['settings'])
        self.assertIn('name', schema['battle']['settings']['archetype'])
        self.assertEqual(schema['battle']['settings']['archetype']['name']['type'], 'string')
        self.assertIn('iconId', schema['battle']['settings']['archetype'])
        self.assertEqual(schema['battle']['settings']['archetype']['iconId']['type'], 'string')
        self.assertIn('participants', schema['battle'])
        self.assertEqual(schema['battle']['participants']['type'], 'array')
        self.assertIn('ranking', schema['battle']['participants']['items'])
        self.assertEqual(schema['battle']['participants']['items']['ranking']['type'], 'integer')

    def test_sniff_schema_2(self):
        input_file = './data/data_2.json'
        output_file = './schema/schema_2.json'

        # Run the schema sniffing process
        sniff_schema(input_file, output_file)

        # Read the output schema file
        with open(output_file, 'r') as file:
            schema = json.load(file)

        # Assert specific attributes and values in the schema
        self.assertIn('user', schema)
        self.assertEqual(schema['user']['id']['type'], 'string')
        self.assertEqual(schema['user']['nickname']['type'], 'string')
        self.assertEqual(schema['user']['title']['type'], 'string')
        self.assertEqual(schema['user']['accountType']['type'], 'string')
        self.assertEqual(schema['user']['countryCode']['type'], 'string')
        self.assertEqual(schema['user']['orientation']['type'], 'string')

if __name__ == '__main__':
    unittest.main()
