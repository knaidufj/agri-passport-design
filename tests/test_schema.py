import unittest
from unittest.mock import patch, MagicMock
from api.schema import create_schema, get_schema

class TestSchema(unittest.TestCase):

    @patch('api.schema.send_api_call')
    def test_create_schema(self, mock_send_api_call):
        # Arrange
        mock_response = {"schema_id": "test_schema_id"}
        mock_send_api_call.return_value = mock_response

        # Act
        result = create_schema("test_schema", "1.0", ["attr1", "attr2"])

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()

    @patch('api.schema.send_api_call')
    def test_get_schema(self, mock_send_api_call):
        # Arrange
        mock_response = {"schema": {"name": "test_schema", "version": "1.0"}}
        mock_send_api_call.return_value = mock_response

        # Act
        result = get_schema("test_schema_id")

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()
