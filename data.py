from pyscript import Element
from link_data import*
password = Element('Password')
username = Element('Username')
body = Element('body')

def show():
    if len(password.value) >= 10 or len(username.value) >= 10:
        body.element.innerHTML = '<a>home</a>'
    if str(password.value) == 'kls2566' and str(username.value) == 'rd2566':
        body.element.innerHTML = data['Edit']

