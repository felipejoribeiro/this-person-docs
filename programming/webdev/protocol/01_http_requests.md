# HTTP request
The http protocol is used by the client to send messages for the server in the following format:

```
A Request-line

Zero or more header (General|Request|Entity) fields followed by CRLF

An empty line (i.e., a line with nothing preceding the CRLF) 
indicating the end of the header fields

Optionally a message-body
```

## The request line
The first thing to be configured is the `method token`, followed by the `request-URI` and the protocol version, ending with `CRLF` (The elements are separated by `SP` characters):

```
Request-Line = Method SP Request-URI SP HTTP-Version CRLF
```
Here is a list with the request methods:

| S.N.    |  Method and Description  |
|---------|--------------------------|
| GET     |  Retrieve information only.  |
| HEAD    |  Same as get, but only sends status line and headers section.  |
| POST    |  Send data to a server. |
| PUT     |  Replaces data in the server.  |
| DELETE  |  Delete target in the server.  |
| CONNECT |  Stablish a tunnel to the server identified by a given `URI`.   |
| OPTIONS |  Describe the communication options for the targer resource.  |
| TRACE   |  Do a message loop back test with the path to the target resource.  |

## Request-URI
Is `Uniform Resource Identifier` and it identifies the resource upon which to apply the request. Here it is the most commonly used forms:

```
Request-URI = "*" | absoluteURI | abs_path | authority
```
- The asterisk `*` is used then an `HTTP` request does not apply to a particular resource, but to the server itself, and is only allowed when the method used does not necessarily apply to a resource. For example: `OPTIONS * HTTP/1.1`
- The absoluteURI is used when an `HTTP` request is being made to a proxy. The proxy is requested to forward the request or service from a valid cache, and return the response. For example: `GET http://www.w3.org/pub/WWW/TheProject.html HTTP/1.1`
- The most common form of Request-URI is that used to identify a resource on an origin server or gateway. For example, a client wishing to retrieve a resource directly from the origin server would create a `TCP` connection to `port 80` of the host "www.w3.org" and send the following lines:
```
GET /pub/WWW/TheProject.html HTTP/1.1

Host: www.w3.org
```
Note that the absolute path cannot be empty; if none is present in the original URI, it MUST be given as "/" (the server root).

## Request header fields
In this field we can pass additional information about the request and about the client itself. These fields act as request modifiers. Here are some:

- Accept-Charset
- Accept-Encoding
- Accept-Language
- Authorization
- Expect
- From
- Host
- If-Match
- If-Modified-Since
- If-None-Match
- If-Range
- If-Unmodified-Since
- Max-Forwards
- Proxy-Authorization
- Range
- Referer
- TE
- User-Agent
If you have your own custom client and web-server you can create new custom entries as well.

Here goes some examples for request messages:

```
GET /hello.htm HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
```

(`HTTP` request to fetch `hello.htm` page from a webserver running on `tutorialspoint.com`.)

```
POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: application/x-www-form-urlencoded
Content-Length: length
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

licenseID=string&content=string&/paramsXML=string
```
(Sending information using request message body.)

```
POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

<?xml version="1.0" encoding="utf-8"?>
<string xmlns="http://clearforest.com/">string</string>
```
(This example shows how you can pass plain XML to your web server.)





