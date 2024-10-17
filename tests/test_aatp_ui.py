import unittest
from unittest.mock import patch, MagicMock
from api.aatp_ui import app

class TestAatpUi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        # Act
        response = self.app.get('/')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'index.html', response.data)

    @patch('api.aatp_ui.create_schema')
    def test_api_create_schema(self, mock_create_schema):
        # Arrange
        mock_create_schema.return_value = {'schema_id': 'test_schema_id'}
        data = {
            'schema_name': 'test_schema',
            'schema_version': '1.0',
            'attributes': ['attr1', 'attr2']
        }

        # Act
        response = self.app.post('/create-schema', data=data)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test_schema_id', response.data)
        mock_create_schema.assert_called_once_with(
            'test_schema', '1.0', ['attr1', 'attr2'],
            auth_token=unittest.mock.ANY,
            url=unittest.mock.ANY
        )

    # Add more tests for other UI routes...
