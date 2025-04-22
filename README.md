docker file:
version: '3.8'

networks:
  kafkaflinkpostgres:
    driver: bridge

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.4.0
    hostname: zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    healthcheck:
      test: [ "CMD", "bash", "-c", "echo 'ruok' | nc localhost 2181" ]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - kafkaflinkpostgres

  broker:
    image: confluentinc/cp-kafka:7.4.0
    hostname: broker
    container_name: broker
    depends_on:
      zookeeper:
        condition: service_healthy
    ports:
      - "9092:9092"
      - "9101:9101"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: 'zookeeper:2181'
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://broker:29092,PLAINTEXT_HOST://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0
      KAFKA_CONFLUENT_LICENSE_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_CONFLUENT_BALANCER_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_JMX_PORT: 9101
      KAFKA_JMX_HOSTNAME: localhost
    healthcheck:
      test: [ "CMD", "bash", "-c", 'nc -z localhost 9092' ]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - kafkaflinkpostgres

  jobmanager:
    image: flink:latest
    expose:
      - "6123"
    ports:
      - "8081:8081"
    command: jobmanager
    networks:
      kafkaflinkpostgres:
        aliases:
          - jobmanager     
    environment:
      - JOB_MANAGER_RPC_ADDRESS=jobmanager
      - TZ=Asia/Kolkata      

  taskmanager:
    image: flink:latest
    depends_on:
      - jobmanager
    command: taskmanager
    networks:
      kafkaflinkpostgres:
        aliases:
          - taskmanager    
    links:
      - "jobmanager:jobmanager"
    environment:
      - JOB_MANAGER_RPC_ADDRESS=jobmanager
      - TZ=Asia/Kolkata    

  appserver:
    image: python:3.10
    environment:
      - TZ=Asia/Kolkata    
    volumes:
      - .:/app
    working_dir: /app
    networks:
      kafkaflinkpostgres:
        aliases:
          - appserver    
    command: bash -c "
      apt update &&
      dpkg -i jdk-11.0.21_linux-x64_bin.deb &&
      python3 -m venv /home/myenv &&
      source /home/myenv/bin/activate &&
      pip install kafka-python &&
      pip install apache-flink &&
      python3 your-python-code/run.py
      "

[user@dinm5CD42655LX FlinkCommerce]$ docker exec -it flinkcommerce-jobmanager-1 cat /opt/flink/conf/config.yaml
blob:
  server:
    port: '6124'
taskmanager:
  memory:
    process:
      size: 1728m
  bind-host: 0.0.0.0
  numberOfTaskSlots: 1
jobmanager:
  execution:
    failover-strategy: region
  rpc:
    address: jobmanager
    port: 6123
  memory:
    process:
      size: 1600m
  bind-host: 0.0.0.0
query:
  server:
    port: '6125'
parallelism:
  default: 1
rest:
  address: 0.0.0.0
env:
  java:
    opts:
      all: --add-exports=java.base/sun.net.util=ALL-UNNAMED --add-exports=java.rmi/sun.rmi.registry=ALL-UNNAMED --add-exports=jdk.compiler/com.sun.tools.java
c.api=ALL-UNNAMED --add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED --add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED --add-exp
orts=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED --add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED --add-exports=java.security.jgss/sun.s
ecurity.krb5=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --a
dd-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/java.lang.reflect=ALL-UNNAMED --add-opens=java.bas
e/java.text=ALL-UNNAMED --add-opens=java.base/java.time=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.locks=ALL-UNNAMED
[user@dinm5CD42655LX FlinkCommerce]$ 
