class Logger(object):
    class __Logger():
        def __init__(self, file_name):
            self.file_name = file_name

        def _write(self, level, msg):
            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self._write("CRITICAL", msg)

        def error(self, msg):
            self._write("ERROR", msg)

        def warn(self, msg):
            self._write("WARNING", msg)

        def info(self, msg):
            self._write("INFO", msg)

        def debug(self, msg):
            self._write("DEBUG", msg)