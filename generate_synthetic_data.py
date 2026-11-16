
import csv
import random
from pathlib import Path
from datetime import datetime, timedelta

random.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

locations = [
    "Mumbai", "Pune", "Delhi", "Chennai", "Bengaluru",
    "Hyderabad", "Kolkata", "Ahmedabad", "Jaipur", "Nagpur",
    "Surat", "Lucknow", "Indore", "Goa", "Kochi"
]

# 1. CONTAINERS: 1,000 records
containers = []

for i in range(1, 1001):
    containers.append({
        "container_id": f"CONT{i:04}",
        "container_type": random.choice(["Reefer", "Insulated", "Standard"]),
        "capacity": random.choice([20, 40]),
        "manufacturer": random.choice(["Carrier", "Thermo King", "Daikin"]),
        "temperature_limit_min": -5,
        "temperature_limit_max": random.choice([4, 5, 8])
    })

# 2. SHIPMENTS: 5,000 records
shipments = []

for i in range(1, 5001):
    dispatch = datetime(2026, 1, 1) + timedelta(
        days=random.randint(0, 300)
    )
    expected = dispatch + timedelta(days=random.randint(2, 15))
    actual = expected + timedelta(days=random.choice([0, 0, 0, 1, 2, 3]))

    source = random.choice(locations)
    destination = random.choice([x for x in locations if x != source])

    shipments.append({
        "shipment_id": f"SHIP{i:05}",
        "container_id": f"CONT{random.randint(1, 1000):04}",
        "source_location": source,
        "destination_location": destination,
        "dispatch_date": dispatch.strftime("%Y-%m-%d"),
        "expected_delivery_date": expected.strftime("%Y-%m-%d"),
        "actual_delivery_date": actual.strftime("%Y-%m-%d"),
        "distance_km": random.randint(200, 3000),
        "transportation_cost": round(random.uniform(15000, 150000), 2),
        "shipment_status": random.choices(
            ["Delivered", "In Transit", "Delayed"],
            weights=[65, 20, 15]
        )[0]
    })

# 3. TEMPERATURE READINGS: 100,000 records
temperature_readings = []

for i in range(1, 100001):
    shipment = random.choice(shipments)
    start = datetime.strptime(shipment["dispatch_date"], "%Y-%m-%d")
    timestamp = start + timedelta(
        hours=random.randint(0, 24 * 20)
    )

    temperature = (
        random.uniform(6, 15)
        if random.random() < 0.12
        else random.uniform(-3, 5)
    )

    temperature_readings.append({
        "reading_id": f"READ{i:06}",
        "container_id": shipment["container_id"],
        "shipment_id": shipment["shipment_id"],
        "reading_timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "temperature_c": round(temperature, 2),
        "humidity_percent": round(random.uniform(35, 95), 2),
        "location": random.choice(locations)
    })

# 4. REROUTE OPTIONS: 10,000 records
reroute_options = []

for i in range(1, 10001):
    shipment = random.choice(shipments)

    alternative = random.choice([
        x for x in locations
        if x != shipment["destination_location"]
    ])

    reroute_options.append({
        "reroute_id": f"ROUTE{i:05}",
        "shipment_id": shipment["shipment_id"],
        "alternative_destination": alternative,
        "additional_distance_km": random.randint(20, 600),
        "estimated_cost": round(random.uniform(5000, 40000), 2),
        "estimated_time_hours": random.randint(2, 72),
        "expected_temperature": round(random.uniform(-3, 12), 2),
        "recommendation_status": random.choice([
            "Recommended", "Alternative", "Not Recommended"
        ])
    })

# Save all datasets as CSV files
datasets = {
    "containers.csv": containers,
    "shipments.csv": shipments,
    "temperature_readings.csv": temperature_readings,
    "reroute_options.csv": reroute_options
}

for filename, records in datasets.items():
    with open(DATA_DIR / filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

print("\nAll datasets generated successfully!")

for filename, records in datasets.items():
    print(f"{filename}: {len(records):,} records")

print(f"\nTotal records: {sum(len(r) for r in datasets.values()):,}")
print(f"Saved in: {DATA_DIR}")
