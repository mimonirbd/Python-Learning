import base64
import requests

#Authenticate
user = ''  # the user in which the auth. token is given
pythonapp = ''  # paste here your auth. token
url = '/wp-json/wp/v2'  # the url of the wp access location
token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8'))  # we have to encode the usr and pw
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

wp_title = "This is Titlee"
slug = "this-is"
status = 'draft'
content = '<!-- wp:paragraph --><p>This paragraph</p><!-- /wp:paragraph -->'

post = {'title': wp_title,
           'slug': slug,
           'status': status,
           'content':content,
           'categories':'1',
           'author': '1',
           'format': 'standard',

           }
r = requests.post(url + '/posts', headers=headers, json=post)
print(r)
