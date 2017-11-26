# coding: utf-8
import os, sys
import time, re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from logging import getLogger, StreamHandler, INFO, DEBUG

from commons.functions import *

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

def main(driver, args, config):
  """
  サンプル機能
  @param driver seleniumのドライバー
  @param args コマンドライン引数
  @param config 読み込まれたconfigファイル
  """
  logger.debug("## %s()", sys._getframe().f_code.co_name)
  logger.debug(args)
  logger.debug(config)
  
  if args.program_name == "test_sample":
    exec_test_sample(driver, args, config)

  sys.exit()
  return None

def exec_test_sample(driver, args, config):
  """
  test_sampleのメインロジック
  @param driver seleniumのドライバー
  @param args コマンドライン引数
  @param config 読み込まれたconfigファイル
  """

  ## 読み込んだconfig["file_sample"]数分ループ
  for (i, line) in read_file(config["file_sample"]):
    logger.debug("line[%s] is %s", i, line)

    # URL取得
    driver.get(config["url"])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'q')))

    # 入力
    driver.find_element_by_id('q').send_keys(line)

    # クリック
    #driver.find_element_by_class_name('btnK').click()
    driver.find_element_by_id('btnK').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lst-ib')))

    # 表示されている場合
    if driver.find_element_by_id('lst-ib').is_displayed():
      # クリック
      driver.find_element_by_class_name('success').click()
    else:
      pass

    # キャプチャを取得
    capture_path = os.path.abspath(os.path.dirname(__file__)) + '/../' + config["screenshot_path"] + get_screenshot_filename(config, i)
    logger.info(capture_path)

    # キャプチャ保存
    driver.save_screenshot(capture_path)



