from gevent.monkey import patch_all
patch_all()

import gevent
import logging

from azrpc import AZRPCServer

from . import rpc, LISTEN_PORT

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)
    AZRPCServer(rpc)
    logger.info('Listening on port %s', LISTEN_PORT)
    try:
        gevent.wait()
    except KeyboardInterrupt:
        pass

main()
