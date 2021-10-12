import sys
import flask


FLASK_VERSION = "2.0.1"
PYTHON_VERSION = "3.9.5"


flask_ver = flask.__version__
error_msg = f"Unexpected Flask version. Expected {FLASK_VERSION}, got {flask_ver}."
assert flask_ver == FLASK_VERSION, error_msg

ver = sys.version_info
python_ver = ".".join([str(i) for i in (ver.major, ver.minor, ver.micro)])
error_msg = f"Unexpected Python version. Expected at least {PYTHON_VERSION}, got {python_ver}."
assert python_ver >= PYTHON_VERSION, error_msg

print("Checks passed!")