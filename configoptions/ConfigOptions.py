# -*- encoding: utf-8 -*-

import os
import yaml


class ConfigOptions:
    def __init__(self,
                 val={},
                 cfg=["/etc/config", "./config", "./config.yml"]):
        '''
        ConfigOptions
        '''
        opts = {}
        if len(cfg):
            for PTH in cfg:
                if os.path.isdir(PTH):
                    ymls = [x for x in os.listdir(PTH) if x.endswith(".yml")]
                    ymls += [x for x in os.listdir(PTH) if x.endswith(".yaml")]
                    for FTH in sorted(ymls):
                        with open("{0}/{1}".format(PTH, FTH)) as f:
                            ndict = yaml.load(f)
                        for k in ndict:
                            opts.update({k: ndict.get(k)})
                elif (os.path.isfile(PTH) and
                        (PTH.endswith(".yml") or PTH.endswith(".yaml"))):
                    with open("{0}".format(PTH)) as f:
                        ndict = yaml.load(f)
                    for k in ndict:
                        opts.update({k: ndict.get(k)})
            self.opts = opts