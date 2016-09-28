# waze_traffic_api

James Moore, JMoore335@gatech.edu

https://github.com/JMoore335/waze_traffic_api

Waze is a nagivation and traffic alert app from Google, available on Android and iOS. The app users send in alerts including wrecks, police (i.e. speed traps), traffic jams, debris on the road, etc.

This script calls real-time traffic data from the Waze API. Specifically, the script logs all police sightings in a contained area (here, the stretch of road between Atlanta and Nashville). The script refreshes the calls every 30 minutes, and logs the info into a CSV file. This would be great for data collection if you wanted to find hotspots of traffic/alerts activity.

The script can be modified by changing the coordinates of the area of which you want to find traffic alerts. You will find the coordinates in the requests URL. The coordinates contain the latitude-East/West and longitude-North/South, so you should have 4 sets of coordinates at the end.

Additionally, the script can be changed to view different traffic alerts. It is currently set to notify just for police sightings.

I have used the code to set up the local server from Nimrod007 (https://github.com/Nimrod007/waze-api).

### Installation

1. Download waze-server
```sh
wget https://github.com/Nimrod007/waze-api/releases/download/1.1/waze-server.jar
```

2. Run the waze-server (port 8080) (in a separate terminal)
```sh
java -jar waze-server.jar server
```

3. Run the script
```sh
python waze_script.py
```

### Resources
https://www.waze.com/

https://www.waze.com/about/dev
