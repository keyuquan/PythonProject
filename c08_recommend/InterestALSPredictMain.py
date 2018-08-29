from pyspark import RDD
from pyspark.sql import Row
from pyspark.sql import SparkSession

from evaluation import RegressionEvaluator
from recommendation import ALS

spark = SparkSession \
    .builder \
    .appName("recommend") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.shuffle.consolidateFiles", "true") \
    .getOrCreate()

lines = spark.read.text("hdfs://isec-hdp01:8020/data/source3/*").rdd  # type: RDD

parts = lines.map(lambda row: row.value.split("::"))
amountsRDD = parts.map(lambda p: Row(userId=int(p[0]), rank=int(p[1]), amount=float(p[2])))
amounts = spark.createDataFrame(amountsRDD)
(training, test) = amounts.randomSplit([0.8, 0.2])

# Build the recommendation model using ALS on the training data
# Note we set cold start strategy to 'drop' to ensure we don't get NaN evaluation metrics
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="rank", ratingCol="amount", coldStartStrategy="drop")
model = als.fit(training)

# Evaluate the model by computing the RMSE on the test data
predictions = model.transform(test)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="amount", predictionCol="prediction")

rmse = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))

# Generate top 10 movie recommendations for each user
userRecs = model.recommendForAllUsers(10)
userRecs.show(100)

# Generate top 10 user recommendations for each movie
movieRecs = model.recommendForAllItems(10)
movieRecs.show()
