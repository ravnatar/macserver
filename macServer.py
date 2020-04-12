#!/usr/bin/python
import sys
from flask import Flask

app = Flask(__name__)

#database of MAC address & info
#in real world, this would be an LDAP lookup

mac_dict = {"D7:A3:E7:FD:58:F5" : "ABC Company", "2B:5C:8D:DC:3C:38" : "XYZ Company"}

@app.route('/macServer/<string:macAddress>', methods=['GET'])
def get_macInfo(macAddress):
  print("looking up info for macAddress : " + macAddress)
  return(mac_dict.get(macAddress, "Not Found !"))


if __name__ == '__main__':
  app.run(ssl_context=('cert.pem', 'key.pem'), host='0.0.0.0')
