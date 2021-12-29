# Databricks notebook source
#call MSSP Notebooks

# COMMAND ----------

#run Member Notebook
%run /Repos/MSSP/MSSP/Notebooks/MSSP_Member

# COMMAND ----------

#run Claim Notebook
%run /Repos/MSSP/MSSP/Notebooks/MSSP_Claim

# COMMAND ----------

#create csv of testresult table and save to blob storage
# Azure Storage Account Name
storage_account_name = "globalproducts"

# Azure Storage Account Key
storage_account_key = "onoPvW5rPcUoa2AoJnTzv4UXijmIC6KU8pXIbMYXq+vxkX2T7VOpb1nrstBz3Vw4FN/e8W5EoEaCqwqhsFoCxA=="

# Azure Storage Account Source Container
container = "globalproducts"

# Set the configuration details to read/write
spark.conf.set("fs.azure.account.key.{0}.blob.core.windows.net".format(storage_account_name), storage_account_key)

# COMMAND ----------

# MAGIC %scala
# MAGIC 
# MAGIC val df_spark= spark.table("default.testresult")
# MAGIC 
# MAGIC 
# MAGIC spark.conf.set("fs.azure.account.key.azurestorage.blob.core.windows.net","onoPvW5rPcUoa2AoJnTzv4UXijmIC6KU8pXIbMYXq+vxkX2T7VOpb1nrstBz3Vw4FN/e8W5EoEaCqwqhsFoCxA==")
# MAGIC 
# MAGIC // Save to the source container
# MAGIC df_spark.write.mode(SaveMode.Append).csv("wasbs://globalproducts@globalproducts.blob.core.windows.net/csvFolder/")
