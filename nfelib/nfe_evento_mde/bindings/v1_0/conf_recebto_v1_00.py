"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:25

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe_evento_mde.bindings.v1_0.leiaute_conf_recebto_v1_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Evento(Tevento):
    """
    Schema XML de validação do evento Confirmação de recebimento.
    """
    class Meta:
        name = "evento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
