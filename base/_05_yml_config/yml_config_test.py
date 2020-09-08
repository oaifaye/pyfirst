from base._05_yml_config.yml_config  import cfg_from_file
from base._05_yml_config.yml_config import cfg

cfg_from_file('text.yml')
print('cfg.GPU_ID:',cfg.GPU_ID)
print('cfg.TRAIN.DISPLAY:',cfg.TRAIN.DISPLAY)
print('cfg.TEST.HAS_RPN :',cfg.TEST.HAS_RPN )
