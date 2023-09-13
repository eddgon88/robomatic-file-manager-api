import requests
from xml.dom import minidom


class Consumer:
    @staticmethod
    def consumeService(params):
        print("Consuming: " + params['service_type'])
        if params['service_type'] == 'REST':
            return consumeRest(params)
        elif params['service_type'] == 'SOAP':
            return consumeSoap(params)
        elif params['service_type'] == 'SCRAPING':
            return consumeScraping(params)
        elif params['service_type'] == 'GRAPH':
            return consumeGraphql(params)


def consumeRest(params):
    print("Sending: " + str(params))
    try:
        if params['method'] == 'GET':            
            return restResponseMapper(requests.get(params['url'], headers=params['headers']))            
        elif params['method'] == 'POST':
            return restResponseMapper(requests.post(params['url'], headers=params['headers'], data=params['body']))
        elif params['method'] == 'PUT':
            return restResponseMapper(requests.put(params['url'], headers=params['headers'], data=params['body']))
        elif params['method'] == 'PATCH':
            return restResponseMapper(requests.patch(params['url'], headers=params['headers'], data=params['body']))
        elif params['method'] == 'DELETE':
            return restResponseMapper(requests.delete(params['url'], headers=params['headers'], data=params['body']))
        elif params['method'] == 'HEAD':
            return restResponseMapper(requests.head(params['url'], headers=params['headers'], data=params['body']))
        elif params['method'] == 'OPTIONS':
            return restResponseMapper(requests.options(params['url'], headers=params['headers'], data=params['body']))
    except Exception as e:
        return e


def consumeSoap(params):    
    xml = minidom.parseString(params['body'])
    body = xml.toprettyxml()    
    print("Sending: " + str(params))
    return responseMapper(requests.post(params['url'], headers=params['headers'], data=str(body)))

def consumeScraping(params):    
    print("Sending: " + str(params))
    return responseMapper(requests.get(params['url'], headers=params['headers']))

def consumeGraphql(params):    
    print("Sending: " + str(params))    
    return restResponseMapper(requests.post(params['url'], headers=params['headers'], json={"query": params['body']}))

def restResponseMapper(httpResponse):
    return {
        'status_code' : httpResponse.status_code,
        'headers' : httpResponse.headers,
        'body' : httpResponse.json(),
    }

def responseMapper(httpResponse):
    print("httpResponse: " + str(httpResponse.status_code))
    print("httpResponse: " + str(httpResponse.headers))
    return {
        'status_code' : httpResponse.status_code,
        'headers' : httpResponse.headers,
        'body' : httpResponse.content
    }