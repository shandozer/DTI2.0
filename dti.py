#!/usr/local/bin/python
"""
__author__ = 'Shannon Buckley', 12/2/14
"""

#import CINDBOILERPLATE
import os
import sys
import shutil
from os import path

VERSION = '1.0.0'

PROCESS_NAME = 'DTI Processing'


# helpers
def get_project_path(project_name):
    pass


def get_project_config(project_name):
    pass


class DtiProcessing():
    """Base class for all dti processing steps"""
    pass


class StageDWI():
    """Use dcm2nii to assemble 4D DWI volume (nii)"""
    pass


class MaskB0():
    """Use fsl to queue up new masks for editing via BET"""
    pass


class CoregisterToStructural():
    """Concatenate reg of dwi to t2 and t2 to t1: get dwi to t1"""
    pass


class EddyCurrentCorrection():
    """Run Eddy Correction... Project config? Needs: 4D DWI and b0 mask"""
    pass


class EPIGeometricDistortionCorrection():
    """Run EPI correction... Project config? Needs EddyCorr, DWI to T2 coreg, params"""
    pass


class EstimateTensors():
    """Apply b0 mask to DWI and run tensor estimations. Project Config: Teem or FSL?"""
    pass


class QualityAssurance():
    """Use fsl to bring up 1) T2 w/ EPIcorr (b0) olay; 2) T1 w/ FA olay"""
    pass


def main():
    pass
# main
