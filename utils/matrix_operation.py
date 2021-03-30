#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : Wed Jan 13 17:21:47 2021
# @Author : JRP - Ruipeng Jia

import torch
import torch.nn.functional as F


def pad(data, pad_id, width=-1):
    if (width == -1):
        width = max(len(d) for d in data)
    rtn_data = [d + [pad_id] * (width - len(d)) for d in data]
    return rtn_data


if __name__ == '__main__':
    ## for pad()
    src = [[1, 2], [3, 4, 5]]
    src = torch.tensor(pad(src, 0)); print(src)  # tensor([[1, 2, 0], [3, 4, 5]])
    # src = torch.nn.utils.rnn.pad_sequence(src, batch_first=True); print(src)  # tensor([[1, 2, 0], [3, 4, 5]]); It's same when there is no width spicified.
