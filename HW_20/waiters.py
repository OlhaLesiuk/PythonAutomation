import time


def wait_until(predicate: callable, message: str, timeout=10, poll_frequency=0.1):
    start = time.time()
    while True:
        try:
            result = predicate()
            if result:
                break
        except:
            if time.time() - start > timeout:
                raise TimeoutError(message)
            time.sleep(poll_frequency)
        if time.time() - start > timeout:
            raise TimeoutError(message)
        time.sleep(poll_frequency)
