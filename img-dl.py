import csv
import requests
import shutil
from random import sample

f = open(r'final file.csv', 'r', encoding = 'utf8')
reader = csv.reader(f)
dicts = {}

i = 1
for row in reader:
    dicts[i] = {'image_one': row[11], 'name': row[12], 'post_url': row[17]
                }
    i = i + 1
f.close()

def image_download(url, filename):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'referer': 'https://google.com/'}
    resp = requests.get(url, stream = True, headers = headers)
    local_file = open('images/' + filename + '.jpg', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    del resp


def append_list_as_row(filename, list_of_element):
    with open(filename, 'a+', newline = "", encoding = 'utf8') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(list_of_element)


j = 2
while j <= len(dicts):
    current_dic = dicts[j]
    image_name = sample([
        current_dic['name'].replace(' ', '-'),
        current_dic['name'].replace(' ', '-') + '-image.jpg',
    ], 1)

    new_dict = {
        'name': current_dic['name'],
        'image_one1': current_dic['image_one'],
        'first_name': image_name[0],
        'url': current_dic['post_url'],
    }
    value_list = list(new_dict.values())

    try:
        image_download(new_dict['image_one1'], 'name')
        append_list_as_row('images_success.csv', value_list)
        print(j, '--------- downloaded successfully.')
    except:
        append_list_as_row('image_error.csv', value_list)
        print(j, '--------- download failed.')
    # #
    # test_url = 'https://i.imgur.com/BWaFpCE.jpeg'
    # filename = value_list[0]
    # image_download(test_url, filename)

    j = j + 1
