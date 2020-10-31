# 打包指令

標準：
```
python setup.py sdist
```

wheel：
```
python setup.py sdist bdist_wheel
```

easy_install：
```
python setup.py bdist_egg
```

all
```
python setup.py sdist;python setup.py sdist bdist_wheel;python setup.py bdist_egg
```
# 上傳指令

要加入環境變數中
```
C:\Users\{user}\AppData\Roaming\Python\{Python38}\Scripts
```

```
twine upload dist/*
```

如果要上傳到 test-pypi
```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

# setup readme注意
```
long_description_content_type='text/markdown',
```
