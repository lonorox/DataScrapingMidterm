import requests
import time


class Collector:
    RATE_LIMIT_DELAY = 1.5  # Class-level rate limit
    DEFAULT_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    @staticmethod
    def __request_methods(method, url, headers=None, json=None, data=None, params=None, timeout=2.5, verify=True,
                          Cert=None):
        """Handles HTTP requests with different methods"""
        m = method.upper()
        headers = headers or Collector.DEFAULT_HEADERS  # Use class variable

        try:
            if m == "GET":
                response = requests.get(url, headers=headers, data=data, params=params, timeout=timeout, verify=verify,
                                       cert=Cert, json=json)
            elif m == "POST":
                response = requests.post(url, headers=headers, data=data, params=params, timeout=timeout, verify=verify,
                                        cert=Cert, json=json)
            elif m == "PUT":
                response = requests.put(url, headers=headers, data=data, params=params, timeout=timeout, verify=verify,
                                       cert=Cert, json=json)
            elif m == "DELETE":
                response = requests.delete(url, headers=headers, data=data, params=params, timeout=timeout,
                                          verify=verify, cert=Cert, json=json)
            else:
                raise ValueError("No valid method specified")

            response.raise_for_status()  # Raise an error for bad responses

            time.sleep(Collector.RATE_LIMIT_DELAY)  # Apply rate limiting
            return response

        except requests.exceptions.HTTPError:
            print('HTTP Error')
            return None
        except requests.exceptions.Timeout:
            print('Timeout Error')
            return None
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            return None
        except requests.exceptions.RequestException:
            print('Request Error')
            return None

    @staticmethod
    def get_method(url, timeout=1, verify=True, Cert=None):
        return Collector.__request_methods("GET", url, timeout=timeout, verify=verify, Cert=Cert)

    @staticmethod
    def post_method(url, headers=None, json=None, data=None, params=None, timeout=2.5, verify=True, Cert=None):
        return Collector.__request_methods("POST", url, headers=headers, json=json, data=data, params=params,
                                           timeout=timeout, verify=verify, Cert=Cert)

    @staticmethod
    def put_method(url, headers=None, json=None, data=None, params=None, timeout=2.5, verify=True, Cert=None):
        return Collector.__request_methods("PUT", url, headers=headers, json=json, data=data, params=params,
                                           timeout=timeout, verify=verify, Cert=Cert)

    @staticmethod
    def delete_method(url, headers=None, json=None, data=None, params=None, timeout=2.5, verify=True, Cert=None):
        return Collector.__request_methods("DELETE", url, headers=headers, json=json, data=data, params=params,
                                           timeout=timeout, verify=verify, Cert=Cert)
