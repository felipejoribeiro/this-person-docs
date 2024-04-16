# Initiating a serverless project
To initiate a serverless project you can use the npm utility `sls create`. You can pass a template for it to be based on. Here goes the available ones:

- aws-clojurescript-gradle
- aws-clojure-gradle
- aws-nodejs
- aws-nodejs-typescript
- aws-alexa-typescript
- aws-nodejs-ecma-script
- aws-python
- aws-python3
- aws-ruby
- aws-provided
- aws-kotlin-jvm-maven
- aws-kotlin-jvm-gradle
- aws-kotlin-nodejs-gradle
- aws-groovy-gradle
- aws-java-maven
- aws-java-gradle
- aws-scala-sbt
- aws-csharp
- aws-fsharp
- aws-go
- aws-go-dep
- aws-go-mod
- plugin

So you can chose one of those with the following command:

```bash
sls create --template aws-python --path myApp --name myApp
```

So you determine the template and the place to create the project. After the download you can run `npm install` to install the required dependencies for the tamplate.

## Basic structure
The project will always contain an `serverless.yml` file. Like `json`, `yml` is a human readable deserialized language. You can even use `json` in `yml`. One thing to take care is the indentation. Like python, this is very important for the syntax.

In this file we register metadata about our service. Like name, that describes the name of our service. Here goes what is created initially:

```yml
service: auction-service

plugins:
  - serverless-bundle
  - serverless-pseudo-parameters

provider:
  name: aws
  runtime: nodejs12.x
  memorySize: 256
  stage: ${opt:stage, 'dev'}
  region: us-east-2
  
functions:
  hello:
    handler: src/handlers/hello.handler
    events:
      - http:
          method: GET
          path: /hello

custom:
  bundle:
    linting: false
```

You can install various pluggins too. But there are two that came with the used template, `serverless-bundle`, it bundles the files using `webpack` it comes configured alt of the box. And `serverless-pseudo-parameters` that easily interpolate amazon services with some configurations.

The provider specifies details about the cloud provider. Like memory when the lambdafunction is executed (`memorySize`). And `stage` that determine the way of deployment.

And functions is where we define the `lambda` functions of the deployment. In the example we can see that when there is a `GET` request the function `/hello` will be called.

You can add custom properties as desabling linting in the example. Notice that this isn't advised in production.

We have a `package.json` as well. With the node packages that are downloaded determined by the template.

## Deploying
Now that everything is configured, we can procede with the deployment. You can do that runing the following command in the directory where you cloned and configured the project:

```bash
sls deploy -v
```

The verbose is for us to see everything the command will do.

It is a bunch of things.

Now you can see your `Lambda` function running with the provided endpoint link. You can see your lambda function running too in the  `AWS` website by going in the `cloudformation` service and checking the `stack` tab. There we will see all services that were deployed and some usefull features. Like the logs and enabled services. These things were configured with the console application and the template configuration.

There we can see a bunch of things like:
- The source code in `LambdaFunction`
- The API in `ApiGatewayRestApi`

If you only changed a function, than you can deploy only the lambdafunction with the following command:

```bash
sls deploy -f createAuction -v 
```

And it will pass the configuration phase and things will go pretty fast.

## Set down an application
It is really simple, just run in the project folder the command:

`sls remove -v`



