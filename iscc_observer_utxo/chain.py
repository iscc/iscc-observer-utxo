"""Blockchain client"""
import iscc_observer_utxo as observer
from bitcoin.rpc import Proxy

__all__ = ["chain", "ch"]


ch = None


def chain() -> Proxy:
    global ch
    if ch is None:
        ch = Proxy(service_url=observer.config.node_service_url)
    return ch
