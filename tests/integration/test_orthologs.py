import os
from nose.tools import eq_, ok_, with_setup

from hommod_rest.services.model import findOrthologsToSeq
from hommod_rest.services.blast import blaster
import hommod_rest.default_settings as config

import logging
_log = logging.getLogger(__name__)

mydir = os.path.dirname(__file__)


def _setup():
    blaster.uniprot_db = os.path.join(mydir, "data/mini")  # small version
    blaster.templates_db = config.TEMPLATESDB
    blaster.blastp_exe = config.BLASTP


def _tear_down():
    pass


@with_setup(_setup, _tear_down)
def test_1OCO_BOVIN():
    orthologs = findOrthologsToSeq(
        "MFINRWLFSTNHKDIGTLYLLFGAWAGMVGTALSLLIRAELGQPGTLLGDDQI"
        "YNVVVTAHAFVMIFFMVMPIMIGGFGNWLVPLMIGAPDMAFPRMNNMSFWLLP"
        "PSFLLLLASSMVEAGAGTGWTVYPPLAGNLAHAGASVDLTIFSLHLAGVSSIL"
        "GAINFITTIINMKPPAMSQYQTPLFVWSVMITAVLLLLSLPVLAAGITMLLTD"
        "RNLNTTFFDPAGGGDPILYQHLFWFFGHPEVYILILPGFGMISHIVTYYSGKK"
        "EPFGYMGMVWAMMSIGFLGFIVWAHHMFTVGMDVDTRAYFTSATMIIAIPTGV"
        "KVFSWLATLHGGNIKWSPAMMWALGFIFLFTVGGLTGIVLANSSLDIVLHDTY"
        "YVVAHFHYVLSMGAVFAIMGGFVHWFPLFSGYTLNDTWAKIHFAIMFVGVNMT"
        "FFPQHFLGLSGMPRRYSDYPDAYTMWNTISSMGSFISLTAVMLMVFIIWEAFA"
        "SKREVLTVDLTTTNLEWLNGCPPPYHTFEEPTYVNLK", 'HUMAN')

    eq_(type(orthologs), dict)
    ok_(len(orthologs) > 0)
