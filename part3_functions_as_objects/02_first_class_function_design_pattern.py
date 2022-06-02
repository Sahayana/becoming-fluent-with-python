'''
 디자인 패턴에 참여하는 일부 클래스의 객체를 간단한 함수로 교체하면 획일적으로 반복되는 코드의 상당부분을 줄일 수 있다.
'''

## 1. 전략 패턴의 리팩토링


'''
1-1 고전적인 전략 : UML(Unified Modeling Language) 클래스 다이어그램 (https://sabarada.tistory.com/72)
 컨텍스트: 일부 계산을 서로 다른 알고리즘을 구현하는 교환 가능한 컴포넌트에 위임함으로써 서비스 제공
 전략: 여러 알고리즘을 구현하는 컴포턴트에 공통된 인터페이스
 구체적 전략: 전략의 구상 서브클래스 중 하나
'''

from abc import ABC, abstractmethod
from collections import namedtuple



Customer = namedtuple('Customer', 'name fidelity') 

class Lineitem:

    def __init__(self, product, quantity, price) -> None:
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity 


class Order:    # 컨텍스트

    def __init__(self, customer, cart, promotion = None) -> None:
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self) -> str:
        return "<Order total: {:.2f} due: {:.2f}>".format(self.total(), self.due())
    

class Promotion(ABC):   # 전략: 추상 베이스 클래스, 추상클래스란 미구현 추상메소드를 한개 이상 가지며, 자식클래스에서 해당 추상 메소드를 반드시 구현하도록 강제

    @abstractmethod
    def discount(self, order):
        """할인액을 구체적 숫자로 반환"""
        

class FidelityPromotion(Promotion): # 첫번째 구체적 전략
    '''충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인'''
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromotion(Promotion): # 두번째 구체적 전략
    '''20개 이상의 동일 상품을 구입하면 10% 할인 적용'''
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromotion(Promotion): # 세번째 구체적 전략
    '''10종류 이상의 상품을 구입하면 전체 7% 할인 적용'''
    def discount(self, order):
        discount_item = {item.product for item in order.cart}
        if len(discount_item) >= 10:
            return order.total() * 0.07
        return 0


yang = Customer('Yang', 0)
geum = Customer('Geum', 1000)

cart = [
    Lineitem('Iphone', 4, 5000),
    Lineitem('Galaxy',10, 3000),
    Lineitem("BlackBerry", 5, 6000),
    ]

yang_order = Order(yang, cart=cart, promotion=FidelityPromotion())
geum_order = Order(geum, cart=cart, promotion=FidelityPromotion())
print('yang_order:',yang_order)
print('geum_order:',geum_order)

bulk_cart = [
    Lineitem('Iphone', 20, 5000),
    Lineitem('Galaxy',10, 3000),
]

bluk_order = Order(yang, cart=bulk_cart, promotion=BulkItemPromotion())
print('bluk_order:',bluk_order)

large_cart = [Lineitem(str(i), 1, 1000) for i in range(1, 21)]
large_order = Order(yang, cart=large_cart, promotion=LargeOrderPromotion())
print('large_order:',large_order)


'''
1-2 함수지향 전략 : 추상 클래스를 제거한 리팩토링
 구체적인 전략 객체가 내부 상태를 가지지 않고 단지 콘텍스트에서 오는 데이터를 처리하는 경우라면,
 다른 클래스를 정의하기 보다 일반 함수를 만드는 것이 좋다.
'''

class NewOrder(Order):
    
    def due(self):
        if self.promotion is None:
            discount = 0
        discount = self.promotion(self)
        return self.total() - discount    
    


def fidelity_promo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

def bulk_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

def large_promo(order):
    discount_item = {item.product for item in order.cart}
    if len(discount_item) >= 10:
        return order.total() * 0.07
    return 0


yang_order = NewOrder(yang, cart=cart, promotion=fidelity_promo)
geum_order = NewOrder(geum, cart=cart, promotion=fidelity_promo)
print('yang_order:',yang_order)
print('geum_order:',geum_order)

bulk_cart = [
    Lineitem('Iphone', 20, 5000),
    Lineitem('Galaxy',10, 3000),
]

bluk_order = NewOrder(yang, cart=bulk_cart, promotion=bulk_promo)
print('bluk_order:',bluk_order)

large_cart = [Lineitem(str(i), 1, 1000) for i in range(1, 21)]
large_order = NewOrder(yang, cart=large_cart, promotion=large_promo)
print('large_order:',large_order)