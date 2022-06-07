# A PySpark/Jupyter template on Gitpod

This is a [PySpark](https://spark.apache.org/docs/latest/api/python/) template configured for ephemeral development environments on [Gitpod](https://www.gitpod.io/).

## Next Steps

Click the button below to start a new development environment:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/muralisuraparaju-tw/gitpod-python)

## Get Started With Your Own Project

### A new project

Click the above "Open in Gitpod" button to start a new workspace. Once you're ready to push your first code changes, Gitpod will guide you to fork this project so you own it.

### An existing project

To get started with Python Django on Gitpod, add a [`.gitpod.yml`](./.gitpod.yml) file which contains the configuration to improve the developer experience on Gitpod. To learn more, please see the [Getting Started](https://www.gitpod.io/docs/getting-started) documentation.



### external jars required 

these jars are specific to Java version 1.8.0_252.

wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-azure/3.3.3/hadoop-azure-3.3.3.jar
wget https://repo1.maven.org/maven2/com/microsoft/azure/azure-storage/8.6.6/azure-storage-8.6.6.jar
wget https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-util-ajax/9.4.8.v20171121/jetty-util-ajax-9.4.8.v20171121.jar
wget https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-util/9.4.46.v20220331/jetty-util-9.4.46.v20220331.jar
venv/bin/pyspark --jars hadoop-azure-3.3.3.jar,azure-storage-8.6.6.jar
cp *.jar venv/lib/python3.9/site-packages/pyspark/jars
