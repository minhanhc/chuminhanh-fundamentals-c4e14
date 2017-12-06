from gmail import GMail, Message
from random import choice
from datetime import datetime



html_template = ['''<p>Em ch&agrave;o c&ocirc;</p>
<p>Em cần nghỉ học. Em bị {{sickness}} .Em sẽ học b&agrave;i v&agrave; l&agrave;m b&agrave;i đầy đủ</p>
<p>Em c&aacute;m ơn c&ocirc;</p>''', '''<p>Em ch&agrave;o c&ocirc;</p>
<p>Em l&agrave; Minh Anh. h&ocirc;m nay em thấy kh&ocirc;ng khỏe.Em bị {{sickness}} c&ocirc; cho em nghỉ học nh&eacute;. Thanks c&ocirc;. Y&ecirc;u c&ocirc; nhiều</p>
<p>Học sinh của c&ocirc;</p>''','''<p>Hello Boss</p>
<p>My grandma has just passed away, and I'm afraid that I could not go to work for a few days. So can I get the leave?</p>
<p>Thanks sir</p>''']

html_reason = ['<p>ỉa chảy</p>', '<p>ốm</p>', '<p>đau ch&acirc;n</p>']
sickness = choice(html_reason)
html_content = '''<p>Em ch&agrave;o c&ocirc;</p>
<p>Em cần nghỉ học. Em bị {{sickness}}. Em sẽ học b&agrave;i v&agrave; l&agrave;m b&agrave;i đầy đủ</p>
<p>Em c&aacute;m ơn c&ocirc;</p>'''.replace("{{sickness}}", sickness)

while True:
    now = datetime.now()
    if now.hour == 7:
        if now.minute == 00:
            gmail = GMail('c4e14minhanhc@gmail.com','aslongasyouloveme')
            msg = Message('đơn xin nghỉ', to = 'hoangc256@gmail.com', html = html_content)
            gmail.send(msg)
            break
