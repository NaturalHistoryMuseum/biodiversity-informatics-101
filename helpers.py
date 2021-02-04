map_config = {
  "version": "v1",
  "option": {
      "readOnly": True
  },  
  "config": {
    "visState": {
    "filters": [
        {
          "dataId": [
            "occurrences"
          ],
          "id": "7gs4atm48",
          "name": [
            "eventDate"
          ],
          "type": "timeRange",
          "value": [
            1092528000000,
            1092528000000
          ],
          "enlarged": True,
          "plotType": "histogram",
          "animationWindow": "incremental",
          "yAxis": None,
          "speed": 1
        }
      ],
      "layers": [
        {
          "id": "t36ps5o",
          "type": "point",
          "config": {
            "dataId": "occurrences",
            "label": "Occurrences",
            "color": [
              231,
              159,
              213
            ],
            "columns": {
              "lat": "decimalLatitude",
              "lng": "decimalLongitude",
              "altitude": None
            },
            "isVisible": True,
            "visConfig": {
              "radius": 10,
              "fixedRadius": False,
              "opacity": 1,
              "outline": False,
              "thickness": 2,
              "strokeColor": None,
              "colorRange": {
                "name": "UberPool 6",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                    "#FFC300",
                    "#F1920E",
                    "#E3611C",
                    "#C70039",
                    "#900C3F",
                    "#5A1846"
                ],
                "reversed": True
              },            
              "radiusRange": [
                0,
                50
              ],
              "filled": True
            },
            "hidden": False,
            "textLabel": []
          },
          "visualChannels": {
            "colorField": {
              "name": "year",
              "type": "real"
            },
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "enabled": False
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "additive",
      "splitMaps": False,
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 50.4546023168623,
      "longitude": -8.399661861255069,
      "pitch": 0,
      "zoom": 3.8708398940534186,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [],
      "mapStyles": {}
    }
  }
}