from seahorse.prelude import *

declare_id('BQ98Z2xeGEebzdVjdYJjKbKWuBHNFhpDNX2Y8ssKcCbz')


class Product(Account):
    owner: Pubkey
    author: Pubkey
    uid: str
    price: u64
    price_one_time: u64
    allow_bid: bool


class Profile(Account):
    owner: Pubkey
    token_account: Pubkey


class Offer(Account):
    owner: Pubkey
    product: Pubkey
    offer_price: u64
    offer_method: str
    product_owner: Pubkey
    status: str


class Order(Account):
    owner: Pubkey
    product: Pubkey
    product_owner: Pubkey
    status: str


@instruction
def create_product(owner: Signer, product: Empty[Product], uid: str, price: u64, price_one_time: u64, allow_bid: bool):
    product = product.init(payer=owner, seeds=['create_product', owner, uid])
    product.owner = owner.key()
    product.author = owner.key()
    product.uid = uid
    product.price = price
    product.price_one_time = price_one_time
    product.allow_bid = allow_bid


@instruction
def create_offer(owner: Signer, offer: Empty[Offer], product: Product, offer_price: u64, offer_method: str):
    offer = offer.init(payer=owner, seeds=['create_offer', owner, product.key(), product.owner])
    offer.owner = owner.key()
    offer.product_owner = product.owner
    offer.product = product.key()
    offer.offer_price = offer_price
    offer.offer_method = offer_method
    offer.status = 'created'


@instruction
def create_oder(signer: Signer, order: Empty[Order], product: Product,
                product_owner: TokenAccount):
    assert product_owner.key() == product.owner, 'Need transfer token to product owner'

    order = order.init(payer=signer, seeds=['create_oder', signer, product.uid])
    order.owner = signer.key()
    order.product = product.key()
    signer.transfer_lamports(product_owner, product.price)
    order.status = 'paid'


@instruction
def confirm_offer(signer: Signer, offer: Offer, product_owner_account: TokenAccount):
    # only the product owner can confirm the offer
    assert signer.key() == offer.product_owner, 'Only the product owner can confirm the offer'
    assert product_owner_account.key() == offer.product_owner, 'Need transfer token to product owner'
    signer.transfer_lamports(product_owner_account, offer.offer_price)
    offer.status = 'confirmed'


@instruction
def cancel_offer(signer: Signer, offer: Offer):
    # only the offer owner can cancel the offer
    assert signer.key() == offer.owner, 'Only the offer owner can cancel the offer'
    offer.status = 'cancelled'


@instruction
def create_profile(signer: Signer, account: Empty[Profile], tokenAccount: TokenAccount):
    account = account.init(payer=signer, seeds=['create_account', signer])
    account.owner = signer.key()
    account.token_account = tokenAccount.key()
