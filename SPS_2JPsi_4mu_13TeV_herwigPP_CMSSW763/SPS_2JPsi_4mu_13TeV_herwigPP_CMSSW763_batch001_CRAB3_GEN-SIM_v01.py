[CRAB]
jobtype     = cmssw
scheduler   = pbs
use_server  = 0

#[CONDORG]
#globus_rsl = (queue=grid)(maxWalltime=1440)(maxCpuTime=1440)

[PBS]
queue     = hepxrt
resources = cput=12:00:00,walltime=12:00:00

[GRID]
rb                   = CERN
proxy_server         = fg-myproxy.fnal.gov
virtual_organization = cms
se_white_list        = T3_US_TAMU
ce_white_list        = T3_US_TAMU

[CMSSW]
pset        = SPS_gg-2Jpsi-4mu_8TeV_herwigPP250_5311p5_GEN_v12.py
output_file = SPS_gg-2Jpsi-4mu_8TeV_herwigPP250_5311p5_GEN_v12.root
datasetpath = None
events_per_job = 100
number_of_jobs = 10

[USER]
thresholdLevel          = 80
email                   = pakhotin.queue@gmail.com
copy_data               = 1
return_data             = 0
storage_element         = T3_US_TAMU
additional_input_files  = MEgg2JpsiJpsi.so
user_remote_dir         = SPS_gg-2Jpsi-4mu_8TeV_herwigPP250_5311p5_GEN_v12
ui_working_dir          = SPS_gg-2Jpsi-4mu_8TeV_herwigPP250_5311p5_GEN_v12
publish_data_name       = SPS_gg-2Jpsi-4mu_8TeV_herwigPP250_5311p5_GEN_v12
publish_data            = 1
dbs_url_for_publication = https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet
