from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SPS_2JPsi_4mu_13TeV_herwigPP_CMSSW763_batch001_CRAB_DIGI_L1_DIGI2RAW_HLT_PU_v02'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SPS_2JPsi_4mu_13TeV_herwigPP_CMSSW763_batch001__cfi__DIGI_L1_DIGI2RAW_HLT_PU.py'

config.section_("Data")
config.Data.inputDataset = '/SPS_JPsi_RunII/jrorie-SPS_2JPsi_4mu_13TeV_herwigPP_CMSSW763_batch001_GEN-SIM_v01-b2cf97c3ed6b81767753b32379415cd4/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/jrorie/'
config.Data.publication = True
config.Data.outputDatasetTag = 'SPS_2JPsi_4mu_13TeV_herwigPP_CMSSW763_batch001_CRAB_DIGI_L1_DIGI2RAW_HLT_PU_v02'

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
