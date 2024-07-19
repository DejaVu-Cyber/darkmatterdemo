
from warcio.archiveiterator import ArchiveIterator

with open('research-caps---chinese-20240625223419.warc', 'rb') as stream:
    for record in ArchiveIterator(stream):
        if record.rec_type == 'response':
            if record.http_headers.get_header('Content-Type') == 'text/html':
                print(record.rec_headers.get_header('WARC-Target-URI'))
                print(record.content_stream().read())
                print('')
