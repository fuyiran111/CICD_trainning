from first_page import app
import logging

def test_first_page():
    logging.info("这是一条日志信息")
    print("这是一条firstpagetest的打印")
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello world' in response.data
        assert b'This is my first page' in response.data
