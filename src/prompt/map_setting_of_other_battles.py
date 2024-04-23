map_info_json_Agincourt = {
  "MapFeatures": {
    "NorthDirection": "Upwards",
    "Scale": {
      "ratio": "Each unit on the map corresponds to 10 yards in real-world distance"
    }
  },
  "Geography": {
    "VillageA": {
      "coordinates": [0, 0],
      "shape": {
        "area": "Not specified",
        "perimeter": "Not specified",
        "description": "The central village on the map, positioned at the presumed center of activity."
      },
      "properties": {
        "type": "Village"
      },
      "description": "central to the map's geography."
    },
    "VillageT": {
      "coordinates": [30, 10],
      "shape": {
        "area": "Not specified",
        "perimeter": "Not specified",
        "description": "Shape and size details of the village are not specified on the map."
      },
      "properties": {
        "type": "Village"
      },
      "description": "Located northeast of VillageA, connected by a road."
    },
    "VillageM": {
      "coordinates": [20, -30],
      "shape": {
        "area": "Not specified",
        "perimeter": "Not specified",
        "description": "Shape and size details of the village are not specified on the map."
      },
      "properties": {
        "type": "Village"
      },
      "description": "Located southeast of VillageA, at the end of the road that forks from the road to VillageT."
    },
    "Roads": {
      "path": {
        "description": "One main road depicted, connecting Agincourt and Tramecourt and forking towards VillageM."
      },
      "properties": {
        "type": "Road"
      },
      "description": "Main roadways connecting the villages."
    },
    "Terrain": {
      "description": "Varying textures represent different terrain such as open fields, possible forests or marshlands."
    }
  }
}



map_info_json_Falkirk = {
  "MapFeatures": {
    "NorthDirection": "Upwards",
    "Scale": {
      "ratio": "Each unit on the map corresponds to 10 yards in real-world distance"
    }
  },
  "Geography": {
    "ForestC": {
      "coordinates": [50, 150],
      "shape": {
        "area": "Not specified",
        "perimeter": "Not specified",
        "description": "Large forested area in the upper central part of the map."
      },
      "properties": {
        "type": "Forest"
      },
      "description": "Dense wooded area, significant in size."
    },
    "RiverB": {
      "path": {
        "start": [-100, -200],
        "end": [100, 50],
        "description": "Flow path of the river begins from the southwest corner towards the northeast."
      },
      "properties": {
        "type": "River"
      },
      "description": "Meandering waterway providing natural boundaries and obstacles."
    },
    "RoadF": {
      "coordinates": [-50, 200],
      "shape": {
        "area": "Not specified",
        "perimeter": "Not specified",
        "description": "Road running diagonally from northwest to southeast."
      },
      "properties": {
        "type": "Road"
      },
      "description": "Main thoroughfare leading to a significant location off-map."
    }
  }
}

map_info_json_Poitiers = {
    "MapFeatures": {
        "NorthDirection": "Upwards",
        "Scale": {
            "ratio": "Each unit on the map corresponds to 10 yards in real-world distance"
        }
    },
    "Geography": {
        "VillageP": {  # Poitiers
            "coordinates": [0, 0],
            "shape": {
                "area": "Not specified",
                "perimeter": "Not specified",
                "description": "Central village"
            },
            "properties": {
                "type": "Village"
            },
            "description": "Central village on the map"
        },
        "VillageN": {  # Nouaillé
            "coordinates": [100, -250],  # estimated position to the southeast of Poitiers
            "shape": {
                "area": "Not specified",
                "perimeter": "Not specified",
                "description": "Shape and size details of the village are not specified on the map."
            },
            "properties": {
                "type": "Village"
            },
            "description": "Southeast of VillageP, named as VillageN"
        },
        "RiverMain": {
            "path": {
                "start": [-200, 100],  # estimated start at the northwest corner
                "end": [0, -300],  # estimated end to the south of Nouaillé
                "description": "Meanders from northwest to southeast."
            },
            "properties": {
                "type": "River"
            },
            "description": "Main river, flows from the northwest past PositionP and down to the south."
        },
        "RiverBranch": {
            "path": {
                "start": [0, -100],  # estimated start at the branch from the main river near Poitiers
                "end": [150, -250],  # estimated end towards Nouaillé
                "description": "Branches off from the main river towards the southeast."
            },
            "properties": {
                "type": "River"
            },
            "description": "Branch of the main river flowing towards WoodN"
        },
        "WoodL": {
            "coordinates": [-150, 50],  # estimated position to the northwest of Poitiers
            "shape": {
                "area": "Not specified",
                "perimeter": "Not specified",
                "description": "Wooded area to the northwest."
            },
            "properties": {
                "type": "Forest"
            },
            "description": ""
        },
        "WoodN": {
            "coordinates": [100, -150],  # estimated position to the east of Poitiers
            "shape": {
                "area": "Not specified",
                "perimeter": "Not specified",
                "description": "Wooded area in the center-east."
            },
            "properties": {
                "type": "Forest"
            },
            "description": "Wood at central-eastern wooded area."
        },
        "WoodS": {
            "coordinates": [150, -350],  # estimated position to the southeast of Nouaillé
            "shape": {
                "area": "Not specified",
                "perimeter": "Not specified",
                "description": "Wooded area in the southeast."
            },
            "properties": {
                "type": "Forest"
            },
            "description": ""
        }
    }
}