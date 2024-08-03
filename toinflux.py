# code to read from the ecowitt API and write to influx 1.x.   then setup a influx datasource in grafana pretty dashboards


import requests
import json

def fetch_ecowitt_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()


def transform_to_influxdb_line_protocol(data):
    lines = []
    timestamp = data.get('time', '') + '000000000'  # Add nanoseconds to the timestamp if needed

    # Process all measurement categories in the 'data' field
    for category, measurements in data.get('data', {}).items():
        for field_key, field_value in measurements.items():
            if isinstance(field_value, dict):
                measurement_path = f"ecowitt.cypress.{category}"

                # Extract the value and construct the line
                value = field_value.get('value', '')
                if value:
                    line = f"{measurement_path} {field_key}={value} {timestamp}"
                    lines.append(line)

    return "\n".join(lines)


def send_to_influxdb(influxdb_url, db_name, line_protocol_data):
    url = f"{influxdb_url}/write?db={db_name}"
    headers = {'Content-Type': 'text/plain'}
    try:
        response = requests.post(url, data=line_protocol_data, headers=headers, timeout=30)
        #print("Request URL:", url)
        #print("Request Data:", line_protocol_data)
        #print("Response Status Code:", response.status_code)
        #print("Response Text:", response.text)
        if response.status_code == 204:
            print("Data written successfully to InfluxDB")
        else:
            print(f"Failed to write data: {response.status_code} {response.text}")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


def main():
    ecowitt_url = 'https://api.ecowitt.net/api/v3/device/real_time?application_key=YOURAPPKEY&api_key=YOURAPIKEY&mac=YOURMAC-XX:XX:XX:XX:XX&call_back=all'  # Replace with your Ecowitt URL
    influxdb_url = 'http://YOURINFLUXSERVER:8086'
    db_name = 'ecowitt'

    # Fetch data from Ecowitt URL
    ecowitt_data = fetch_ecowitt_data(ecowitt_url)

    # Print the type and raw fetched data for debugging
    #print("Type of Raw Ecowitt Data:", type(ecowitt_data))
    #print("Raw Ecowitt Data:")
    #print(json.dumps(ecowitt_data, indent=2))

    # Transform data to InfluxDB line protocol format
    line_protocol_data = transform_to_influxdb_line_protocol(ecowitt_data)

    # Print the line protocol data for debugging
    #print("Line Protocol Data:")
    #print(line_protocol_data)

    # Send data to InfluxDB
    send_to_influxdb(influxdb_url, db_name, line_protocol_data)

if __name__ == "__main__":
    main()

