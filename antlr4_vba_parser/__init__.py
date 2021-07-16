"""Here we try to update the JAVA $CLASSPATH environment variable so that the bundled antlr4 JAR is picked up."""
import os
import sys

_sep = ';' if sys.platform == 'win32' else ':'

os.environ['CLASSPATH'] = \
    os.environ.get('CLASSPATH', '') + _sep + os.path.dirname(__file__)  # should include antlr-4.*-complete.jar
