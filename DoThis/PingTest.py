import time, re, random
from subprocess import check_output


hostname = "4.2.2.2"

ran = random.randrange(1000)
while True:
    out = check_output(["ping", "-n", "1",hostname]).decode('utf-8')
    x = re.search('[0-9]+ms', out)
    y = x.group(0)
    print(y)

    z = (time.strftime("%d/%m/%Y at %H:%M") + " Ping:" + y + "\n")

    with open("ping_record.txt","a") as b:
        b.write(z)

    time.sleep(1)

# " + str(ran) + " use this if you want to generate a random name for the text file, pretty pointless
