import logging

def test_example():
    logging.info("这是一条日志信息")
    print("这是一条普通的打印,不应该被记录到日志中")
    assert True