selenium_testcodes
====

## pyenv, anacondaのインストール(mac) 
```
### install pyenv anaconda
$ brew update
$ brew upgrade
$ brew install pyenv
$ pyenv --version
$ pyenv install anaconda3-5.0.0
$ pyenv versions
$ pyenv global anaconda3-5.0.0

### add bash
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ source ~/.bash_profile
$ which conda
```

## ダウンロード
```
$ git clone https://github.com/hirasaki1985/selenium_testcodes.git
$ cd selenium_testcodes
```

## 環境構築
```
$ conda create --name selenium python=3.6
$ source activate selenium
(selenium)$ python -V
(selenium)$ pip install -r requirements.txt
```

## 実行
```
$ source activate selenium
(selenium)$ python src/main.py
```

## main.py
|オプション|説明|
|-m|機能名|
|-p|プロジェクト(案件名)|
|-s|対象環境|


## 参考
[Macにanacondaをインストールする→ライブラリの追加](https://qiita.com/berry-clione/items/24fb5d97e4c458c0fc28)
[PythonでSeleniumを使ってスクレイピング (基礎)](https://qiita.com/kinpira/items/383b0fbee6bf229ea03d)
[ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/home)
[Pythonでディクショナリを扱う時に便利なライブラリ「Box」](http://co.bsnws.net/article/246)
[webdriver](http://www.seleniumhq.org/projects/webdriver/)

## Author

[m.hirasaki](https://github.com/hirasaki1985)
