# gta_view_assets
GTAオンラインのキャッシュフロー可視化

# 概要

* GTAオンライン 自アカウントの現金と預金をCSVにタンキング
* タンキングしたデータをグラフ化

経営者気分が味わえます!

# 環境

* OS

```sh
> Get-WmiObject Win32_OperatingSystem


SystemDirectory : C:\WINDOWS\system32
Organization    :
BuildNumber     : 18363
RegisteredUser  : user
SerialNumber    : 00330-80000-00000-AA868
Version         : 10.0.18363

```

* Python

```sh
> python --version
Python 3.7.2
```

# 準備

### 仮想環境作成

```sh
> python -m venv <name>
> .\<name>\Scripts\activate
```


### パッケージインストール

* Y軸の単位が指数表示になってしまうため、matplotlibは3.1.1を使います

```sh
> python -m pip install -r .\requests.txt
```

### pip list

```sh
> python -m pip list
Package         Version
--------------- -------
cycler          0.10.0
kiwisolver      1.2.0
matplotlib      3.1.1
numpy           1.18.2
pip             18.1
pyparsing       2.4.7
python-dateutil 2.8.1
selenium        3.141.0
setuptools      40.6.2
six             1.14.0
urllib3         1.25.9
```

* configure.py

```
email = <Your email>
password = <YOur password>
chrome_path = <Your chrome userdata path>
my_path = <Your csv data save directory> # For Taskscheduler
```

Chromeユーザプロファイルのログイン情報を利用します。  
そのためseleniumで一度Rockstar Soclal Clubへのログインが必要です。

# タンキング

何のツールでもいいので数分おきにタンキングスクリプトを起動します。

```sh
> python .\getgtamoney.py
```

取得したデータは.\data\gtacashflow.csvにタンキングされます。
例ではスクリプトをタスクスケジューラーで起動しています。

* タンキングされたデータ

```sh
> cat .\data\gtacashflow.csv
2020/04/12 17:15,40000,1081924
2020/04/12 17:30,40000,1081924
2020/04/12 17:45,0,1121924
2020/04/12 18:00,0,1095781
2020/04/12 18:15,0,1060181
2020/04/12 18:30,0,1236818
2020/04/12 18:45,2000,1236818
2020/04/12 19:00,2000,1136818
2020/04/12 19:15,0,1122693
2020/04/12 19:30,0,1239993
2020/04/12 19:45,0,1248918
2020/04/12 20:00,0,1248918
2020/04/12 20:15,0,1248918
```

# グラフ化

```sh
> python .\view_assets.py
```

* 出力例

![GTA_Asstets_Figure_2](https://user-images.githubusercontent.com/9325405/79679982-9d33e680-8245-11ea-9f90-7f7aa008d021.png)


# Have a fun GTA Online! :smile:

