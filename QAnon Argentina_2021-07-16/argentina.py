from bs4 import BeautifulSoup
import csv


def clean_str(text):
    return text.strip().replace('\n', '')


number_files = 16
elements = []
for file in range(1, number_files):
    with open(f"messages{file}.html") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, "html.parser")
        messages = soup.find_all(class_="message")
        last_from_name = ''
        last_message_time = ''
        for message in messages:
            for body in message.find_all(class_="body"):
                is_forwarded = ''
                if 'forwarded' in body['class']:
                    is_forwarded = True

                message_time = body.find(class_="pull_right date details")
                if message_time is not None:
                    message_time = message_time['title']
                    last_message_time = message_time
                elif 'service' in message['class']:
                    message_time = last_message_time

                message_text = body.find(class_="text")
                if message_text is not None:
                    message_text = clean_str(message_text.text)
                else:
                    description = message.find(class_="description")
                    if description is not None:
                        if 'Not included, change data' in description.text:
                            message_text = 'Media not included'
                    elif 'details' in body['class']:
                        message_text = clean_str(body.text)

                message_from_name = body.find(class_="from_name")
                if message_from_name is not None:
                    message_from_name = clean_str(message_from_name.text)
                    last_from_name = message_from_name
                elif 'joined' in message['class']:
                    message_from_name = last_from_name
                elif 'service' in message['class']:
                    message_from_name = 'Service message'

                reply_to = body.find(class_="reply_to")
                if reply_to is not None:
                    reply_to = clean_str(reply_to.text)

                if message_time is None and \
                   message_text is None and \
                   message_from_name is None and \
                   reply_to is None:
                    continue

                elements.append([
                    message_time,
                    is_forwarded,
                    message_from_name,
                    message_text,
                    reply_to]
                )


with open('mensajes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(elements)