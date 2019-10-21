from imapclient import IMAPClient

HOST = 'imap.vestergade22.dk'
USERNAME = 'pocket@vestergade22.dk'
PASSWORD = 'lemoncurry'
ssl = False

server=IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

select_info = server.select_folder('INBOX')

print(select_info[b'EXISTS'])

messages = server.search(['NOT', 'DELETED'])
print("{0} messages that aren't deleted".format(len(messages)))
unseen=server.search(['NOT', 'SEEN'])
print("{0} unread messages".format(len(unseen)))

response = server.fetch(messages, ['BODY[HEADER.FIELDS (TO)]'])
for msgid, data in response.items():
    print ("ID {0}  body {1}".format(msgid, data[b'BODY[HEADER.FIELDS (TO)]']))