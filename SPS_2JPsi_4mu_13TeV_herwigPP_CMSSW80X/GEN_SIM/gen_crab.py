from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SPS_2JPsi_4mu_13TeV_herwigPP_CMSSW7122_GEN_v3'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SPS_gg-2Jpsi-4mu_8TeV_herwigPP250_5311p5_GEN_v12.py'
config.JobType.inputFiles = ['MEgg2JpsiJpsi.so']

config.section_("Data")
#config.Data.inputDBS = 'phys03'
config.Data.outputPrimaryDataset = 'SPS_JPsi_RunII'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2500
NJOBS = 800
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/bmichlin/'
config.Data.publication = True
config.Data.outputDatasetTag = 'SPS_2JPsi_4mu_13TeV_herwigPP_CMSSW7122_GEN_v3'

config.section_("Site")
config.Site.storageSite = 'T3_US_Rice'
