import requests

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
api_key = 'eUcmvMCf2u2QqvBv1Ih01w'
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'url': 'https://linkedin.com/in/eden-marco/'
}


if __name__ == '__main__':

    # response = requests.get(
    #     api_endpoint,
    #     params=params,
    #     headers=header_dic
    # )

    # print(response.json())

    response = requests.get("https://gist.githubusercontent.com/Mlevydaniel/733014293a5817d7864db5ff5ff2de99/raw/ca105fec197676a3bfbbcea337cdd811c566e83c/eden-marco.json")
    print(response.json()["full_name"])