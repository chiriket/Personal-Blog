# import urllib.request,json
# from .models import Quote



# # Getting api key
# api_key = None

# # Getting the movie base url
# base_url = None

# def configure_request(app):
#     global api_key,base_url
#     api_key = app.config['QUOTE_API_KEY']
#     base_url = app.config['QUOTE_API_BASE_URL']






# # def get_quotes(category):
# #     '''
# #     Function that gets the json responce to our url request
# #     '''
# #     get_quotes_url = base_url.format(category,api_key)

# #     with urllib.request.urlopen(get_quotes_url) as url:
# #         get_quotes_data = url.read()
# #         get_quotes_response = json.loads(get_quotes_data)

# #         quote_results = None

# #         if get_quotees_response['results']:
# #             quote_results_list = get_quotes_response['results']
# #             quote_results = process_results(quote_results_list)


# #     return quote_results()










