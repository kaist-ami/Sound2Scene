import torch
from torch import nn
import torch.nn.functional as F
from models import resnet

class AVENet(nn.Module):

    def __init__(self,args):
        super(AVENet, self).__init__()
        self.audnet = Resnet(args)

    def forward(self, audio):
        x, aud, inter = self.audnet(audio)

        # return aud, x, inter
        return aud, x


class AVENet_(nn.Module):
    def __init__(self,args):
        super(AVENet_, self).__init__()
        self.audnet = Resnet(args)

    def forward(self, audio):
        x, aud, inter = self.audnet(audio)

        # return aud, x, inter
        return aud, x

def Resnet(opt):

    assert opt.model_depth in [10, 18, 34, 50, 101, 152, 200]

    if opt.model_depth == 10:
        model = resnet.resnet10(
            num_classes=opt.n_classes)
    elif opt.model_depth == 18:
        if opt.resnet_type=="fc2":
            model = resnet.resnet18_(
                num_classes=opt.n_classes,
                pool=opt.pool)
        else:
            model = resnet.resnet18(
                num_classes=opt.n_classes,
                pool=opt.pool)
    elif opt.model_depth == 34:
        model = resnet.resnet34(
            num_classes=opt.n_classes,
            pool=opt.pool)
    elif opt.model_depth == 50:
        model = resnet.resnet50(
            num_classes=opt.n_classes,
            pool=opt.pool)
    elif opt.model_depth == 101:
        model = resnet.resnet101(
            num_classes=opt.n_classes)
    elif opt.model_depth == 152:
        model = resnet.resnet152(
            num_classes=opt.n_classes)
    elif opt.model_depth == 200:
        model = resnet.resnet200(
            num_classes=opt.n_classes)
    return model

if __name__=='__main__':
    model = AVENet()