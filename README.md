[user@dinm5CD42655LX FlinkCommerce]$ docker cp target/FlinkCommerce-1.0-SNAPSHOT.jar flinkcommerce-jobmanager-1:/opt/flink/lib/
Successfully copied 20.3MB to flinkcommerce-jobmanager-1:/opt/flink/lib/
[user@dinm5CD42655LX FlinkCommerce]$ docker exec -it flinkcommerce-jobmanager-1 flink run -c FlinkCommerce.DataStreamJob /opt/flink/lib/FlinkCommerce-1.0-SNAPSHOT.jar
WARNING: Unknown module: jdk.compiler specified to --add-exports
WARNING: Unknown module: jdk.compiler specified to --add-exports
WARNING: Unknown module: jdk.compiler specified to --add-exports
WARNING: Unknown module: jdk.compiler specified to --add-exports
WARNING: Unknown module: jdk.compiler specified to --add-exports

------------------------------------------------------------
 The program finished with the following exception:

org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: Failed to execute job 'Flink Java API Skeleton'.
        at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:372)
        at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:222)
        at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:105)
        at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:851)
        at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:245)
        at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1095)
        at org.apache.flink.client.cli.CliFrontend.lambda$mainInternal$9(CliFrontend.java:1189)
        at org.apache.flink.runtime.security.contexts.NoOpSecurityContext.runSecured(NoOpSecurityContext.java:28)
        at org.apache.flink.client.cli.CliFrontend.mainInternal(CliFrontend.java:1189)
        at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1157)
Caused by: org.apache.flink.util.FlinkException: Failed to execute job 'Flink Java API Skeleton'.
        at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.executeAsync(StreamExecutionEnvironment.java:2253)
        at org.apache.flink.client.program.StreamContextEnvironment.executeAsync(StreamContextEnvironment.java:189)
        at org.apache.flink.client.program.StreamContextEnvironment.execute(StreamContextEnvironment.java:118)
        at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.execute(StreamExecutionEnvironment.java:2099)
        at FlinkCommerce.DataStreamJob.main(DataStreamJob.java:33)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.base/java.lang.reflect.Method.invoke(Unknown Source)
        at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:355)
        ... 9 more
