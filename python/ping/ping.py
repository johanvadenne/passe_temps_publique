import os
hostname = ""
response = os.system("ping -c 1 " + hostname)
if response == 0:
    pingstatus = "Network Active"
else:
    pingstatus = "Network Error"

print(pingstatus)