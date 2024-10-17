import unittest
from unittest.mock import patch, MagicMock
from api.aatp_cli import main

class TestAatpCli(unittest.TestCase):

    @patch('api.aatp_cli.argparse.ArgumentParser.parse_args')
    @patch('api.aatp_cli.create_schema')
    def test_main_create_schema(self, mock_create_schema, mock_parse_args):
        # Arrange
        mock_args = MagicMock()
        mock_args.action = 'create-schema'
        mock_args.schema_name = 'test_schema'
        mock_args.schema_version = '1.0'
        mock_args.attributes = ['attr1', 'attr2']
        mock_parse_args.return_value = mock_args

        # Act
        main()

        # Assert
        mock_create_schema.assert_called_once_with(
            'test_schema', '1.0', ['attr1', 'attr2'],
            auth_token=mock_args.auth_token,
            url=mock_args.url
        )

    @patch('api.aatp_cli.argparse.ArgumentParser.parse_args')
    @patch('api.aatp_cli.get_schema')
    def test_main_get_schema(self, mock_get_schema, mock_parse_args):
        # Arrange
        mock_args = MagicMock()
        mock_args.action = 'get-schema'
        mock_args.schema_id = 'test_schema_id'
        mock_parse_args.return_value = mock_args

        # Act
        main()

        # Assert
        mock_get_schema.assert_called_once_with(
            'test_schema_id',
            auth_token=mock_args.auth_token,
            url=mock_args.url
        )

    # Add more tests for other CLI actions...
