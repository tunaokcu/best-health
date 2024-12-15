import subprocess
import time
import requests

BASE_URL = "http://127.0.0.1:8000"


def start_server():
    process = subprocess.Popen(
        ["uvicorn", "main:app", "--reload"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    #time.sleep(10)  # Wait a few seconds to ensure the server is fully up
    return process

def stop_server(process):
    process.terminate()
    process.wait()

def sample_test():    
    try:
        # Example GET request
        response = requests.get(f"{BASE_URL}/example-endpoint")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

        # Example POST request
        payload = {"key": "value"}
        response = requests.post(f"{BASE_URL}/example-endpoint", json=payload)
        assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
    except Exception as e:
        print(f"Test failed: {e}")


def is_OK(resp):
    return resp.status_code >= 200 or resp.status_code < 300

"""
Should get non-2XX(not OK) codes in redirection history, but finally get 2XX OK.
"""
def get_nonexistent(endpoint, id):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}/{id}")

        assert is_OK(response)

        non_2xx_found = any(not is_OK(resp) for resp in response.history)
        assert not non_2xx_found, "No non-2XX status codes found in the redirect history."

    except Exception as e:
        print(f"Test failed: {e}") 

def get_negative_room():
    return get_nonexistent("rooms", -10)

def get_negative_patient():
    return get_nonexistent("patients", -10)

def get_negative_admission():
    return get_nonexistent("admissions", -100)

def get_nonexistent_room():
    return get_nonexistent("rooms", 10)

def get_nonexistent_patient():
    return get_nonexistent("patients", 100)

def get_nonexistent_admission():
    return get_nonexistent("admissions", 100)

def run_tests():
    get_nonexistent_room()
    get_negative_room()
    get_nonexistent_patient()
    get_negative_patient()
    get_nonexistent_admission()
    get_negative_admission()

if __name__ == "__main__":
    print("Starting server...")
    server_process = start_server()

    try:
        print("Running tests...")
        run_tests()
    finally:
        print("Stopping server...")
        stop_server(server_process)
