# InvoiceSmartLink_withoutOCR

## 项目简介
InvoiceSmartLink_withoutOCR 是一个用于处理发票的工具，不依赖于光学字符识别（OCR）技术。该项目旨在提供高效、准确的发票数据处理解决方案。

## 功能特性
- **发票数据解析**: 从发票文件中提取关键信息。


## 安装指南
pip install requiements.txt
python main.py

## 使用方法
1. 修改JsonManger:
    - 修改年份
    - 根据自己的 勘定科目 进行修改
    ```
2. 将发票文件上传到指定目录，应用将自动处理并生成结果文件。

## 如何打包
pyinstaller --onefile --icon=isl_no_ocr.ico --name=IvoiceSmartLinkWithoutOCR main.py

## 贡献指南
欢迎贡献代码！请遵循以下步骤:
1. Fork 本仓库。
2. 创建一个新的分支 (`git checkout -b feature-branch`)。
3. 提交您的更改 (`git commit -am 'Add new feature'`)。
4. 推送到分支 (`git push origin feature-branch`)。
5. 创建一个新的 Pull Request。

## 许可证
该项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

## 联系方式
如有任何问题或建议，请通过以下方式联系我们:
- 邮箱: curtis_han@outlook.com

感谢您的使用和支持！