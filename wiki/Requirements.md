# Requirements

## User
BEIS. CGI.

## Requirements Capture

- Fully deployed SaaS platform
- SPA, Vue.JS
- Containerized Deploy: Data Model, API
- Views: Map View
- Date Sources: Transmission Lines to the nearest store
- Data Groups: Weather, Costs, Existing Infrastructure
- Generaors: Wind Turbine, Solar Cells, Wave Turbine
- No preference in Generators
- Ignoring Waters
- OpenStreetMap
- River flow
- Overview over UK with Layers of information
- Micro view: Get location and show specific data
- Viability filters
- Get cost of land
- Dangers of Wind Turbines
- Cost Calculator: How long to pay it back

## Solar
- Is it close to demand, is it producing the maximum when its demand
- DOn't put solar when needed at night
- There is no holding of energy
- Historical demand energy is propriority
- Where and how much?
- Demand goes up based on the temperature

## Current

- Available land is taken us
- Topology maps
- Cliff faces: Sun facing.
- More expenisves.
- Sound facing on fields
- Cells oriented
- sunlight data
- Global demand
- Location to transmission lines
- BAIS has demand date 
- Cell temperature affect efficientcy
- Adding water improves efficiency. Currently done in china
- Transmission lines
- Don't focus on low level in terms of price
- Tranmission loss
- Life stock farms: Solar panels under sheets
- Lakes: Improved efficiency 
- Existing PVs and their data usage
- Upgradabilty
- Star rating shown in heat map
- Cornwall: Cheap land, losts of sun. But low demand and not connected to the rest of the line
- Don't upgrade because trasmission lines are too saturated
- Electricity costs are the same

## KPI
- What line I can get today (MVP)
- What about 30 years from now (Extension)

## Requirements Specification

### MVP

- Invite everyone to repo and slack
- Protect Master and Develop branches, Request 1 code Review
- Show the entire country 
- Create Mock data: Land value, Weather, Sunlight
- Decide Tiles levels
- Pre processing: Filter out cities/population density from data
- General land price
- Plot transmission lines
- PLot existing PVs
- Calculate minimum output to compensate for energy loss
- Sunlight score: Little sun the entire day. 
- Demand per tiles. Seperated in local and excess

### Dragons Den Presentation

### Extensions
- EVs location
- Upgradabltiy

### Finals Presentation