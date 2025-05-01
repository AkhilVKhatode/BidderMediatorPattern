from abc import ABC, abstractmethod

class AuctionMediator(ABC):
    @abstractmethod
    def register_bidder(self, bidder):
        pass

    @abstractmethod
    def place_bid(self, bidder, amount):
        pass


class AuctionHouse(AuctionMediator):
    def __init__(self):
        self.bidders = []

    def register_bidder(self, bidder):
        self.bidders.append(bidder)

    def place_bid(self, bidder, amount):
        print(f"{bidder.get_name()} placed a bid of {amount}")
        for b in self.bidders:
            if b != bidder:
                b.receive_bid(bidder, amount)


class Bidder:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def get_name(self):
        return self.name

    def place_bid(self, amount):
        self.mediator.place_bid(self, amount)

    def receive_bid(self, bidder, amount):
        print(f"{self.name} is notified: {bidder.get_name()} placed a bid of {amount}")


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
