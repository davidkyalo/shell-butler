import threading
from ..types import stack

threads = stack()

def add_to_queue(response):
    thread = threads.get(response.data.path, None)
    if not thread:
        thread = DowloadThread(response)
        threads[response.data.path] = thread

    return thread


def in_queue(key):
    if key in threads.keys():
        return True
    else:
        return False

def download(key):
    thread = threads.get(key, None)
    if thread:
        if thread._is_waiting:
            thread._is_waiting = False
            thread.start()
        if thread.is_alive():
            thread.join()
            del threads[key]
    return


CHUNK_SIZE = 1024

class DowloadThread(threading.Thread):
    """docstring for DowloadThread"""
    def __init__(self, response, *args, **kwargs):
        super(DowloadThread, self).__init__( *args, **kwargs)
        self.response = response
        self._is_waiting = True
        self.daemon = True

    def run(self):
        response = self.response
        try:
            if response._content is False:
                with open(response.data.path, 'wb') as fo:
                    for chunk in response.iter_content(CHUNK_SIZE):
                        fo.write(chunk)
            elif response._content != None:
                response.data.write(response.content, True)
            response._content = None
        except:
            response.data.delete()