Caused by: java.lang.RuntimeException: org.apache.flink.runtime.client.JobInitializationException: Could not start the JobMaster.
        at org.apache.flink.util.ExceptionUtils.rethrow(ExceptionUtils.java:321)
        at org.apache.flink.util.function.FunctionUtils.lambda$uncheckedFunction$2(FunctionUtils.java:75)
        at java.base/java.util.concurrent.CompletableFuture$UniApply.tryFire(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture$Completion.exec(Unknown Source)
        at java.base/java.util.concurrent.ForkJoinTask.doExec(Unknown Source)
        at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(Unknown Source)
        at java.base/java.util.concurrent.ForkJoinPool.scan(Unknown Source)
        at java.base/java.util.concurrent.ForkJoinPool.runWorker(Unknown Source)
        at java.base/java.util.concurrent.ForkJoinWorkerThread.run(Unknown Source)
Caused by: org.apache.flink.runtime.client.JobInitializationException: Could not start the JobMaster.
        at org.apache.flink.runtime.jobmaster.DefaultJobMasterServiceProcess.lambda$new$0(DefaultJobMasterServiceProcess.java:97)
        at java.base/java.util.concurrent.CompletableFuture.uniWhenComplete(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.postComplete(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture$AsyncSupply.run(Unknown Source)
        at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
        at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
        at java.base/java.lang.Thread.run(Unknown Source)
Caused by: java.util.concurrent.CompletionException: java.lang.RuntimeException: org.apache.flink.runtime.JobException: Cannot instantiate the coordinator for operator Source: Kafka source -> Sink: Print to Std. Out
        at java.base/java.util.concurrent.CompletableFuture.encodeThrowable(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.completeThrowable(Unknown Source)
        ... 4 more
Caused by: java.lang.RuntimeException: org.apache.flink.runtime.JobException: Cannot instantiate the coordinator for operator Source: Kafka source -> Sink: Print to Std. Out
        at org.apache.flink.util.ExceptionUtils.rethrow(ExceptionUtils.java:321)
        at org.apache.flink.util.function.FunctionUtils.lambda$uncheckedSupplier$4(FunctionUtils.java:114)
        ... 4 more
Caused by: org.apache.flink.runtime.JobException: Cannot instantiate the coordinator for operator Source: Kafka source -> Sink: Print to Std. Out
        at org.apache.flink.runtime.executiongraph.ExecutionJobVertex.initialize(ExecutionJobVertex.java:234)
        at org.apache.flink.runtime.executiongraph.DefaultExecutionGraph.initializeJobVertex(DefaultExecutionGraph.java:894)
        at org.apache.flink.runtime.executiongraph.ExecutionGraph.initializeJobVertex(ExecutionGraph.java:224)
        at org.apache.flink.runtime.executiongraph.DefaultExecutionGraph.initializeJobVertices(DefaultExecutionGraph.java:875)
        at org.apache.flink.runtime.executiongraph.DefaultExecutionGraph.attachJobGraph(DefaultExecutionGraph.java:829)
        at org.apache.flink.runtime.executiongraph.DefaultExecutionGraphBuilder.buildGraph(DefaultExecutionGraphBuilder.java:221)
        at org.apache.flink.runtime.scheduler.DefaultExecutionGraphFactory.createAndRestoreExecutionGraph(DefaultExecutionGraphFactory.java:163)
        at org.apache.flink.runtime.scheduler.SchedulerBase.createAndRestoreExecutionGraph(SchedulerBase.java:371)
        at org.apache.flink.runtime.scheduler.SchedulerBase.<init>(SchedulerBase.java:214)
        at org.apache.flink.runtime.scheduler.DefaultScheduler.<init>(DefaultScheduler.java:140)
        at org.apache.flink.runtime.scheduler.DefaultSchedulerFactory.createInstance(DefaultSchedulerFactory.java:156)
        at org.apache.flink.runtime.jobmaster.DefaultSlotPoolServiceSchedulerFactory.createScheduler(DefaultSlotPoolServiceSchedulerFactory.java:122)
        at org.apache.flink.runtime.jobmaster.JobMaster.createScheduler(JobMaster.java:379)
        at org.apache.flink.runtime.jobmaster.JobMaster.<init>(JobMaster.java:356)
        at org.apache.flink.runtime.jobmaster.factories.DefaultJobMasterServiceFactory.internalCreateJobMasterService(DefaultJobMasterServiceFactory.java:128)
        at org.apache.flink.runtime.jobmaster.factories.DefaultJobMasterServiceFactory.lambda$createJobMasterService$0(DefaultJobMasterServiceFactory.java:100)
        at org.apache.flink.util.function.FunctionUtils.lambda$uncheckedSupplier$4(FunctionUtils.java:112)
        ... 4 more
Caused by: java.lang.ClassCastException: cannot assign instance of org.apache.kafka.clients.consumer.OffsetResetStrategy to field org.apache
.flink.connector.kafka.source.enumerator.initializer.ReaderHandledOffsetsInitializer.offsetResetStrategy of type org.apache.kafka.clients.consumer.OffsetResetStrategy in instance of org.apache.flink.connector.kafka.source.enumerator.initializer.ReaderHandledOffsetsInitializer    
        at java.base/java.io.ObjectStreamClass$FieldReflector.setObjFieldValues(Unknown Source)
        at java.base/java.io.ObjectStreamClass$FieldReflector.checkObjectFieldValueTypes(Unknown Source)
        at java.base/java.io.ObjectStreamClass.checkObjFieldValueTypes(Unknown Source)
        at java.base/java.io.ObjectInputStream.defaultCheckFieldValues(Unknown Source)
        at java.base/java.io.ObjectInputStream.readSerialData(Unknown Source)
        at java.base/java.io.ObjectInputStream.readOrdinaryObject(Unknown Source)
        at java.base/java.io.ObjectInputStream.readObject0(Unknown Source)
        at java.base/java.io.ObjectInputStream.defaultReadFields(Unknown Source)
        at java.base/java.io.ObjectInputStream.readSerialData(Unknown Source)
        at java.base/java.io.ObjectInputStream.readOrdinaryObject(Unknown Source)
        at java.base/java.io.ObjectInputStream.readObject0(Unknown Source)
        at java.base/java.io.ObjectInputStream.defaultReadFields(Unknown Source)
        at java.base/java.io.ObjectInputStream.readSerialData(Unknown Source)
        at java.base/java.io.ObjectInputStream.readOrdinaryObject(Unknown Source)
        at java.base/java.io.ObjectInputStream.readObject0(Unknown Source)
        at java.base/java.io.ObjectInputStream.readObject(Unknown Source)
        at java.base/java.io.ObjectInputStream.readObject(Unknown Source)
        at org.apache.flink.util.InstantiationUtil.deserializeObject(InstantiationUtil.java:539)
        at org.apache.flink.util.InstantiationUtil.deserializeObject(InstantiationUtil.java:527)
        at org.apache.flink.util.SerializedValue.deserializeValue(SerializedValue.java:67)
        at org.apache.flink.runtime.operators.coordination.OperatorCoordinatorHolder.create(OperatorCoordinatorHolder.java:477)
        at org.apache.flink.runtime.executiongraph.ExecutionJobVertex.createOperatorCoordinatorHolder(ExecutionJobVertex.java:292)
        at org.apache.flink.runtime.executiongraph.ExecutionJobVertex.initialize(ExecutionJobVertex.java:225)
        ... 20 more
