## System design
- Funnel design
- Data collection
- Data modelling
- Data Analysis
- Data pipeline and assumption

### Funnel design
Once a website is build, a user has to go through multiple steps to reflect his engagement behaviour. 
Let's say it's a product website, then to finish a transaction usually a user will visit Home Page --> Product Page --> Checkout Page --> Order Page.
A funnel can be created to help analyse which step is causing dropouts, for instance if it shows there is a high bounce rate in product page, then the product may not be appealing, or some functional feature needs to be improved for better experience.
In terms of designing a funnel, for each step we add a specific url. This funnel includes all pages which should be visited, and to get more granular details, we can create custom metrics to assist behaviour analysis. 

### Data collection
Components: Web js(tracking code in frontend)  --> logs ---> database --> visualisation tool
- Frontend
> embed javascript code in the app/website so when a user arrives it will capture various data information of how the user engages with this website.

Information consists of user's behaviour in viewing, clicking, each event includes the user's browser configuration(browser name, device, ip address, location and operation system) as well as the url/page he/she viewed, hang on time, referral link.

Based on cookie data, will assign each visitor a unique identifier id, this can be used to analyse sessions, visit counts, total visit times. traffic sources and bounces.

- Backend
> all related logs will be streamed into backend database, for interactive query all events will be further sent to database which supports dml using standard sql via connectors.

### Data modelling
If we try to normalise data, we can find there are three aspects, starting with session as a fact table, there are three dimensions (user, page, location)
- Session: session_id, session_time and all other foreign keys which point to other dimension tables.
- User: visitor_id, channel, client. 
- Location: ip_address, city, country, language. 
- Page: page-view url, page_order, page_time, event (click/move, transaction, social share)

However we can also store data in data warehouse, where we allow redundant data in session tables to avoid cost from join other dimensions. An example for this is bigquery is gcp. Raw analytics data is streamed into bigquery with partitions everyday, and can be unnested/flatten and used for further aggregation.


### Data Analysis
```sql
-- 1) Within a given time range (example: Today, This Week, From 2018-10-1 to 2019-01-01, etc.).
SELECT date, 
SUM(totals.visits) AS sessions
FROM dataset.table1
GROUP BY date
-- 2) By channel (How does the funnel perform when user comes from Search vs. Paid ads).
SELECT trafficSource.medium, 
SUM(totals.newVisits) / SUM(totals.visits) AS percentNewSessions
FROM dataset.table1
GROUP BY trafficSource.medium
-- 3) By device (Browser vs. mobile)
SELECT device.operatingSystem, 
SUM(totals.visits) AS sessions
FROM dataset.table1
GROUP BY device.operatingSystem
```


### Data pipeline and assumption

- We are assuming visitor is doing single-session engagement, as it's hard to track how engagement turns into conversion (Homepage >> Product Page >> Checkout Page) if this visitor complete action in multiple sessions.
- The funnel built is aiming at page-to-page tracking, we assume each step is a web page. So it's not an event-oriented funnel.