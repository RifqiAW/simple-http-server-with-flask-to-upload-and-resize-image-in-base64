from server import app
from flask import json
import base64

class TestServer:
    def test_resize(self):
        with open('tests/sample.jpeg', 'rb') as f:
            im_b64 = base64.b64encode(f.read())
        response = app.test_client().post(
            '/resize_image',
            data={'input_jpeg': im_b64, 'desired_width':'200', 'desired_height':'100'}
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['message'] == "success"