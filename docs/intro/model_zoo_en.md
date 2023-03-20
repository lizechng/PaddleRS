# Model Zoo

PaddleRS' base model library comes from the Paddle-CV suite: [PaddleClas](https://github.com/PaddlePaddle/PaddleClas/blob/release/2.3/docs/zh_CN/algorithm_introduction/ImageNet_models.md)、[PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg/blob/release/2.4/docs/model_zoo_overview_cn.md)、[PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.3/README_cn.md#模型库)以及[PaddleGAN](https://github.com/PaddlePaddle/PaddleGAN/blob/develop/README_cn.md#模型库). In addition, PaddleRS also contains a series of remote sensing feature models, which can be used for remote sensing image segmentation and change detection.

## List of PaddleRS supported models

All PaddleRS currently supported models are as follows (those marked \* are dedicated models for remote sensing) :

| Task | Model | Multiband Support |
|--------|---------|------|
| Change Detection | \*BIT | Yes |
| Change Detection | \*CDNet | Yes |
| Change Detection | \*ChangeFormer | Yes |
| Change Detection | \*ChangeStar | No |
| Change Detection | \*DSAMNet | Yes |
| Change Detection | \*DSIFN | No |
| Change Detection | \*FC-EF | Yes |
| Change Detection | \*FC-Siam-conc | Yes |
| Change Detection | \*FC-Siam-diff | Yes |
| Change Detection | \*FCCDN | Yes |
| Change Detection | \*P2V-CD | Yes |
| Change Detection | \*SNUNet | Yes |
| Change Detection | \*STANet | Yes |
| Scene Classification | CondenseNet V2 | Yes |
| Scene Classification | HRNet | No |
| Scene Classification | MobileNetV3 | No |
| Scene Classification | ResNet50-vd | No |
| Image Restoration | DRN | No |
| Image Restoration | ESRGAN | Yes |
| Image Restoration | LESRCNN | No |
| Object Detection | Faster R-CNN | No |
| Object Detection | PP-YOLO | No |
| Object Detection | PP-YOLO Tiny | No |
| Object Detection | PP-YOLOv2 | No |
| Object Detection | YOLOv3 | No |
| Image Segmentation | BiSeNet V2 | Yes |
| Image Segmentation | DeepLab V3+ | Yes |
| Image Segmentation | \*FactSeg | Yes |
| Image Segmentation | \*FarSeg | Yes |
| Image Segmentation | Fast-SCNN | Yes |
| Image Segmentation | HRNet | Yes |
| Image Segmentation | UNet | Yes |