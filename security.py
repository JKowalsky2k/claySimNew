import platform
import socket
import re
import uuid
import json
import psutil
from cryptography.fernet import Fernet
import datetime

class Security:
    def __init__(self) -> None:
        self.secret_key = b'-d3XhZsvyvaUTsICb7TcyV-PBTDkOL3sLD8cQ_c4UCE='
        self.signature = 'gAAAAABkHIIEh93RR3YSGt7HXwyC0-duOIkuL3XRYJPGdrtC6LXaY2wa3yZkwkOPCYrsdqLhcovan1yNS7QJb2PlJXj4LagJvlgFp0VQ1fEyfFAGTBDalPKUlg45-9SHcT_GUJADXwMiZEGNAirgqXGptknPP2MpHAmNWwNcOqWVf1iKUhnrWUvDCJztqDMwM7cRLawPsGsMIfm3AyDDngnxDdrz9lEmHrQ_PXcOTWsJ5XDqhh0poQ_rzVnzrH_zpqwdFdKPhJ9Yj58Ax43szJHrW4O3g2W3ynN5sOUzIE2FNpzQ5ZqjSOzQt-le-s5Y1VxjRgs1ncAUXFT1eUwNMxqkr_8MPi2tsw=='
        self.security_engine = Fernet(self.secret_key)
        self.final_date = datetime.date(2023, 4, 14)
        self.last_error = ""
    
    def check_sys_info(self):
        try:
            info={}
            info['platform']=platform.system()
            info['architecture']=platform.machine()
            info['hostname']=socket.gethostname()
            info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            info['processor']=platform.processor()
            info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        except Exception as error:
            self.last_error = "Could not comapre singatures"
            return False 
        return json.dumps(info) == self.security_engine.decrypt(self.signature).decode()
    
    def check_date(self):
        current_time = datetime.datetime.today().date()
        return current_time <= self.final_date

    def check(self):
        return self.check_sys_info() and self.check_date()

    