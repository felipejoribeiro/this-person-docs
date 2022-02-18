# Introduction
The way database encorajes us to do is consider data things, like, people, trains and trees. These things has state and we store then in the database.
Now we want to thing about events first, the difference is by its definition, its not a thing, it is an indication in time that the thing took place.
It's a little cumbersome to store events in databases. Instead we use a structure like a log, that is a orderede sequence of these logs, with a little bit of state of what happened in that time. They are easy to build ad scale.

Apace Kafka is a solution to manage these logs. It calls then topics. An ordered collection of events that is stored in a durable way. They are written to disk in more than onw server, like, in a dusable way. They can store data for short periods of time or long periods of time.Day, years or forever. They can be small or big (there isn't any infra limitation concerning size). Each one of these events represent a thing happening in the business, maybe a user updates a shipping addres, maybe a thermostat reported a temperature or maybe some one entered in hte building. Kafka makes you thing about events first and things secondly.

When databases came along, it was normal to create monolithic applications that used all the database by itself. And it was the natural way. They were difficult to change and difficult to understand. Now the trend is to create lots of small applications, and these small applications that can be more easily understood and changed, like micro services for example can comunicate with each other through kafka topics. Each one of these services can consume from a kafka topic, do computations and all sorts of things, and then write to another kafka topic. And just like that we can create nets of these little services working together.


         .----------
         |
         |



## Ferramentas Kafka:
Maybe you want to integrate other old tools, that is, other old ways of storing data with kafka in your moment of transition, or maybe you want to use various forms of data storage besides kafka. For that you can use kafka connect. With the tool you can read from a database and write to a topic and vice versa. You don't need to write that code, it is already written in nice usuable modules that do all the work for you. You just need to deploy then and see then work.

Grouping, aggregation, enrichment (database joint), filtering... Kafka has modules for that, a java api that handles that for you called kafka streams. It implements these things in a scalable and optimized way.

- Kafka streams: API for data handling in kafka.
- Kafka connect: Old database models integration.
