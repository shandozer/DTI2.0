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
    """Base class for all dti processing steps. All file formats .nii.gz unless otherwise stated.
    1) Stage dicoms to make 4D DWI volume (all frames + b0)
    2) MaskB0. Runs BET and pauses for manual work & associated plog entry = Pass/Done.
    3) Coregistration to Structural. Requires: Step 2 plog = Pass/Don AND T2-BrainMask (T2-ICV).
        -Take DWI to T2 (via masked b0, via T2-ICV (config). Outputs .mat solving for T2->T1, B0->T2, concatenated B0->T1, and inverses.
        -Could also be made to take aparc+aseg from FS for starter-T2-mask (for passing FS QC cases).
    4) Eddy Correction: either FSL or Fletcher (config). Input masked b0 and 4D DWI.
    5) EPI Correction: assuming you want this (config) you can use FSL or Fletcher (config).
        In: EddyCorr DWI,
        Out: EPIcorrection DWI data (a warped, T2-like-space, essentially), the warp fields.
    6) Tensor Estimation: FSL or Teem (config). In: b0 masked, Eddy Corrected & EPI-corrected (or not. config) DWI.
    Out: many files.
    7) Do some QC... FSLview is great. 1) assess EPI-correctiton quality ; 2) asses overall DTI quality (usually FA
    sufficient)
    8) config: package up a list of deliverables specific to that project & its collaborators?"""
    pass


class StageDWI(DtiProcessing):
    """Use dcm2nii to assemble 4D DWI volume (nii). In: raw dicoms. Out: 4D_DWI.nii.gz, contains all frames + b0"""
    pass


class MaskB0(DtiProcessing):
    """Use fsl to queue up new masks (BET2) for editing. Input: b0 frame from 4D_DWI. Out: maskedB0."""
    pass


class CoregisterToStructural(DtiProcessing):
    """Concatenate reg of dwi to t2 and t2 to t1: get dwi to t1. In: DWI + mask, Structural + Mask(s). Out: .mat
    files for all registrations in both directions."""
    pass


class EddyCurrentCorrection(DtiProcessing):
    """Run Eddy Correction... Project config? In: 4D DWI and b0 mask. Out: EddyCorrected 4D DWI"""
    pass


class EPIGeometricDistortionCorrection(DtiProcessing):
    """Run EPI correction... Project config? In: EddyCorr DWI, DWI to T2 coreg, Fletcher params"""
    pass


class EstimateTensors(DtiProcessing):
    """Apply b0 mask to DWI and run tensor estimations. Project Config: Teem or FSL? In: 4D DWI, b0 Mask. Out: Many
    DTI related files."""
    pass


class QualityAssurance(DtiProcessing):
    """Use fsl to bring up 1) T2 w/ EPIcorr (b0) olay to verify EPI correction quality;
    2) T1 w/ FA olay to verify adequacy of MRI-space dti data (FA often the most critical)."""
    pass


def main():
    """do all the things"""
    pass


# REPOSITORY

class DTIProcessingRepository():
    """SQL repository to gather data for various steps."""

    def get_raw_dwi_dicoms(self):
        pass

    def get_t2_masked(self):
        pass

    def get_b0_masked(self):
        pass



