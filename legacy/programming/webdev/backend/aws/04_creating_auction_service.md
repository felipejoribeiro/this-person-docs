# Creating an auction service
The `lambda` function has some interesting limitations. One example is that we can't store information in the global context, as each call of the function will not necessarily occur in the same machine. For persistance we need to use other technologies like `DynamoDB` or other database.

Other limitation is the time. The lambda function can only run for 15 minutes. Here goes the initial structure for this auction service:

```javascript
async function createAuction(event, context) {
  const { title } = JSON.parse(event.body)
  const now = new Date()

  const auction = {
    title,
    status: 'OPEN',
    createdAt: now.toISOString()
  }

  return {
    statusCode: 201,
    body: JSON.stringify(auction),
  };
}

export const handler = createAuction;
```
Notice that we can receive the body of the request in the `event` variable. There are other things that came with it. If we send the request and return the `event` and `context` objects, we will receive something like this:

```json
{
    "event": {
        "resource": "/auction",
        "path": "/auction",
        "httpMethod": "POST",
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "CloudFront-Forwarded-Proto": "https",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-Mobile-Viewer": "false",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Tablet-Viewer": "false",
            "CloudFront-Viewer-Country": "BR",
            "Content-Type": "application/json",
            "Host": "...execute-api.us-east-2.amazonaws.com",
            "Postman-Token": "...",
            "User-Agent": "...",
            "Via": "...",
            "X-Amz-Cf-Id": "...",
            "X-Amzn-Trace-Id": "...",
            "X-Forwarded-For": "...",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https"
        },
        "multiValueHeaders": {
            "Accept": [
                "*/*"
            ],
            "Accept-Encoding": [
                "gzip, deflate, br"
            ],
            "CloudFront-Forwarded-Proto": [
                "https"
            ],
            "CloudFront-Is-Desktop-Viewer": [
                "true"
            ],
            "CloudFront-Is-Mobile-Viewer": [
                "false"
            ],
            "CloudFront-Is-SmartTV-Viewer": [
                "false"
            ],
            "CloudFront-Is-Tablet-Viewer": [
                "false"
            ],
            "CloudFront-Viewer-Country": [
                "BR"
            ],
            "Content-Type": [
                "application/json"
            ],
            "Host": [
                "..."
            ],
            "Postman-Token": [
                "..."
            ],
            "User-Agent": [
                "..."
            ],
            "Via": [
                "..."
            ],
            "X-Amz-Cf-Id": [
                "..."
            ],
            "X-Amzn-Trace-Id": [
                "..."
            ],
            "X-Forwarded-For": [
                "..."
            ],
            "X-Forwarded-Port": [
                "443"
            ],
            "X-Forwarded-Proto": [
                "https"
            ]
        },
        "queryStringParameters": null,
        "multiValueQueryStringParameters": null,
        "pathParameters": null,
        "stageVariables": null,
        "requestContext": {
            "resourceId": "...",
            "resourcePath": "/auction",
            "httpMethod": "POST",
            "extendedRequestId": "...",
            "requestTime": "08/Jun/2021:20:28:19 +0000",
            "path": "/dev/auction",
            "accountId": "...",
            "protocol": "HTTP/1.1",
            "stage": "dev",
            "domainPrefix": "...",
            "requestTimeEpoch": 1,
            "requestId": "...",
            "identity": {
                "cognitoIdentityPoolId": null,
                "accountId": null,
                "cognitoIdentityId": null,
                "caller": null,
                "sourceIp": "...",
                "principalOrgId": null,
                "accessKey": null,
                "cognitoAuthenticationType": null,
                "cognitoAuthenticationProvider": null,
                "userArn": null,
                "userAgent": "...",
                "user": null
            },
            "domainName": "...",
            "apiId": "..."
        },
        "body": "{\n    \"tile\":\"super nice car\"\n}",
        "isBase64Encoded": false
    },
    "context": {
        "callbackWaitsForEmptyEventLoop": true,
        "functionVersion": "$LATEST",
        "functionName": "auction-service-dev-createAuction",
        "memoryLimitInMB": "256",
        "logGroupName": "/aws/lambda/auction-service-dev-createAuction",
        "logStreamName": "...",
        "invokedFunctionArn": "...",
        "awsRequestId": "..."
    }
}
```

So we are responding with the `auction` object that we created, it has some informations that we even processed in the machine where the lambda function was executed.

If you only changed the javascript function then you can redeploy with other command:

```bash
sls deploy -f createAuction -v
```
It is way faster and good for development as you can change things quickly and see the result.


