"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:32

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.cte.bindings.v4_0.cons_sit_cte_tipos_basico_v4_00 import TconsSitCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class ConsSitCte(TconsSitCte):
    """
    Schema de validação XML dp Pedido de Consulta da Situação Atual do CT-e.
    """
    class Meta:
        name = "consSitCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
