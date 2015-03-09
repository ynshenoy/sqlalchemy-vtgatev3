from sqlalchemy.engine import default
from sqlalchemy.orm import Session
from sqlalchemy import event

class VTGatev3Dialect(default.DefaultDialect):
    def __init__(self, **kwargs):
        default.DefaultDialect.__init__(self, **kwargs)

    @classmethod
    def dbapi(cls):
        import vtdb as module
        return module

    def create_connect_args(self, url):
        #import pudb; pu.db
        opts = url.translate_connect_args()
        addr = "{}:{}".format(opts['host'],opts['port'])
        timeout = 10.0
         
        #print opts
        return [(addr,timeout), {}]

    def _check_unicode_returns(self, connection):
        pass
    def _check_unicode_description(self, connection):
        pass

    
    @event.listens_for(Session, 'after_begin')
    def receive_after_begin(session, transaction, connection):
        dbapi_connection = connection.connection.connection
        dbapi_connection.begin()
