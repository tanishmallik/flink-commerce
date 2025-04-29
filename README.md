
when running the flink locally
[user@dinm5CD42655LX flink-1.18.0]$ ./bin/start-cluster.sh
Starting cluster.
Starting standalonesession daemon on host dinm5CD42655LX.
Starting taskexecutor daemon on host dinm5CD42655LX.
[user@dinm5CD42655LX flink-1.18.0]$ cd
[user@dinm5CD42655LX ~]$


[user@dinm5CD42655LX FlinkCommerce]$ /mnt/c/Dev/flink-1.18.0-bin-scala_2.12/flink-1.18.0/bin/flink run -c FlinkCommerce.DataStreamJob /mnt/c/Users/z00505yp/workspace/FlinkCommerce/target/FlinkCommerce-1.0-SNAPSHOT.jar
Job has been submitted with JobID 25e9e5191ccddb1b45304623ab875ce2

------------------------------------------------------------
 The program finished with the following exception:

org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: org.apache.flink.client.program.ProgramInvocationException: Job failed (JobID: 25e9e5191ccddb1b45304623ab875ce2)
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
Caused by: java.util.concurrent.ExecutionException: org.apache.flink.client.program.ProgramInvocationException: Job failed (JobID: 25e9e5191ccddb1b45304623ab875ce2)
        at java.base/java.util.concurrent.CompletableFuture.reportGet(CompletableFuture.java:395)
        at java.base/java.util.concurrent.CompletableFuture.get(CompletableFuture.java:2005)
        at org.apache.flink.client.program.StreamContextEnvironment.getJobExecutionResult(StreamContextEnvironment.java:171)
        at org.apache.flink.client.program.StreamContextEnvironment.execute(StreamContextEnvironment.java:122)
        at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.execute(StreamExecutionEnvironment.java:2099)
        at FlinkCommerce.DataStreamJob.main(DataStreamJob.java:33)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.base/java.lang.reflect.Method.invoke(Method.java:566)
        at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:355)
        ... 9 more
Caused by: org.apache.flink.client.program.ProgramInvocationException: Job failed (JobID: 25e9e5191ccddb1b45304623ab875ce2)
        at org.apache.flink.client.deployment.ClusterClientJobClientAdapter.lambda$null$6(ClusterClientJobClientAdapter.java:130)
        at java.base/java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:642)
        at java.base/java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:506)
        at java.base/java.util.concurrent.CompletableFuture.complete(CompletableFuture.java:2079)
        at org.apache.flink.util.concurrent.FutureUtils.lambda$retryOperationWithDelay$6(FutureUtils.java:302)
        at java.base/java.util.concurrent.CompletableFuture.uniWhenComplete(CompletableFuture.java:859)
        at java.base/java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(CompletableFuture.java:837)
        at java.base/java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:506)
        at java.base/java.util.concurrent.CompletableFuture.complete(CompletableFuture.java:2079)
        at org.apache.flink.client.program.rest.RestClusterClient.lambda$pollResourceAsync$33(RestClusterClient.java:794)
        at java.base/java.util.concurrent.CompletableFuture.uniWhenComplete(CompletableFuture.java:859)
        at java.base/java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(CompletableFuture.java:837)
        at java.base/java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:506)
        at java.base/java.util.concurrent.CompletableFuture.complete(CompletableFuture.java:2079)
        at org.apache.flink.util.concurrent.FutureUtils.lambda$retryOperationWithDelay$6(FutureUtils.java:302)
        at java.base/java.util.concurrent.CompletableFuture.uniWhenComplete(CompletableFuture.java:859)
        at java.base/java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(CompletableFuture.java:837)
        at java.base/java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:506)
        at java.base/java.util.concurrent.CompletableFuture.postFire(CompletableFuture.java:610)
        at java.base/java.util.concurrent.CompletableFuture$UniCompose.tryFire(CompletableFuture.java:1085)
        at java.base/java.util.concurrent.CompletableFuture$Completion.run(CompletableFuture.java:478)
        at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)
        at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)
        at java.base/java.lang.Thread.run(Thread.java:829)
Caused by: org.apache.flink.runtime.client.JobExecutionException: Job execution failed.
        at org.apache.flink.runtime.jobmaster.JobResult.toJobExecutionResult(JobResult.java:144)
        at org.apache.flink.client.deployment.ClusterClientJobClientAdapter.lambda$null$6(ClusterClientJobClientAdapter.java:128)
        ... 23 more
