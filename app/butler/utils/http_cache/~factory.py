from requests_cache.core import CachedSession

class SessionFactory(CachedSession):

    # def  __init__(self, *args, interceptors = None, **kwargs):
    #     super(SessionFactory, self).__init__(*args, **kwargs)
    #     self._interceptors =


    def send(self, request, **kwargs):
        lazy_cache = kwargs.get('stream', False)
        if (self._is_cache_disabled
            or request.method not in self._cache_allowable_methods):
            response = super(CachedSession, self).send(request, **kwargs)
            response.from_cache = False
            return response

        cache_key = self.cache.create_key(request)

        def send_request_and_cache_response():
            response = super(CachedSession, self).send(request, **kwargs)
            if response.status_code in self._cache_allowable_codes:
                self.cache.save_response(cache_key, response, lazy = lazy_cache)
            response.from_cache = False
            return response

        response, timestamp = self.cache.get_response_and_time(cache_key)
        if response is None:
            return send_request_and_cache_response()

        if self._cache_expire_after is not None:
            is_expired = datetime.utcnow() - timestamp > self._cache_expire_after
            if is_expired:
                if not self._return_old_data_on_error:
                    self.cache.delete(cache_key)
                    return send_request_and_cache_response()
                try:
                    new_response = send_request_and_cache_response()
                except Exception:
                    return response
                else:
                    if new_response.status_code not in self._cache_allowable_codes:
                        return response
                    return new_response

        # dispatch hook here, because we've removed it before pickling
        response.from_cache = True
        response = dispatch_hook('response', request.hooks, response, **kwargs)
        return response


    def get(self, url, before_cache = ):
        pass

    def pipe(self, url, tap = None):
        pass
