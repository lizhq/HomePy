# devlop
devlop

## 安装依赖 https://packaging.python.org/en/latest/tutorials/packaging-projects/
    py -m pip install --upgrade pip setuptools wheel build twine

## 编译
    py -m build

## 发布测试
    // twine upload --repository testpypi dist/*
    // pip install --index-url https://test.pypi.org/simple/ --no-deps HomePy
    
    twine upload --repository pypi dist/*