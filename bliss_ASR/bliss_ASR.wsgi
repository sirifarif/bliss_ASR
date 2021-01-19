import sys
import bliss_ASR.bliss_ASR
import clam.clamservice
application = clam.clamservice.run_wsgi(bliss_ASR.bliss_ASR)