## all the output
Here goes all the output of the deployment:
```
Serverless: Deprecation warning: Starting from next major object notation for "service
" property will no longer be recognized. Set "service" property directly with service
name.
            More Info: https://www.serverless.com/framework/docs/deprecations/#SERVICE
_OBJECT_NOTATION
Serverless: Deprecation warning: CLI options definitions were upgraded with "type" pro
perty (which could be one of "string", "boolean", "multiple"). Below listed plugins do
 not predefine type for introduced options:
             - ServerlessPlugin for "out"
            Please report this issue in plugin issue tracker.
            Starting with next major release, this will be communicated with a thrown
error.
            More Info: https://www.serverless.com/framework/docs/deprecations/#CLI_OPT
IONS_SCHEMA
Serverless: Deprecation warning: Resolution of lambda version hashes was improved with
 better algorithm, which will be used in next major release.
            Switch to it now by setting "provider.lambdaHashingVersion" to "20201221"
            More Info: https://www.serverless.com/framework/docs/deprecations/#LAMBDA_
HASHING_VERSION_V2
Serverless: Using configuration:
{
  "packager": "npm",
  "packagerOptions": {},
  "webpackConfig": "node_modules/serverless-bundle/src/webpack.config.js",
  "includeModules": {
    "forceExclude": [
      "aws-sdk"
    ],
    "forceInclude": null,
    "packagePath": "package.json"
  },
  "keepOutputDirectory": false
}
Serverless: Removing .../aws_class/auction-service/.webpack
Serverless: Bundling with Webpack...
Serverless: Fetch dependency graph from .../aws_class/auction-service/package.json
Serverless: No external modules needed
Serverless: Zip service: .../aws_class/auction-service/.webpack/service [39 ms]
Serverless: Packaging service...
Serverless: Remove .../aws_class/auction-service/.webpack
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
CloudFormation - CREATE_IN_PROGRESS - AWS::CloudFormation::Stack - auction-service-dev
CloudFormation - CREATE_IN_PROGRESS - AWS::S3::Bucket - ServerlessDeploymentBucket
CloudFormation - CREATE_IN_PROGRESS - AWS::S3::Bucket - ServerlessDeploymentBucket
CloudFormation - CREATE_COMPLETE - AWS::S3::Bucket - ServerlessDeploymentBucket
CloudFormation - CREATE_IN_PROGRESS - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
CloudFormation - CREATE_IN_PROGRESS - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
CloudFormation - CREATE_COMPLETE - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
CloudFormation - CREATE_COMPLETE - AWS::CloudFormation::Stack - auction-service-dev
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service auction-service.zip file to S3 (75.77 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
CloudFormation - UPDATE_IN_PROGRESS - AWS::CloudFormation::Stack - auction-service-dev
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::RestApi - ApiGatewayRestApi
CloudFormation - CREATE_IN_PROGRESS - AWS::IAM::Role - IamRoleLambdaExecution
CloudFormation - CREATE_IN_PROGRESS - AWS::Logs::LogGroup - HelloLogGroup
CloudFormation - CREATE_IN_PROGRESS - AWS::IAM::Role - IamRoleLambdaExecution
CloudFormation - CREATE_IN_PROGRESS - AWS::Logs::LogGroup - HelloLogGroup
CloudFormation - CREATE_COMPLETE - AWS::Logs::LogGroup - HelloLogGroup
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::RestApi - ApiGatewayRestApi
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::RestApi - ApiGatewayRestApi
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Resource - ApiGatewayResourceHello
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Resource - ApiGatewayResourceHello
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::Resource - ApiGatewayResourceHello
CloudFormation - CREATE_COMPLETE - AWS::IAM::Role - IamRoleLambdaExecution
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Function - HelloLambdaFunction
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Function - HelloLambdaFunction
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Function - HelloLambdaFunction
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - ...
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Permission - HelloLambdaPermissionApiGateway
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Version - ...
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Permission - HelloLambdaPermissionApiGateway
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Version - ... 
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment...
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment...
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::Deployment - ApiGatewayDeployment...
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Permission - HelloLambdaPermissionApiGateway
CloudFormation - UPDATE_COMPLETE_CLEANUP_IN_PROGRESS - AWS::CloudFormation::Stack - auction-service-dev
CloudFormation - UPDATE_COMPLETE - AWS::CloudFormation::Stack - auction-service-dev
Serverless: Stack update finished...
Service Information
service: auction-service
stage: dev
region: us-east-2
stack: auction-service-dev
resources: 11
api keys:
  None
endpoints:
  GET - https:// <link>
  functions:
  hello: auction-service-dev-hello
layers:
  None

Stack Outputs
...
ServiceEndpoint: https:// <link>
ServerlessDeploymentBucketName: ...



**************************************************************************************
Serverless: Announcing Metrics, CI/CD, Secrets and more built into Serverless Framewor
k. Run "serverless login" to activate for free..
**************************************************************************************
```
