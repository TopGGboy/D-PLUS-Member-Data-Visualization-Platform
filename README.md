# JD PLUS Member Data Visualization Platform

简体中文 | [English](./README_EN.md)

> 基于 Django + ECharts 的京东 PLUS 会员数据分析可视化平台

## 📖 项目简介

这是一个专为京东 PLUS 会员数据分析而设计的可视化平台，通过直观的数据图表展示会员画像、会员增长趋势及行为特征，帮助运营团队洞察会员价值。

## ✨ 功能特性

- **会员画像分析**：学历分布、性别比例、城市分布
- **会员趋势分析**：累计在籍会员数增长趋势
- **会员结构分析**：新会员 vs 老会员比例
- **会员行为分析**：开通次数分布、每日状态变化（拉新/续费/召回）

## 🛠 技术栈

| 类别 | 技术 |
|------|------|
| 后端框架 | Django 5.x |
| 数据库 | MySQL 8.0 |
| 前端框架 | HTML5 + CSS3 + JavaScript (ES6+) |
| 图表库 | ECharts 5.x |
| 工具库 | jQuery 3.x |

## 📁 项目结构

```
jd-plus-visualization/
├── 电商可视化/              # Django 项目配置
│   ├── settings.py         # 配置文件
│   ├── urls.py             # 主路由
│   └── wsgi.py             # WSGI 入口
├── PLUSUser/               # 应用模块
│   └── views.py            # 视图函数
├── templates/             # HTML 模板
│   └── plushome.html       # 主页面
├── static/                 # 静态资源
│   ├── css/                # 样式文件
│   ├── js/                 # JavaScript 文件
│   └── images/             # 图片资源
├── manage.py               # Django 管理脚本
└── 相关资料数据/            # 数据文件
```

## 🚀 快速开始

### 环境要求

- Python 3.10+
- MySQL 8.0

### 安装步骤

1. **克隆项目**

```bash
git clone https://github.com/yourusername/jd-plus-visualization.git
cd jd-plus-visualization
```

2. **创建数据库**

```sql
CREATE DATABASE jdplus CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. **安装依赖**

```bash
pip install django pymysql
```

4. **配置数据库**

编辑 `电商可视化/settings.py`：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jdplus',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'your_password'
    }
}
```

5. **初始化数据库**

```bash
# 导入数据库结构（请根据实际情况修改）
mysql -u root -p jdplus < 相关资料数据/数据库代码.sql

# 执行迁移
python manage.py migrate
```

6. **启动服务**

```bash
python manage.py runserver
```

访问地址：http://127.0.0.1:8000/plushome/

## 📊 页面预览

页面采用三栏布局：

```
┌─────────────┬──────────────────┬─────────────┐
│  会员画像   │   会员状态总览    │  会员变化   │
│             │                  │             │
│ · 学历分布  │   · 会员总人数    │ · 累计趋势  │
│ · 性别分布  │   · 每日状态变化  │ · 新老比例  │
│ · 城市分布  │                  │ · 开通次数  │
└─────────────┴──────────────────┴─────────────┘
```

## 📡 API 接口

| 接口路径 | 说明 |
|----------|------|
| `useredu/` | 用户学历分布 |
| `usercity/` | 用户城市分布 |
| `usersex/` | 用户性别分布 |
| `plusacc/` | 累计在籍会员数趋势 |
| `plusold_new_plus/` | 新老会员比例 |
| `plususer_times/` | 开通次数分布 |
| `plus_uds/` | 每日会员状态变化 |

## 📝 相关资料

- `相关资料数据/m1.csv` - 会员基础信息数据
- `相关资料数据/m2.csv` - 会员扩展数据
- `相关资料数据/m3.csv` - 会员状态变化数据
- `相关资料数据/数据库代码.sql` - 数据库表结构

## 🔧 优化建议

项目提供以下优化方向，供参考：

1. **使用 Django ORM** 替代直接 SQL 查询，提升代码可维护性
2. **添加数据缓存**（Redis/Django Cache）减少数据库压力
3. **启用 CSRF 防护** 提升安全性
4. **使用参数化查询** 防止 SQL 注入
5. **引入 API 框架**（如 Django REST Framework）实现前后端分离

## 📄 许可证

本项目仅供学习交流使用。

## 🙏 致谢

- [Django](https://www.djangoproject.com/) - 后端框架
- [ECharts](https://echarts.apache.org/) - 数据可视化图表库
- [jQuery](https://jquery.com/) - JavaScript 工具库
