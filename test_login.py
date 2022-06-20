# -*- coding: UTF-8 -*-
from uitrace.api import *
import pytest

init_driver(workspace=os.path.dirname(__file__))
def test_login_demo():
    cmd_adb("shell input keyevent HOME", id_mark=True, timeout=-1)
    start_app("com.tencent.wetestdemo")
    # 登录
    # 输入账号
    click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.EditText[@text="Username" and @resource-id="com.tencent.wetestdemo:id/username"]', by=DriverType.UI, timeout=20)
    input_text("udt")
    # 输入密码
    click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.EditText[@text="Password" and @resource-id="com.tencent.wetestdemo:id/password"]', by=DriverType.UI, timeout=20)
    input_text("udt")
    # login
    click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.Button[@text="SIGNIN" and @resource-id="com.tencent.wetestdemo:id/login"]', by=DriverType.CV, timeout=30)