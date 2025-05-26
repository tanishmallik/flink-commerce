package FlinkCommerce;

import Deserializer.StationChargerStatusDeserializationSchema;
import Dto.StationChargerStatus;
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class DataStreamJob {

	public static void main(String[] args) throws Exception {
		final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

		String topic = "station_charger_status"; // use your exact Kafka topic name here

		KafkaSource<StationChargerStatus> source = KafkaSource.<StationChargerStatus>builder()
				.setBootstrapServers("localhost:9092")
				.setTopics(topic)
				.setGroupId("flink-group")
				.setStartingOffsets(OffsetsInitializer.earliest())
				.setValueOnlyDeserializer(new StationChargerStatusDeserializationSchema())
				.build();

		DataStream<StationChargerStatus> stream = env.fromSource(source, WatermarkStrategy.noWatermarks(), "Kafka Source");

		// Print the incoming objects to verify deserialization
		stream.print();

		env.execute("Station Charger Status Streaming Job");
	}
}
