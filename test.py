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
    return resp.status_code >= 200 and resp.status_code < 300

"""
Should get non-2XX(not OK) codes in redirection history, but finally get 2XX OK.
"""
def get_nonexistent(endpoint, id):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}/{id}")

        assert is_OK(response), "Response not okay"

        non_2xx_found = any(not is_OK(resp) for resp in response.history)
        assert non_2xx_found, "No non-2XX status codes found in the redirect history."

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

def get_nonexistent_tests():
    login()

    get_nonexistent_room()
    get_negative_room()
    get_nonexistent_patient()
    get_negative_patient()
    get_nonexistent_admission()
    get_negative_admission()

    logout()

def login():
    data = {
        "email": "email@email.com",
        "password": "password"
    }
    return requests.post(f"{BASE_URL}/auth/login", data)

def logout():
    return requests.get(f"{BASE_URL}/auth/logout")

def get_private_page():
    return requests.get(f"{BASE_URL}/patients/register")

def should_access_private_page_after_login():
    login()
    res = get_private_page()
    assert is_OK(res), "Could not get page even though the user is logged in"
    logout()


def should_not_access_private_page_without_login():
    res = get_private_page()
    assert not is_OK(res), "Could access page without logging in"

def should_not_access_private_page_after_logout():
    login()
    logout()
    res = get_private_page()
    assert not is_OK(res), "Could access page after logging out"

def auth_tests():
    should_access_private_page_after_login()
    should_not_access_private_page_without_login()
    should_not_access_private_page_after_logout()

    
def run_tests():
    get_nonexistent_tests()
    auth_tests()

if __name__ == "__main__":
    print("Starting server...")
    server_process = start_server()

    try:
        print("Running tests...")
        run_tests()
    finally:
        print("Stopping server...")
        stop_server(server_process)
