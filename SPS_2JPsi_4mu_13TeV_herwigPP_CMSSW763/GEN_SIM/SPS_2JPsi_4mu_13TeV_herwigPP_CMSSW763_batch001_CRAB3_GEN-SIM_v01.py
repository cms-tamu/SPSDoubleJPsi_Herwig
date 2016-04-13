from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SPS_2JPsi_4mu_13TeV_herwigPP_CMSSW763_batch001_GEN-SIM_v01'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SPS_2JPsi_4mu_13TeV_herwigPP_CMSSW763_batch001__cfi__GEN-SIM_v01.py'
config.JobType.inputFiles = ['MEgg2JpsiJpsi.so']

config.section_("Data")
#config.Data.inputDBS = 'phys03'
config.Data.outputPrimaryDataset = 'SPS_JPsi_RunII'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/jrorie/'
config.Data.publication = True
config.Data.outputDatasetTag = 'SPS_2JPsi_4mu_13TeV_herwigPP_CMSSW763_batch001_GEN-SIM_v01'

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
