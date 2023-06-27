from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from cassandra.cluster import Cluster

# Create SparkSession and StreamingContext
spark = SparkSession.builder \
    .appName('ClickstreamProcessor') \
    .config('spark.cassandra.connection.host', 'localhost') \
    .config('spark.cassandra.connection.port', '9042') \
    .getOrCreate()

ssc = StreamingContext(spark.sparkContext, batchDuration=5)

# Create Kafka Direct Stream
kafka_params = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'clickstream_group',
    'auto.offset.reset': 'latest'
}

kafka_stream = KafkaUtils.createDirectStream(
    ssc, topics=['clickstream'], kafkaParams=kafka_params
)

# Process Clickstream Data
def process_clickstream_data(rdd):
    # Process each RDD in the DStream
    for record in rdd:
        clickstream_data = record[1]
        print(clickstream_data)

# Save Data to Cassandra
def save_to_cassandra(rdd):
    if not rdd.isEmpty():
        spark = SparkSession.builder.getOrCreate()
        clickstream_df = spark.createDataFrame(rdd, schema=['clickstream_data'])
        clickstream_df.write \
            .format('org.apache.spark.sql.cassandra') \
            .options(table='clickstream_table', keyspace='your_keyspace') \
            .mode('append') \
            .save()

# Start the Streaming Context
kafka_stream.foreachRDD(process_clickstream_data)
kafka_stream.foreachRDD(save_to_cassandra)

ssc.start()
ssc.awaitTermination()
