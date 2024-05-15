
from io import BytesIO
import pycurl
import json

def send_purchase_request(url, headers, body_dict):
  # Create a pycurl object
  curl = pycurl.Curl()

  # Set request options
  curl.setopt(pycurl.URL, url)
  curl.setopt(pycurl.HTTPHEADER, headers)
  curl.setopt(pycurl.POST, 1)  # Set it to POST explicitly

  # Prepare JSON body
  body_as_json_string = json.dumps(body_dict)
  body_as_file_object = BytesIO(body_as_json_string.encode('utf-8'))  # Use BytesIO for efficient handling

  # Set request body options
  curl.setopt(pycurl.READDATA, body_as_file_object)
  curl.setopt(pycurl.POSTFIELDSIZE, len(body_as_json_string))

  # Perform the request and capture the response
  test = curl.perform()
  status_code = curl.getinfo(pycurl.RESPONSE_CODE)

  # Close the connection
  curl.close()

  return status_code

# Replace with actual values
url = 'url'
headers = [
    'accept: */*',
    'accept-language: en,tr-TR;q=0.9,tr;q=0.8,en-US;q=0.7',
    'content-type: application/json',
    'cookie: ',
    'origin: ',
    'priority: u=1, i',
    'referer: ',
    'sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile: ?0',
    'sec-ch-ua-platform: "macOS"',
    'sec-fetch-dest: empty',
    'sec-fetch-mode: cors',
    'sec-fetch-site: same-origin',
    'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-csrf-token: '
]
body_dict = {
   
    },

}

# Send the request and handle the response
status_code = send_purchase_request(url, headers, body_dict)

if status_code == 200:
  print("Request successful!")
else:
  print("Request failed. Check the response for details.")
