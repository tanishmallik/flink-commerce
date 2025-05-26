import json
from confluent_kafka import Producer
from datetime import datetime, timezone

def charger_status_data():
    # Directly take input data — no logic applied here
    charger_groups = [
        {
            "charger_group_id": "g001",
            "chargers": [
                {"chargerId": "c001", "status": "Online"},
                {"chargerId": "c002", "status": "Online"},
                {"chargerId": "c003", "status": "Online"},
                {"chargerId": "c004", "status": "Online"},
                {"chargerId": "c005", "status": "Online"}
            ],
            
        },
        {
            "charger_group_id": "g002",
            "chargers": [
                {"chargerId": "c006", "status": "Engaged"},
                {"chargerId": "c007", "status": "Failure"},
                {"chargerId": "c008", "status": "Engaged"},
                {"chargerId": "c009", "status": "Engaged"},
                {"chargerId": "c010", "status": "Engaged"}
            ],
           
        },
        {
            "charger_group_id": "g003",
            "chargers": [
                {"chargerId": "c011", "status": "Online"},
                {"chargerId": "c012", "status": "Engaged"},
                {"chargerId": "c013", "status": "Online"},
                {"chargerId": "c014", "status": "Engaged"},
                {"chargerId": "c015", "status": "Online"}
            ],
            
        }
    ]

    charger_data = {
        "stationId": "station_001",
        "timestamp": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        "chargerGroups": charger_groups
    }

    return charger_data

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record {msg.key()} successfully produced to {msg.topic()} partition {msg.partition()}")

def main():
    kafka_conf = {
        'bootstrap.servers': 'localhost:9092',
    }

    producer = Producer(kafka_conf)
    topic = 'station_charger_status'

    charger_data = charger_status_data()
    message_key = charger_data['stationId']
    message_value = json.dumps(charger_data)

    producer.produce(topic=topic, key=message_key, value=message_value, callback=delivery_report)
    producer.flush()

if __name__ == "__main__":
    main()