Caused by: org.apache.flink.runtime.JobException: Recovery is suppressed by NoRestartBackoffTimeStrategy
        at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.handleFailure(ExecutionFailureHandler.java:176)
        at org.apache.flink.runtime.executiongraph.failover.flip1.ExecutionFailureHandler.getGlobalFailureHandlingResult(ExecutionFailureHandler.java:126)   
        at org.apache.flink.runtime.scheduler.DefaultScheduler.handleGlobalFailure(DefaultScheduler.java:328)
        at org.apache.flink.runtime.operators.coordination.OperatorCoordinatorHolder$LazyInitializedCoordinatorContext.lambda$failJob$0(OperatorCoordinatorHolder.java:642)
        at org.apache.flink.runtime.rpc.pekko.PekkoRpcActor.lambda$handleRunAsync$4(PekkoRpcActor.java:451)
        at org.apache.flink.runtime.concurrent.ClassLoadingUtils.runWithContextClassLoader(ClassLoadingUtils.java:68)
        at org.apache.flink.runtime.rpc.pekko.PekkoRpcActor.handleRunAsync(PekkoRpcActor.java:451)
        at org.apache.flink.runtime.rpc.pekko.PekkoRpcActor.handleRpcMessage(PekkoRpcActor.java:218)
        at org.apache.flink.runtime.rpc.pekko.FencedPekkoRpcActor.handleRpcMessage(FencedPekkoRpcActor.java:85)
        at org.apache.flink.runtime.rpc.pekko.PekkoRpcActor.handleMessage(PekkoRpcActor.java:168)
        at org.apache.pekko.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:33)
        at org.apache.pekko.japi.pf.UnitCaseStatement.apply(CaseStatements.scala:29)
        at scala.PartialFunction.applyOrElse(PartialFunction.scala:127)
        at scala.PartialFunction.applyOrElse$(PartialFunction.scala:126)
        at org.apache.pekko.japi.pf.UnitCaseStatement.applyOrElse(CaseStatements.scala:29)
        at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:175)
        at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:176)
        at scala.PartialFunction$OrElse.applyOrElse(PartialFunction.scala:176)
        at org.apache.pekko.actor.Actor.aroundReceive(Actor.scala:547)
        at org.apache.pekko.actor.Actor.aroundReceive$(Actor.scala:545)
        at org.apache.pekko.actor.AbstractActor.aroundReceive(AbstractActor.scala:229)
        at org.apache.pekko.actor.ActorCell.receiveMessage(ActorCell.scala:590)
        at org.apache.pekko.actor.ActorCell.invoke(ActorCell.scala:557)
        at org.apache.pekko.dispatch.Mailbox.processMailbox(Mailbox.scala:280)
        at org.apache.pekko.dispatch.Mailbox.run(Mailbox.scala:241)
        at org.apache.pekko.dispatch.Mailbox.exec(Mailbox.scala:253)
        at java.base/java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:290)
        at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1020)
        at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:1656)
        at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1594)
        at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:183)
Caused by: org.apache.flink.util.FlinkException: Global failure triggered by OperatorCoordinator for 'Source: Kafka source -> Sink: Print to Std. Out' (operator cbc357ccb763df2852fee8c4fc7d55f2).
        at org.apache.flink.runtime.operators.coordination.OperatorCoordinatorHolder$LazyInitializedCoordinatorContext.failJob(OperatorCoordinatorHolder.java:624)
        at org.apache.flink.runtime.operators.coordination.RecreateOnResetOperatorCoordinator$QuiesceableContext.failJob(RecreateOnResetOperatorCoordinator.java:248)
        at org.apache.flink.runtime.source.coordinator.SourceCoordinatorContext.failJob(SourceCoordinatorContext.java:395)
        at org.apache.flink.runtime.source.coordinator.SourceCoordinatorContext.handleUncaughtExceptionFromAsyncCall(SourceCoordinatorContext.java:408)      
        at org.apache.flink.util.ThrowableCatchingRunnable.run(ThrowableCatchingRunnable.java:42)
        at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
        at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
        at java.base/java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:304)
        at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)
        at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)
        at java.base/java.lang.Thread.run(Thread.java:829)
Caused by: org.apache.flink.util.FlinkRuntimeException: Failed to list subscribed topic partitions due to
        at org.apache.flink.connector.kafka.source.enumerator.KafkaSourceEnumerator.checkPartitionChanges(KafkaSourceEnumerator.java:248)
        at org.apache.flink.runtime.source.coordinator.ExecutorNotifier.lambda$null$1(ExecutorNotifier.java:83)
        at org.apache.flink.util.ThrowableCatchingRunnable.run(ThrowableCatchingRunnable.java:40)
        ... 6 more
Caused by: java.lang.RuntimeException: Failed to get metadata for topics [financial_transactions].
        at org.apache.flink.connector.kafka.source.enumerator.subscriber.KafkaSubscriberUtils.getTopicMetadata(KafkaSubscriberUtils.java:47)
        at org.apache.flink.connector.kafka.source.enumerator.subscriber.TopicListSubscriber.getSubscribedTopicPartitions(TopicListSubscriber.java:52)       
        at org.apache.flink.connector.kafka.source.enumerator.KafkaSourceEnumerator.getSubscribedTopicPartitions(KafkaSourceEnumerator.java:233)
        at org.apache.flink.runtime.source.coordinator.ExecutorNotifier.lambda$notifyReadyAsync$2(ExecutorNotifier.java:80)
        ... 6 more
Caused by: java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.TimeoutException: Timed out waiting for a node assignment. Call: describeTopics
        at java.base/java.util.concurrent.CompletableFuture.reportGet(CompletableFuture.java:395)
        at java.base/java.util.concurrent.CompletableFuture.get(CompletableFuture.java:2005)
        at org.apache.kafka.common.internals.KafkaFutureImpl.get(KafkaFutureImpl.java:165)
        at org.apache.flink.connector.kafka.source.enumerator.subscriber.KafkaSubscriberUtils.getTopicMetadata(KafkaSubscriberUtils.java:44)
        ... 9 more
Caused by: org.apache.kafka.common.errors.TimeoutException: Timed out waiting for a node assignment. Call: describeTopics
[user@dinm5CD42655LX FlinkCommerce]$

