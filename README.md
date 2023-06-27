# Clickstream_DataPipeline
ClickStream Data Pipeline using Apache Spark, Apache Kafka and Apache Cassandra(Dockerised)

This project is created using:
Python,
Docker,
Apache Kafka(Locally),
Apache Spark(Locally),
Apache Cassandra(Docker Container).

I have created a small python file which will produce sample clickstream data. The data will be pushed and consumed by a Kafka topic an further pushed to a spark cluster which will process and store the data in Cassandra.

Setup kafka:

> Download Apache Kafka from the official website.

> cd Kafka_directory/

> Start the zookeeper: bin/zookeeper-server-start.sh config/zookeeper.properties

> Start the kafka server: bin/kafka-server-start.sh config/server.properties

> Create a kafka topic :  bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic clickstream
 > Start the producer: bin/kafka-console-producer.sh --broker-list localhost:9092 --topic clickstream

> Start the consumer: bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic clickstream --from-beginning


Setup Spark:

> Download pyspark using homebrew: 'brew install pyspark'.



Setup Apache Cassandra using Docker:

> docker pull cassandra
> docker run --name cassandra-container -d -p 9042:9042 cassandra
> docker exec -it cassandra-container cqlsh

And extecute the scripts.


