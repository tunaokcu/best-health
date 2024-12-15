1)Initial activation
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload

deactivate

2)Subsequent activations
venv\Scripts\activate

uvicorn main:app --reload

deactivate

3)Running the test script(you don't need to start a server instance on the side); seeing no error means all tests pass
venv\Scripts\activate

test.py

deactivate

Credits for the CSS theme goes to https://codepen.io/ayush602/pen/mdQJreW 