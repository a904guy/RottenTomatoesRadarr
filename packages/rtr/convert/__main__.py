import requests
from parsel import Selector
import json

def main(args):

    # Ghetto Validation
    if(args['http']['path'] == ""):
        return {
            'headers': {
                'content-type': 'application/json'
            },
            'body': json.dumps({
                'error': "Copy the URL slug from your want to see list and append it to this url. Example: /user/id/[uuid]/wts".format(args['http']['path']),
                'success': False
            })
        }

    if('/user/id/' not in args['http']['path'] or '/wts' not in args['http']['path']):
        return {
            'headers': {
                'content-type': 'application/json'
            },
            'body': json.dumps({
                'error': "URL Path ({}) doesn't appear to be a user's Want To See list. Example: /user/id/[uuid]/wts".format(args['http']['path']),
                'success': False
            })
        }

    list = []

    # Gather List HTML.
    html = requests.get('https://www.rottentomatoes.com/{}'.format(args['http']['path'])).text
    selector = Selector(text=html)

    # For Each Media Item
    for media in selector.css('[data-qa="wts-item"]'):
        data = {}
        data['release_year'] = media.css('.wts-item_info small::text').get().replace('(', '').replace(')', '')
        data['clean_title'] = media.css('.wts-item__thumbnail a').attrib['href']
        data['title'] = media.css('.wts-item__thumbnail a').attrib['title']
        data['adult'] = False

        # Query to get IMDB ID
        info_json = requests.get('https://www.omdbapi.com/?t={}&apikey=6be019fc'.format(data['title'])).json()

        data['imdb_id'] = info_json['imdbID']
        data['id'] = int(data['imdb_id'].replace('tt', ''))

        list.append(data)

    return {
        'headers': {
            'content-type': 'application/json'
        },
        'body': json.dumps(list)
    }

# print(
#     main({
#         'http': {
#             'path': "/user/id/[uuid]/wts"
#         }
#     })
# )