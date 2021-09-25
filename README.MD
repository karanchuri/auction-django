# Auction System Micro Service

## Stack:
1. Django
2. Redis

## Basic Concept:
1. When auction is created its detials are stored in redis cache
2. Bidders poll to that cache instead of auctioneer sending request to all bidders (with this it can scale to many bidders efficiently) .
3. Bidders send HTTP request to Auction system. If bid is greater than current bid it is replaced
4. After 200 ms wait on that endpoint whatever bid is set on cache is being send back to the auctioneer

## Docker Setup:
Easy Setup:
```
chmod u+x build.sh
./build.sh
```

Step 1 (Build):
```bash
docker build -t greedy_games/auction_system:latest .
```
Step 2 (Start):
```bash
docker-compose up -d
```

## Debug:
### Logs:
1. Main auction service
```bash
docker-compose logs --follow --tail=100 auction-system-main
```
2. Bidder
```bash
docker-compose logs --follow --tail=100 auction_system_bidder_1
```
### Exec:
1. Exec in server
```bash
docker-compose exec auction-system-main bash
```

## Start an auction:
```
http://127.0.0.1:9000/api/auctionms/api/create-auction?auction_id=1
```

## Clear channel:
```
http://127.0.0.1:9000/api/auctionms/api/clear-bid-channel
```

## Happy Developing ❤
