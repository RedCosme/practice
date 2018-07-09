import requests
import random
def verity_phone(phone):
    url = "http://game.i-h5.cn/ljd_game/Mar_carbj2/api.php?a=verify"
    data = {"number": phone}
    ret = None
    try:
        ret = requests.post(url, data=data)
    except Exception as e:
        print e

    if ret.status_code != 200:
        return ret.text
    return ret.json()

def createPhone():
    prelist=["130","131","132","133","134","135","136","137","138","139",
             "147","150","151","152","153","155","156","157","158","159","186","187","188"]
    return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

if __name__ == "__main__":
    print "begin"
    for i in xrange(100000):
        phone = createPhone()
        ret = verity_phone(phone)
        if ret and ret["data"] != "":
            print phone
            print ret
            break
    print "end"