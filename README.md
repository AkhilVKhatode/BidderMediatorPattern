# AuctionMediator Design Pattern in Python

This repository contains an implementation of the **Mediator Design Pattern** using an auction scenario. The system involves an `AuctionHouse` acting as a mediator that facilitates communication between multiple `Bidder` objects. The `AuctionHouse` accepts bids from bidders and notifies all other bidders of the placed bids.

## Structure

- `AuctionMediator`: An abstract class that defines the interface for registering bidders and placing bids.
- `AuctionHouse`: A concrete class that implements the `AuctionMediator` interface. It manages the bidders and places bids.
- `Bidder`: A class representing a bidder. Each bidder can place a bid and will be notified of others' bids.

## How It Works

1. **Registering Bidders**: Each bidder registers with the `AuctionHouse` (mediator).
2. **Placing a Bid**: When a bidder places a bid, the `AuctionHouse` receives it and notifies all other registered bidders.
3. **Notification**: All other bidders are notified when a bid is placed, including the bid amount and the bidder's name.

## Example Usage

The code demonstrates how to use the `AuctionHouse` and `Bidder` classes:

```python
if __name__ == "__main__":
    auction_house = AuctionHouse()
    bidder1 = Bidder("Alice", auction_house)
    bidder2 = Bidder("Bob", auction_house)
    bidder3 = Bidder("Charlie", auction_house)

    auction_house.register_bidder(bidder1)
    auction_house.register_bidder(bidder2)
    auction_house.register_bidder(bidder3)

    bidder1.place_bid(100)
    bidder2.place_bid(150)
    bidder3.place_bid(200)
```
Output:
```less
Alice placed a bid of 100
Bob is notified: Alice placed a bid of 100
Charlie is notified: Alice placed a bid of 100
Bob placed a bid of 150
Alice is notified: Bob placed a bid of 150
Charlie is notified: Bob placed a bid of 150
Charlie placed a bid of 200
Alice is notified: Charlie placed a bid of 200
Bob is notified: Charlie placed a bid of 200
```
