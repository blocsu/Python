import requests
url = 'https://the-one-api.dev/v2/book'
res = requests.get(url).json()
_id = None
for x in res['docs']:
    if x['name'] == 'The Two Towers':
        _id = x['_id']
        break
url = f'https://the-one-api.dev/v2/book/{_id}/chapter'
res = requests.get(url).json()
chapter_name = None
for x in res['docs']:
    if x['_id'] == '6091b6d6d58360f988133ba7':
        chapter_name = x['chapterName']
        break
print(len(res['docs']), chapter_name)