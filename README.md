# Python API Autotest

## 项目简介
这是一个基于 Python 的接口自动化测试示例项目，用于演示常见接口测试场景。

## 技术栈
- Python
- requests
- pytest

## 测试场景
- 登录接口测试
- 参数校验
- token鉴权验证
- 响应结果断言

## 目录规划
- tests/
- utils/
- requirements.txt

## 说明
该项目用于展示接口测试与自动化测试基础能力。

## 目录结构
- tests/：测试用例
- utils/：公共方法
- data/：测试数据
- config.py：接口地址配置

## 测试场景
- 登录成功
- 登录失败
- 用户信息查询
- 用户注册

## 运行方式
pip install -r requirements.txt
pytest
