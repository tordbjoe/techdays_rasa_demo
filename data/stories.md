## tell_joke happypath
* greet
  - utter_greet
* tell_joke
  - utter_tell_joke
  - action_restart


## chit_chat general
* greet
    - utter_greet
* chit_chat
    - utter_chitchat


## interactive_story_1
* ask_weather{"city_weather": "oslo"}
    - slot{"city_weather": "oslo"}
    - get_weather
    - action_restart

## interactive_story_2
* ask_weather{"city_weather": "copenhagen"}
    - slot{"city_weather": "copenhagen"}
    - get_weather
    - action_restart

## interactive_story_3
* ask_weather{"city_weather": "stockholm"}
    - slot{"city_weather": "stockholm"}
    - get_weather
    - action_restart

## interactive_story_1
* ask_weather{"city_weather": "oslo"}
    - slot{"city_weather": "oslo"}
    - get_weather
    - action_restart

## interactive_story_2
* ask_weather{"city_weather": "stockholm"}
    - slot{"city_weather": "stockholm"}
    - get_weather
    - action_restart

## interactive_story_3
* ask_weather{"city_weather": "copenhagen"}
    - slot{"city_weather": "copenhagen"}
    - get_weather
    - action_restart

## interactive_story_4
* ask_weather
    - utter_ask_weather
* greet{"city_weather": "oslo"}
    - slot{"city_weather": "oslo"}
    - get_weather
    - action_restart

## interactive_story_1
* chit_chat
    - utter_default
* chit_chat
    - utter_chitchat
* chit_chat
    - utter_chitchat
