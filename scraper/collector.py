import requests
import time

class Collector:
    def __init__(self):
        self.RATE_LIMIT_DELAY = 1.5  # rate limiting
        self. DEFAULT_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    # (encapsulation)
    def __request_methods(self,method,url,headers=None,json =None, data=None, params = None,timeout = 2.5,verify = True, Cert = None):
        m = method.upper()
        headers = headers or self.DEFAULT_HEADERS
        # check which method is called
        try:
            if m == "GET":
                request = requests.get(url, headers=headers, data=data, params=params, timeout=timeout,verify=verify,cert=Cert,json=json)
            elif m == "POST":
                request = requests.post(url, headers=headers, data=data, params=params, timeout=timeout,verify=verify,cert=Cert,json=json)
            elif m == "PUT":
                request = requests.put(url, headers=headers, data=data, params=params, timeout=timeout,verify=verify,cert=Cert,json=json)
            elif m == "DELETE":
                request = requests.delete(url, headers=headers, data=data, params=params, timeout=timeout,verify=verify,cert=Cert,json=json)
            else:
                raise "No valid method"
            # for client and server errors
            request.raise_for_status()

            time.sleep(self.RATE_LIMIT_DELAY)  # rate limiting
            return request
        # error handling for status codes
        except requests.exceptions.HTTPError as http_err:
            return http_err
        except requests.exceptions.Timeout:
            return "Request timed out"
        except requests.exceptions.ConnectionError:
            return "Connection Error"
        except requests.exceptions.RequestException as err:
            return err
    @staticmethod
    def get_method(self,url,timeout = 2.5,verify = True, Cert = None):
        return self.request_methods("GET",url,timeout = timeout,verify = verify, Cert = Cert)
    @staticmethod
    def post_method(self,url,headers=None,json =None, data=None, params = None,timeout = 2.5,verify = True, Cert = None):
        return self.request_methods("POST",url,headers=headers,json =json, data=data, params = params,timeout = timeout,verify = verify, Cert = Cert)
    @staticmethod
    def put_method(self,url,headers=None,json =None, data=None, params = None,timeout = 2.5,verify = True, Cert = None):
        return self.request_methods("PUT",url,headers=headers,json =json, data=data, params = params,timeout = timeout,verify = verify, Cert = Cert)
    @staticmethod
    def delete_method(self,url,headers=None,json =None, data=None, params = None,timeout = 2.5,verify = True, Cert = None):
        return self.request_methods("DELETE",url,headers=headers,json =json, data=data, params = params,timeout = timeout,verify = verify, Cert = Cert)


