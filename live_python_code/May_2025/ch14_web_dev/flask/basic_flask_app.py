from flask import Flask
print(f"__name__ : {__name__}")
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    web_app.run(debug=True)

#http methods
# get, post, put, delete

# http 1.0 and 1.1 difference
# HTTP 1.0:
# - Introduced in 1996.
# - Connection is closed after each request/response cycle.
# - Lacks persistent connections, meaning a new TCP connection is established for each request.
# - Does not support chunked transfer encoding.
# - Limited caching capabilities.
# - No support for pipelining requests.

# HTTP 1.1:
# - Introduced in 1999.
# - Supports persistent connections, allowing multiple requests to be sent over a single TCP connection.
# - Introduces chunked transfer encoding, allowing data to be sent in chunks.
# - Improved caching mechanisms with cache control headers.
# - Supports pipelining, allowing multiple requests to be sent without waiting for each response.
# - Introduces additional headers like Host, allowing multiple domains on a single IP address.

# 404- page not found
# 500- internal server error
# 200- ok
# 301- moved permanently
# 302- found (temporary redirect)
# 403- forbidden
# 401- unauthorized
# 304- not modified