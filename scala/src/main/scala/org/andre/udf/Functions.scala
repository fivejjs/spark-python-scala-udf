package com.databricks.solutions.udf
import org.apache.spark.sql.SQLContext

object Functions {
  def cube(n: Int) = n * n * n

  def isprime(n: Int): Boolean = {
    if (n <= 1)
      false
    else if (n == 2)
      true
    else
      !(2 to scala.math.sqrt(n).toInt).exists(x => n % x == 0)

  }

  def registerFunc(sqlContext: SQLContext, name: String) {
    val f = cube(_)
    sqlContext.udf.register(name, f)
  }

  def registerFunc2(sqlContext: SQLContext, name: String) {
    val f = isprime(_)
    sqlContext.udf.register(name, f)
  }
}
