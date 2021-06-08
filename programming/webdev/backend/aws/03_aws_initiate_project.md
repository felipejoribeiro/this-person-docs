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

In this file we register metadata about our service. Like name, that describes the name of our service.







