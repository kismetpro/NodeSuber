# NodeSuber

**选择您的语言 / Select Your Language / Выберите ваш язык / زبان خود را انتخاب کنید**

[**English**](#english) | [**简体中文**](#简体中文) | [**Русский**](#русский) | [**فارسی**](#فارسی)

</div>

---

<a name="english"></a>

## English

### **NodeSuber: Your Free, Real-time Proxy Node Subscription Center**

**NodeSuber** is a powerful open-source project dedicated to providing users with **free**, **real-time updated** solutions for circumventing internet censorship. This project aims to help users easily bypass **firewalls** and achieve stable, efficient network access. We collect and integrate a **large number** of proxy **nodes**, offering them through a convenient **subscription** method. Say goodbye to the tedious process of searching for and configuring **nodes**. NodeSuber is your ideal tool for getting over the wall.

#### **Core Features:**

1.  **Comprehensive Protocol Support**
    NodeSuber is fully compatible with mainstream and emerging proxy protocols, including **Vless**, **Vmess**, **Tuic**, **Trojan**, **ShadowsocksR (SSR)**, and the high-performance **Hysteria2**. No matter which client you use, you can find a suitable **node** here.

2.  **Real-time Updates & High-Quality Nodes**
    Our system automatically detects and **updates the node pool** around the clock, ensuring that the connections you get through your **subscription** are always live and available. We focus on providing **high-quality nodes** to create a stable and fast online experience for you.

3.  **Flexible Subscription Links**
    *   **Universal Subscription Link**: A single **configuration subscription link** to import all types of **nodes** at once for maximum convenience.
    *   **Protocol-Specific Subscription Links**: For personalized needs, we also offer **subscription links** categorized by protocol. You can choose to **subscribe** only to Vless **nodes**, Trojan **nodes**, or any other specific type you prefer.

#### **Project Advantages:**

*   **Completely Free**: Enjoy **high-quality** proxy services at no cost.
*   **Massive Selection**: A **large number** of **nodes** covering multiple protocols, so there's always one that fits your needs.
*   **Real-time & Efficient**: **Real-time updates** ensure the validity of your **subscription** content, making it a reliable tool for bypassing **firewalls**.
*   **One-Click Subscription**: A simple **configuration subscription link** eliminates the hassle of manual setup, making internet freedom simpler than ever.

Whether you're a beginner trying to access the free internet for the first time or a seasoned user looking for a stable backup, NodeSuber is your best choice for a stable, efficient, and free solution.

### **Subscription Links**

- **All Configurations Subscription Link (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/out/All_Configs_Sub.txt
  ```

- **Hysteria2 Protocol Subscription Link (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/hy2.txt
  ```

- **Shadowsocks Protocol Subscription Link (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ss.txt
  ```

- **ShadowsocksR Protocol Subscription Link (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ssr.txt
  ```

- **Trojan Protocol Subscription Link (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/trojan.txt
  ```

- **Tuic Protocol Subscription Link (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/tuic.txt
  ```

- **Vless Protocol Subscription Link (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vless.txt
  ```

- **Vmess Protocol Subscription Link (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vmess.txt
  ```

<br>

<details>
<summary><b>For Developers</b></summary>

### Project Overview
This is an asynchronous Python project for managing V2Ray configurations. It fetches subscription links from a list of URLs defined in `config.json` and then categorizes them by protocol.

### Tech Stack
- Python
- `asyncio`
- `aiohttp`
- `requests`
- `pybase64`

### Installation
To install the dependencies, run the following command:
```bash
pip install -r Files/requirements.txt
```

### Usage
To run the project, use the following command:
```bash
python main.py
```
All configurations are handled in `config.json`.

### Architecture
The project is a data processing pipeline driven by `config.json`:
1. `app_logic.py`: Fetches and decodes subscription links.
2. `sort_logic.py`: Sorts the decoded configurations.
3. `utils.py`: Provides helper functions.

### Code Style
- PEP 8
- Bilingual (English/Chinese) logging and comments

### Testing
- This project currently has no test setup.

</details>

---

<a name="简体中文"></a>

## 简体中文

### **NodeSuber：您的免费实时科学上网节点订阅中心**

**NodeSuber** 是一个强大的开源项目，致力于为广大用户提供**免费**、**实时更新**的**科学上网**解决方案。本项目旨在帮助用户轻松突破**防火墙**的限制，实现稳定、高效的网络访问。我们搜集并整合了**大量**的代理**节点**，通过便捷的**订阅**方式，让您告别繁琐的**节点**查找和配置过程，是您理想的**翻墙**与**梯子**工具。

#### **核心特性：**

1.  **全面的协议支持**
    NodeSuber 全面兼容市面上主流及新兴的代理协议，包括 **Vless**、**Vmess**、**Tuic**、**Trojan**、**ShadowsocksR (SSR)** 以及高性能的 **Hysteria2**。无论您使用何种客户端，都能在这里找到适合您的**节点**。

2.  **实时更新与高质量节点**
    我们的系统全天候自动检测和**更新节点**池，确保您通过**订阅**获取的都是**实时**可用的连接。我们专注于提供**高质量**的**节点**，为您打造稳定、快速的**科学上网**体验。

3.  **灵活的订阅链接**
    *   **通用配置订阅链接**：提供一个统一的**配置订阅链接**，一键导入即可获取所有类型的**节点**，方便快捷。
    *   **专属协议订阅链接**：为满足个性化需求，我们也提供了按协议分类的**协议订阅链接**。您可以根据自己的偏好，只**订阅** Vless **节点**或 Trojan **节点**等特定类型。

#### **项目优势总结：**

*   **完全免费**：无需任何费用，即可享受**高质量**的**科学上网**服务。
*   **海量选择**：提供**大量**覆盖多种协议的**节点**，总有一款适合您。
*   **实时高效**：**实时更新**，确保**订阅**内容的有效性，是您穿越**防火墙**的可靠工具。
*   **一键订阅**：简单的**配置订阅链接**，免去手动配置的烦恼，让**翻墙**变得前所未有的简单。

无论您是初次尝试**科学上网**的新手，还是寻求稳定备用**梯子**的老手，NodeSuber 都将是您稳定、高效、免费的最佳选择。

### **订阅链接**

- **所有配置订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/out/All_Configs_Sub.txt
  ```

- **Hysteria2 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/hy2.txt
  ```

- **Shadowsocks 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ss.txt
  ```

- **ShadowsocksR 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ssr.txt
  ```

- **Trojan 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/trojan.txt
  ```

- **Tuic 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/tuic.txt
  ```

- **Vless 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vless.txt
  ```

- **Vmess 协议订阅链接 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vmess.txt
  ```

<br>

<details>
<summary><b>开发者信息</b></summary>

### 项目概况
这是一个异步的 Python 项目，用于管理 V2Ray 配置。它从 `config.json` 中定义的 URL 列表中获取订阅链接，然后将它们按协议分类。

### 技术栈
- Python
- `asyncio`
- `aiohttp`
- `requests`
- `pybase64`

### 安装
要安装依赖，请运行以下命令：
```bash
pip install -r Files/requirements.txt
```

### 命令
要运行该项目，请使用以下命令：
```bash
python main.py
```
所有配置都在 `config.json` 中处理。

### 架构
该项目是一个由 `config.json` 驱动的数据处理流水线：
1. `app_logic.py`：获取并解码订阅链接。
2. `sort_logic.py`：对解码后的配置进行分类。
3. `utils.py`：提供辅助函数。

### 代码风格
- PEP 8
- 双语（英语/中文）日志和注释

### 测试
- 该项目目前没有测试设置。

</details>

---

<a name="русский"></a>

## Русский

### **NodeSuber: Ваш бесплатный центр подписок на прокси-узлы с обновлениями в реальном времени**

**NodeSuber** — это мощный проект с открытым исходным кодом, предназначенный для предоставления пользователям **бесплатных** и **обновляемых в реальном времени** решений для обхода интернет-цензуры. Цель проекта — помочь пользователям легко преодолевать **файрволы** и получать стабильный и эффективный доступ к сети. Мы собираем и интегрируем **большое количество** прокси-**узлов**, предлагая их через удобный механизм **подписки**. Попрощайтесь с утомительным процессом поиска и настройки **узлов**. NodeSuber — ваш идеальный инструмент для преодоления блокировок.

#### **Ключевые особенности:**

1.  **Поддержка всех основных протоколов**
    NodeSuber полностью совместим с популярными и новыми протоколами, включая **Vless**, **Vmess**, **Tuic**, **Trojan**, **ShadowsocksR (SSR)** и высокопроизводительный **Hysteria2**. Независимо от того, какой клиент вы используете, вы найдете здесь подходящий **узел**.

2.  **Обновления в реальном времени и высококачественные узлы**
    Наша система круглосуточно автоматически обнаруживает и **обновляет пул узлов**, гарантируя, что все соединения, полученные по **подписке**, всегда активны и доступны. Мы сосредоточены на предоставлении **высококачественных узлов** для стабильного и быстрого доступа в интернет.

3.  **Гибкие ссылки на подписки**
    *   **Универсальная ссылка на подписку**: Единая **ссылка на подписку** для импорта всех типов **узлов** одним кликом для максимального удобства.
    *   **Ссылки на подписки для конкретных протоколов**: Для индивидуальных потребностей мы также предлагаем **ссылки на подписки**, сгруппированные по протоколам. Вы можете **подписаться** только на **узлы** Vless, Trojan или любые другие на ваш выбор.

#### **Преимущества проекта:**

*   **Полностью бесплатно**: Наслаждайтесь **высококачественными** прокси-сервисами без какой-либо платы.
*   **Огромный выбор**: **Большое количество узлов**, охватывающих множество протоколов, так что всегда найдется подходящий вариант.
*   **Актуальность и эффективность**: **Обновления в реальном времени** обеспечивают работоспособность вашей **подписки**, делая NodeSuber надежным инструментом для обхода **файрволов**.
*   **Подписка в один клик**: Простая **ссылка на подписку** избавляет от необходимости ручной настройки, делая доступ к свободному интернету проще, чем когда-либо.

Независимо от того, новичок ли вы, впервые пытающийся обойти блокировки, или опытный пользователь, ищущий стабильный запасной вариант, NodeSuber — ваш лучший выбор для стабильного, эффективного и бесплатного решения.

### **Ссылки на подписки**

- **Ссылка на подписку со всеми конфигурациями (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/out/All_Configs_Sub.txt
  ```

- **Ссылка на подписку по протоколу Hysteria2 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/hy2.txt
  ```

- **Ссылка на подписку по протоколу Shadowsocks (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ss.txt
  ```

- **Ссылка на подписку по протоколу ShadowsocksR (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ssr.txt
  ```

- **Ссылка на подписку по протоколу Trojan (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/trojan.txt
  ```

- **Ссылка на подписку по протоколу Tuic (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/tuic.txt
  ```

- **Ссылка на подписку по протоколу Vless (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vless.txt
  ```

- **Ссылка на подписку по протоколу Vmess (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vmess.txt
  ```

<br>

<details>
<summary><b>Для разработчиков</b></summary>

### Обзор проекта
Это асинхронный проект на Python для управления конфигурациями V2Ray. Он получает ссылки на подписки из списка URL-адресов, определённого в `config.json`, а затем классифицирует их по протоколам.

### Технологический стек
- Python
- `asyncio`
- `aiohttp`
- `requests`
- `pybase64`

### Установка
Для установки зависимостей выполните следующую команду:
```bash
pip install -r Files/requirements.txt
```

### Использование
Для запуска проекта используйте следующую команду:
```bash
python main.py
```
Все настройки производятся в файле `config.json`.

### Архитектура
Проект представляет собой конвейер обработки данных, управляемый `config.json`:
1. `app_logic.py`: Получает и декодирует ссылки на подписки.
2. `sort_logic.py`: Сортирует декодированные конфигурации.
3. `utils.py`: Предоставляет вспомогательные функции.

### Стиль кода
- PEP 8
- Двуязычные (английский/китайский) логи и комментарии

### Тестирование
- В настоящее время в проекте нет настроек для тестирования.

</details>

---

<a name="فارسی"></a>

<div dir="rtl">

## فارسی

### **NodeSuber: مرکز اشتراک رایگان و لحظه‌ای سرورهای شما**

**NodeSuber** یک پروژه‌ی قدرتمند و متن‌باز است که به ارائه‌ی راه‌حل‌های **رایگان** و **به‌روزرسانی لحظه‌ای** برای عبور از فیلترینگ اینترنت اختصاص دارد. هدف این پروژه کمک به کاربران برای عبور آسان از **فایروال‌ها** و دستیابی به اینترنت پایدار و پرسرعت است. ما تعداد **بسیار زیادی** از **سرورهای** پروکسی را جمع‌آوری و یکپارچه کرده و از طریق روش **اشتراک (Subscription)** آسان در اختیار شما قرار می‌دهیم. با فرآیند خسته‌کننده جستجو و پیکربندی دستی **سرورها** خداحافظی کنید. NodeSuber ابزار ایده‌آل شما برای عبور از محدودیت‌هاست.

#### **ویژگی‌های کلیدی:**

۱. **پشتیبانی جامع از پروتکل‌ها**
NodeSuber به طور کامل با پروتکل‌های رایج و جدید پروکسی از جمله **Vless**، **Vmess**، **Tuic**، **Trojan**، **ShadowsocksR (SSR)** و پروتکل پرسرعت **Hysteria2** سازگار است. مهم نیست از چه کلاینتی استفاده می‌کنید، همیشه می‌توانید **سرور** مناسب خود را اینجا پیدا کنید.

۲. **به‌روزرسانی لحظه‌ای و سرورهای باکیفیت**
سیستم ما به صورت شبانه‌روزی و خودکار مجموعه **سرورها را بررسی و به‌روزرسانی می‌کند** تا اطمینان حاصل شود اتصالاتی که از طریق **اشتراک** دریافت می‌کنید، همیشه فعال و در دسترس هستند. ما بر ارائه‌ی **سرورهای باکیفیت** تمرکز داریم تا تجربه‌ای پایدار و سریع برای شما فراهم کنیم.

۳. **لینک‌های اشتراک انعطاف‌پذیر**
* **لینک اشتراک عمومی**: یک **لینک اشتراک واحد** که با افزودن آن به کلاینت خود، تمام انواع **سرورها** را به صورت یک‌جا و به راحتی دریافت می‌کنید.
* **لینک‌های اشتراک بر اساس پروتکل**: برای نیازهای شخصی‌سازی‌شده، ما **لینک‌های اشتراک** را بر اساس پروتکل نیز دسته‌بندی کرده‌ایم. شما می‌توانید انتخاب کنید که فقط **اشتراک سرورهای** Vless، Trojan یا هر نوع دیگری را که ترجیح می‌دهید، دریافت کنید.

#### **مزایای پروژه:**

*   **کاملاً رایگان**: از خدمات پروکسی **باکیفیت** بدون هیچ هزینه‌ای لذت ببرید.
*   **انتخاب گسترده**: ارائه‌ی **تعداد زیادی سرور** با پوشش پروتکل‌های متنوع که همیشه یکی از آن‌ها مناسب شما خواهد بود.
*   **لحظه‌ای و کارآمد**: **به‌روزرسانی‌های لحظه‌ای** اعتبار محتوای **اشتراک** شما را تضمین می‌کند و آن را به ابزاری قابل اعتماد برای عبور از **فایروال‌ها** تبدیل می‌کند.
*   **اشتراک با یک کلیک**: **لینک اشتراک** ساده، شما را از دردسرهای تنظیمات دستی بی‌نیاز می‌کند و دسترسی به اینترنت آزاد را آسان‌تر از همیشه می‌سازد.

چه کاربری مبتدی باشید که برای اولین بار به دنبال دسترسی به اینترنت آزاد هستید، و چه کاربری حرفه‌ای که به دنبال یک ابزار پشتیبان پایدار می‌گردد، NodeSuber بهترین انتخاب شما برای یک راه‌حل پایدار، کارآمد و رایگان خواهد بود.

### **لینک‌های اشتراک**

- **لینک اشتراک تمام کانفیگ‌ها (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/out/All_Configs_Sub.txt
  ```

- **لینک اشتراک پروتکل Hysteria2 (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/hy2.txt
  ```

- **لینک اشتراک پروتکل Shadowsocks (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ss.txt
  ```

- **لینک اشتراک پروتکل ShadowsocksR (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/ssr.txt
  ```

- **لینک اشتراک پروتکل Trojan (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/trojan.txt
  ```

- **لینک اشتراک پروتکل Tuic (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/tuic.txt
  ```

- **لینک اشتراک پروتکل Vless (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vless.txt
  ```

- **لینک اشتراک پروتکل Vmess (Base64):**
  ```
  https://github.com/kismetpro/NodeSuber/raw/refs/heads/main/Splitted-By-Protocol/vmess.txt
  ```

<br>

<details>
<summary><b>اطلاعات برای توسعه‌دهندگان</b></summary>

### نمای کلی پروژه
این یک پروژه پایتون غیرهمزمان (asynchronous) برای مدیریت کانفیگ‌های V2Ray است. این پروژه لینک‌های اشتراک را از لیستی از URLها که در `config.json` تعریف شده‌اند، دریافت کرده و سپس آن‌ها را بر اساس پروتکل دسته‌بندی می‌کند.

### پشته فناوری
- Python
- `asyncio`
- `aiohttp`
- `requests`
- `pybase64`

### نصب
برای نصب وابستگی‌ها، دستور زیر را اجرا کنید:
```bash
pip install -r Files/requirements.txt
```

### نحوه استفاده
برای اجرای پروژه، از دستور زیر استفاده کنید:
```bash
python main.py
```
تمام تنظیمات در فایل `config.json` انجام می‌شود.

### معماری
این پروژه یک خط لوله پردازش داده است که توسط `config.json` هدایت می‌شود:
۱. `app_logic.py`: لینک‌های اشتراک را دریافت و رمزگشایی (decode) می‌کند.
۲. `sort_logic.py`: کانفیگ‌های رمزگشایی‌شده را مرتب می‌کند.
۳. `utils.py`: توابع کمکی را ارائه می‌دهد.

### استایل کدنویسی
- PEP 8
- لاگ‌ها و کامنت‌های دوزبانه (انگلیسی/چینی)

### تست
- این پروژه در حال حاضر تنظیمات تست ندارد.

