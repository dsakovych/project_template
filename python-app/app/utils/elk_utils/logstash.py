from logging.handlers import SocketHandler
from logstash import formatter
from app.settings import project_config


class CustomLogstashFormatter(formatter.LogstashFormatterBase):

    def format(self, record):
        # Create message dict
        message = {
            '@timestamp': self.format_timestamp(record.created),
            '@version': '1',
            'message': record.getMessage(),
            'port': project_config.PORT,
            'host': project_config.HOST,
            'level': record.levelname,
        }

        # Add extra fields
        # message.update(self.get_extra_fields(record))

        # If exception, add debug info
        if record.exc_info:
            message.update(self.get_debug_fields(record))

        return self.serialize(message)


class TCPLogstashHandler(SocketHandler, object):
    """Python logging handler for Logstash. Sends events over TCP.
    :param host: The host of the logstash server.
    :param port: The port of the logstash server (default 5959).
    :param message_type: The type of the message (default logstash).
    :param fqdn; Indicates whether to show fully qualified domain name or not (default False).
    :param version: version of logstash event schema (default is 0).
    :param tags: list of tags for a logger (default is None).
    """

    def __init__(self, host, port=5959, message_type='logstash', tags=None, fqdn=False):
        super(TCPLogstashHandler, self).__init__(host, port)

        self.formatter = CustomLogstashFormatter(message_type, tags, fqdn)

    def makePickle(self, record):
        return self.formatter.format(record) + b'\n'
