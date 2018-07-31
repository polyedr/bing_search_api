import json
import requests


def read_bing_key():

    bing_api_key = None
    try:
        with open('bing.key','rb') as f:
            bing_api_key = f.readline().strip()
    except:
        raise IOError('bing.key file not found')
        
    return bing_api_key
    

def run_query(search_terms):


    bing_api_key = read_bing_key()
    if not bing_api_key:
        raise KeyError('Bing Key Not Found')


    results = []



    
    try:
        url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
        headers = {'Ocp-Apim-Subscription-Key': bing_api_key}
        params = {'q': 'search_terms', "textDecorations":True, "textFormat":"HTML"}
        r = requests.get(url, headers=headers, params=params)     
        
    
        r = r.json()


        for result in r['webPages']['value']:
            results.append({
                'title': result['name'],
                'link': result['displayUrl'],
                'summary': result['snippet']})

    except:
        print("Error when querying the Bing API")


    return results






def main():
    print("Enter a query ")
    query = input()

    results = run_query(query)
    
   
    for result in results:
        print(result['title'])
        print('-'*len(result['title']))
        print(result['summary'])
        print(result['link'])
        print()
        
   
    
if __name__ == '__main__':
    main()

