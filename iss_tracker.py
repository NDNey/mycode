#!/usr/bin/env python3

import requests
import time

URL= "http://api.open-notify.org/iss-now.json"

def main():
    resp= requests.get(URL).json()
    position = resp["iss_position"]
    print("CURRENT LOCATION OF THE ISS:")
    print("Timestamp: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(resp["timestamp"])))
    print(f"Lon: {position['longitude']}")
    print(f"Lat: {position['latitude']}")


if __name__ == "__main__":
    main()
