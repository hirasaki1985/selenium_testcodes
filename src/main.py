# coding: utf-8
import os, sys
import argparse

from selenium import webdriver
from logging import getLogger, StreamHandler, INFO, DEBUG

import commons.functions as common
import modules.sample.sample as sample

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

def main(args):
  """
  最初に実行される関数.
  @param args コンソールで渡された引数をdict型にしたもの
  """

  # ドライバーのロード
  driver = getDriver(args)
  config = common.read_config(os.path.abspath(os.path.dirname(__file__)) + "/../" + args.config)

  # お問い合わせ画面の場合 
  if args.module_name == "sample":
    sample.main(driver, args, config[args.stage]);

  driver.quit()
  driver.close()

def getDriver(args, driver_path ="librarys/selenium_drivers/chromedriver"):
  """
  seleniumのdvierを返す.
  @param args コマンドライン引数
  @param driver_path ドライバーへのパス。標準はchrome
  @return dvierインスタンス
  """
  return webdriver.Chrome(os.path.abspath(os.path.dirname(__file__))  + '/' + driver_path)  

if __name__ == '__main__':
  # 引数のチェック、dictの作成
  parser = argparse.ArgumentParser()

  parser.add_argument("-module_name", "-m", help="please input module_name", required=True)
  parser.add_argument("-program_name", "-p", help="please input program_name", required=True)
  parser.add_argument("-config", "-c", help="example ... config/environments.json", default="config/environments.json")
  parser.add_argument("-stage", "-s", help="local, staging, production", default="local")

  args = parser.parse_args()

  # main実行
  main(args)

