import requests

apiKey = 'F8G7is65SfFVHdRRfLCzXDPultr6yy7evpfQiCu3'

def fetchMars(date):
  URL_APOD = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?"
  params = {
      'api_key':apiKey,
      'earth_date':date,
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()
  ans = (response)
  return ans['photos'][:3]

fetchMars('2022-11-22')
