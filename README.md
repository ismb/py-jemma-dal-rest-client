# py-jemma-dal-rest-client

This quick-and-dirty Python Client can be used to make calls to the JEMMA DAL.

# Examples

General usage:

```
./py-jemma-dal-rest-client -a <address-of-DAL-endpoint> -c <command> <command-specific-arguments>
```

## Getting devices list

```
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c listd 
```

## Getting the list of function of a device

```
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c listf -d "ZigBee:Meter Lamp:ah.app.5149012995480223-2"
```

## Performing operations

```
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c operate -d "ZigBee:Meter Lamp:ah.app.5149012995480223-2" -f "OnOff" -o "reverse"
```

## Reading a property

```
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c read -d "ZigBee:LEDStrip 6:ah.app.6623462354059559-11" -f "ColorControl" -p "HS"
```

## Writing a property


## Other misc examples

```
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c read -d "ZigBee:LEDStrip 6:ah.app.6623462354059559-11" -f "ColorControl" -p "HS"
./py-jemma-dal-rest-client.py -a 127.0.0.1 -c read -d "ZigBee:LEDStrip 6:ah.app.6623462354059559-11" -f "MultiLevelControl" -p "data"
```
