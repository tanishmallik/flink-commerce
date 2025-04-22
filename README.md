[user@dinm5CD42655LX FlinkCommerce]$ docker cp target/FlinkCommerce-1.0-SNAPSHOT.jar flinkcommerce-jobmanager-1:/opt/flink/lib/
Successfully copied 20.3MB to flinkcommerce-jobmanager-1:/opt/flink/lib/
[user@dinm5CD42655LX FlinkCommerce]$ docker exec -t flinkcommerce-jobmanager-1 /opt/flink/bin/flink run -c FlinkCommerce.DataStreamJob /opt/flink/lib/FlinkCommerce-1.0-SNAPSHOT.jar
WARNING: Unknown module: jdk.compiler specified to --add-exports
WARNING: Unknown module: jdk.compiler specified to --add-exports
WARNING: Unknown module: jdk.compiler specified to --add-exports
WARNING: Unknown module: jdk.compiler specified to --add-exports
WARNING: Unknown module: jdk.compiler specified to --add-exports
Job has been submitted with JobID 9ad266aad85cf17ad73fb85469db8117

------------------------------------------------------------
 The program finished with the following exception:

org.apache.flink.client.program.ProgramInvocationException: The main method caused an error: org.apache.flink.client.program.ProgramInvocationException: Job failed (JobID: 9ad266aad85cf17ad73fb85469db8117)
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
Caused by: java.util.concurrent.ExecutionException: org.apache.flink.client.program.ProgramInvocationException: Job failed (JobID: 9ad266aad85cf17ad73fb85469db8117)
        at java.base/java.util.concurrent.CompletableFuture.reportGet(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.get(Unknown Source)
        at org.apache.flink.client.program.StreamContextEnvironment.getJobExecutionResult(StreamContextEnvironment.java:171)
        at org.apache.flink.client.program.StreamContextEnvironment.execute(StreamContextEnvironment.java:122)
        at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.execute(StreamExecutionEnvironment.java:2099)
        at FlinkCommerce.DataStreamJob.main(DataStreamJob.java:33)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.base/java.lang.reflect.Method.invoke(Unknown Source)
        at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:355)
        ... 9 more
Caused by: org.apache.flink.client.program.ProgramInvocationException: Job failed (JobID: 9ad266aad85cf17ad73fb85469db8117)
        at org.apache.flink.client.deployment.ClusterClientJobClientAdapter.lambda$null$6(ClusterClientJobClientAdapter.java:130)
        at java.base/java.util.concurrent.CompletableFuture$UniApply.tryFire(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.postComplete(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.complete(Unknown Source)
        at org.apache.flink.util.concurrent.FutureUtils.lambda$retryOperationWithDelay$6(FutureUtils.java:302)
        at java.base/java.util.concurrent.CompletableFuture.uniWhenComplete(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.postComplete(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.complete(Unknown Source)
        at org.apache.flink.client.program.rest.RestClusterClient.lambda$pollResourceAsync$33(RestClusterClient.java:794)
        at java.base/java.util.concurrent.CompletableFuture.uniWhenComplete(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.postComplete(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.complete(Unknown Source)
        at org.apache.flink.util.concurrent.FutureUtils.lambda$retryOperationWithDelay$6(FutureUtils.java:302)
        at java.base/java.util.concurrent.CompletableFuture.uniWhenComplete(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.postComplete(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.postFire(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture$UniCompose.tryFire(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture$Completion.run(Unknown Source)
        at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
        at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
        at java.base/java.lang.Thread.run(Unknown Source)
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
        at java.base/java.util.concurrent.ForkJoinTask.doExec(Unknown Source)
        at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(Unknown Source)
        at java.base/java.util.concurrent.ForkJoinPool.scan(Unknown Source)
        at java.base/java.util.concurrent.ForkJoinPool.runWorker(Unknown Source)
        at java.base/java.util.concurrent.ForkJoinWorkerThread.run(Unknown Source)
Caused by: org.apache.flink.util.FlinkException: Global failure triggered by OperatorCoordinator for 'Source: Kafka source -> Sink: Print to Std. Out' (operator cbc357ccb763df2852fee8c4fc7d55f2).
        at org.apache.flink.runtime.operators.coordination.OperatorCoordinatorHolder$LazyInitializedCoordinatorContext.failJob(OperatorCoordinatorHolder.java:624)
        at org.apache.flink.runtime.operators.coordination.RecreateOnResetOperatorCoordinator$QuiesceableContext.failJob(RecreateOnResetOperatorCoordinator.java:248)
        at org.apache.flink.runtime.source.coordinator.SourceCoordinatorContext.failJob(SourceCoordinatorContext.java:395)
        at org.apache.flink.runtime.source.coordinator.SourceCoordinatorContext.handleUncaughtExceptionFromAsyncCall(SourceCoordinatorContext.java:408)      
        at org.apache.flink.util.ThrowableCatchingRunnable.run(ThrowableCatchingRunnable.java:42)
        at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Unknown Source)
        at java.base/java.util.concurrent.FutureTask.run(Unknown Source)
        at java.base/java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(Unknown Source)
        at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
        at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
        at java.base/java.lang.Thread.run(Unknown Source)
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
        at java.base/java.util.concurrent.CompletableFuture.reportGet(Unknown Source)
        at java.base/java.util.concurrent.CompletableFuture.get(Unknown Source)
        at org.apache.kafka.common.internals.KafkaFutureImpl.get(KafkaFutureImpl.java:165)
        at org.apache.flink.connector.kafka.source.enumerator.subscriber.KafkaSubscriberUtils.getTopicMetadata(KafkaSubscriberUtils.java:44)
        ... 9 more
Caused by: org.apache.kafka.common.errors.TimeoutException: Timed out waiting for a node assignment. Call: describeTopics
[user@dinm5CD42655LX FlinkCommerce]$ 
