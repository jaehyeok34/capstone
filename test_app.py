import os
import tempfile
import shutil
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.uploads_dir = os.path.join(os.getcwd(), 'uploads')

        # Remove uploads folder if exists to ensure a clean test environment.
        if os.path.exists(self.uploads_dir):
            shutil.rmtree(self.uploads_dir)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello world')

    def test_pseudonymize_csv_missing_filePath(self):
        response = self.client.post('/pseudonymize/csv', json={})
        self.assertEqual(response.status_code, 400)

        data = response.get_json()
        self.assertIn('error', data)
        self.assertIn('filePath', data['error'])

    def test_pseudonymize_scv_success(self):
        response = self.client.post('/pseudonymize/csv', json={'filePaths': ['/Users/jaehyeok34/Documents/uploads/1740319416231-datas.csv']})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()