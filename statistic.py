import smtplib

try:
    f = open("statistic.txt")
    g = f.read()
    f.close()
    g1 = str(g)
except Exception:
    g1 = "Error File!!!"
finally:
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login('fmdsmkeii45enredfg45tgededs@gmail.com', '23hdfskjdfui43hj')
    server.sendmail('fmdsmkeii45enredfg45tgededs@gmail.com', 'nicholas.romanets@gmail.com', g1)
    print(g1)
    server.close()