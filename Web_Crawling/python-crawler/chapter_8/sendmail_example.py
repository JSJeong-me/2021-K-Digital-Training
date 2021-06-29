import smtplib
from email.message import EmailMessage

FROM = '자신의 메일 주소를 입력해주세요.'

def mail(to, subject, body=None):
    msg = EmailMessage()
    msg['To'] = to
    msg['Subject'] = subject
    msg['From'] = FROM
    if body is None:
        raise ValueError("메일 내용을 입력해주세요.")
    else:
        msg.set_content(body)

    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)

if __name__ == '__main__':
    mail('자신의 메일 주소를 입력해주세요', "메일 제목", "메일 내용")
