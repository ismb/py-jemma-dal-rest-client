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
