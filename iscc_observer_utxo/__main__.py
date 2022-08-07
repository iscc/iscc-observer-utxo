# -*- coding: utf-8 -*-
from loguru import logger as log
import click
import iscc_core as ic
import iscc_observer_utxo as observer


@click.command()
@click.argument("envfile", default=".env.dev")
def main(envfile):
    observer.config = observer.ObserverSettings(_env_file=envfile)
    log.info(f" --> starting utxo observer")
    log.info(f"version: {observer.__version__}")
    log.info(f"chain:\t{ic.ST_ID(observer.config.chain_id).name}")
    log.info(f"registry:\t{observer.config.registry_url}")
    log.info(f"updates:\tevery {observer.config.update_interval} seconds")

    client = observer.chain()
    log.info(f"blocks:\t {client.getblockcount()}")


if __name__ == "__main__":
    main()
