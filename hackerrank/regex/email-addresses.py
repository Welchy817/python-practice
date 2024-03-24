# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import email.utils

N = int(input())
valid_emails = []

for emails in range(N):
    email_addr = email.utils.parseaddr(input())
    if re.search(r"(^[a-zA-Z][a-zA-Z0-9\-\_\.]+[@][a-zA-Z]+\.[a-zA-Z]{0,3}$)", email_addr[1]):
        print(email.utils.formataddr(email_addr))