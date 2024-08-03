# ecowitt-gw2000
Ecowitt gw2000 python to save ecowitt metrics to influxdb 1.x for grafana 
1. Connect to the ecowitt API
2. fetch_ecowitt_data
3. transform_to_influxdb_line_protocol
4. send_to_influxdb

ubuntu@ip-172-31-13-23:~/ecowitt$ python3 toinflux.py

ecowitt.cypress.outdoor temperature=98.1 1722726464000000000
ecowitt.cypress.outdoor feels_like=111.2 1722726464000000000
ecowitt.cypress.outdoor app_temp=105.9 1722726464000000000
ecowitt.cypress.outdoor dew_point=75.0 1722726464000000000
ecowitt.cypress.outdoor humidity=48 1722726464000000000
ecowitt.cypress.indoor temperature=76.3 1722726464000000000
ecowitt.cypress.indoor humidity=52 1722726464000000000
ecowitt.cypress.solar_and_uvi solar=287.9 1722726464000000000
ecowitt.cypress.solar_and_uvi uvi=2 1722726464000000000
ecowitt.cypress.rainfall_piezo rain_rate=0.00 1722726464000000000
ecowitt.cypress.rainfall_piezo daily=0.00 1722726464000000000
ecowitt.cypress.rainfall_piezo event=0.00 1722726464000000000
ecowitt.cypress.rainfall_piezo hourly=0.00 1722726464000000000
ecowitt.cypress.rainfall_piezo weekly=0.00 1722726464000000000
ecowitt.cypress.rainfall_piezo monthly=0.00 1722726464000000000
ecowitt.cypress.rainfall_piezo yearly=0.00 1722726464000000000
ecowitt.cypress.wind wind_speed=4.5 1722726464000000000
ecowitt.cypress.wind wind_gust=4.5 1722726464000000000
ecowitt.cypress.wind wind_direction=288 1722726464000000000
ecowitt.cypress.pressure relative=29.72 1722726464000000000
ecowitt.cypress.pressure absolute=29.72 1722726464000000000
ecowitt.cypress.temp_and_humidity_ch1 temperature=70.7 1722726464000000000
ecowitt.cypress.temp_and_humidity_ch1 humidity=54 1722726464000000000
ecowitt.cypress.battery haptic_array_battery=3.18 1722726464000000000
ecowitt.cypress.battery haptic_array_capacitor=5.4 1722726464000000000
ecowitt.cypress.battery temp_humidity_sensor_ch1=0 1722726464000000000


Data written successfully to InfluxDB
