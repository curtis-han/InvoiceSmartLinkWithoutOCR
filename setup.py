from setuptools import setup, find_packages

setup(
    name="InvoiceSmartLink",
    version="1.0.0",
    description="A smart link for managing invoices",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "Pillow==8.2.0",  # For image processing
        "numpy==1.20.3",  # For numerical operations
        # 他の依存関係をここに追加
    ],
    entry_points={
        'console_scripts': [
            'invoicesmartlink=main:main',  # main.pyのmain関数をエントリーポイントとして指定
        ],
    },
)