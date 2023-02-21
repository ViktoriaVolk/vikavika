import requests

api_url = 'http://localhost:8000'

def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12)
def test_numbers_3_3(self):
        self.assertEqual(3 * 4, 12)
def test_numbers_3_2(self):
        self.assertEqual(3 * 4, 12)

class TestDocuments(self):
    def test_get_empty_docs():
        response = requests.get(f'{api_url}/v1/docs')
        assert response.status_code == 200
        assert len(response.json()) == 0
