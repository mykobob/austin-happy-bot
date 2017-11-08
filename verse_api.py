
class VerseApi:

    def get_text(self, verse_ref):
        bible_response = requests.get('http://getbible.net/json?passage=' + verse_ref)
        bible_obj = json.loads(bible_response.text[1:-2])
        
        verse_texts = bible_obj['book'][0]['chapter']

        return ' '.join(verse_texts[i]['verse'].strip() for i in verse.verse_range())

