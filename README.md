# py-jemma-dal-rest-client

This quick-and-dirty Python Client can be used to make calls to the JEMMA DAL.
JEMMA DAL API documentation cane be found [here](https://github.com/ismb/it.ismb.pert.osgi.dal.web-apis).

# Examples

General usage:

```
./py-jemma-dal-rest-client -a <address-of-DAL-endpoint> -p <DAL-port> -c <command> <command-specific-arguments>
```

## Getting devices list

```
./py-jemma-dal-rest-client.py -a 127.0.0.1:8080 -c listd 
```

## Getting the list of function of a device

```
./py-jemma-dal-rest-client.py -a 127.0.0.1:8080 -c listf -d "ZigBee:ah.app.3521399293210526201-8"
```

## Performing operations

```
./py-jemma-dal-rest-client.py -a 127.0.0.1:8080 -c operate -d "ZigBee:ah.app.3521399293210526201-8" -f "OnOff" -o "reverse"
```

## Reading a property

```
./py-jemma-dal-rest-client.py -a 127.0.0.1:8080 -c read -d "ZigBee:ah.app.3521399293210526201-8" -f "EnergyMeter" -p "current"
```

## Writing a property

```
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c write -d "ZigBee:LEDStrip 6:ah.app.6623462354059559-11" -f "ColorControl" -p "data" -v '[{"type":"java.lang.Short","value":"168"},{"type":"java.lang.Short","value":"253"}]'
```

## Unsorted/misc examples

```
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c listd 
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c listf -d "ZigBee:Meter Lamp:ah.app.5149012995480223-2"
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c operate -d "ZigBee:Meter Lamp:ah.app.5149012995480223-2" -f "OnOff" -o "reverse"
./py-jemma-dal-rest-client.py -a 127.0.0.1 -d "ZigBee:LEDStrip 6:ah.app.6623462354059559-11" -f "ColorControl" -c read -p "HS"
./py-jemma-dal-rest-client.py -a 127.0.0.1 -d "ZigBee:LEDStrip 6:ah.app.6623462354059559-11" -f "MultiLevelControl" -c read -p "data"
./py-jemma-dal-rest-client.py -a 127.0.0.1 -d "ZigBee:Striscia 6:ah.app.6623462354059559-11" -f "MultiLevelControl" -c write  -p "data" -v '[{"type":"java.math.BigDecimal","value":"0"}]'
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c write -d "ZigBee:Striscia 6:ah.app.6623462354059559-11" -f "ColorControl" -p "HS" -v '[{"type":"java.lang.Short","value":"168"},{"type":"java.lang.Short","value":"253"}]'
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c write -d "ZigBee:LEDStrip 6:ah.app.6623462354059559-11" -f "ColorControl" -p "data" -v '[{"type":"java.lang.Short","value":"168"},{"type":"java.lang.Short","value":"253"}]'
```

## Example Scripts

Here some examples of script which work in my home setup (4 hues + 2 strips + 1 disco ball)

```
python example_rolling_red_light.py
python example_alternate_lights.py
python example_rotating_lights.py 
python example_random_disco.py

```

# Credits

Developed by Riccardo Tomasi.
