# MINE SEED AUTO

SEED Telegram Mini App Bot Auto

Bot Link: <https://t.me/seed_coin_bot/app?startapp=441146600>

[![Static Badge](https://img.shields.io/badge/Dzuhri_AUTO_Links-yes?style=for-the-badge&color=black)](https://t.me/hidden_coding)
[![Static Badge](https://img.shields.io/badge/Channel-yes?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/dzuhri_auto)
[![Static Badge](https://img.shields.io/badge/discussion-yes?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/dzuhri_auto_discussion)
[![Static Badge](https://img.shields.io/badge/BOT_Store-yes?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/dz_auto_store)

## Features

- Support Telethon sessions
- Auto Claim First Egg (for fresh account)
- Auto Daily
- Auto Claim Ticket Streak
- Auto Hunting
- Auto Claim Hunting
- Auto Catch Worm
- Auto Upgrade Boost
- Auto Buy Worm
- Auto Claim Guild Seed
- Auto Clear Tasks 🔥🔥🔥 *(not all missions)*
- Auto Clear Academy Tasks
- Auto Spin Tickets
- Auto Fusion Egg Pieces
- Auto Hatch Egg
- Auto Sell Unneeded Worms

## Supported Operating Systems

- VPS
- Windows
- Mac
- Android (using Termux)

## Prerequisites

Before setting up the bot, ensure the following are installed:

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/) (version 3.10.0 - 3.11.9)

## .env Settings

All the configurations can be set in the .env file.

| Name                    | Description                                  | Default     |
| ----------------------- | -------------------------------------------- | ----------- |
| LICENSE_KEY             | Dzuhri Auto License Key                      |             |
| API_ID / API_HASH       | API and API HASH from telegram account       |             |
| REF_LINK                | Put your refferal link here                  | my ref link |
| AUTO_UPGRADE            | Enable auto upgrade boosts                   | True        |
| AUTO_BUY_WORM           | Enable auto upgrade worm from market         | False       |
| AUTO_SPIN               | Enable auto upgrade worm from market         | True        |
| AUTO_FUSION             | Enable auto upgrade worm from market         | False       |
| AUTO_HATCH              | Enable auto upgrade worm from market         | False       |
| MIN_CLAIM_GUILD_AMOUNT  | Minimum guild seed that can be claimed       | 7           |
| AUTO_SELL_WORM          | Enable auto sell worm to market              | False       |
| USE_RANDOM_DELAY_IN_RUN | Delay each account in seconds                | True        |
| RANDOM_DELAY_IN_RUN     | Delay after all account completed in seconds | [5, 15]     |
| USE_PROXY_FROM_FILE     | For using proxy                              | False       |

## How to Obtain API ID and API HASH

1. Go to [my.telegram.org](https://my.telegram.org/) and log in using your phone number.
2. Select `API development tools` and fill out the form to register a new application.
3. Record the `API_ID` and `API_HASH` provided after registering your application in the `.env` file.

<!-- ## How to obtain and use Query ID

To get the Query ID, [read this guide.](https://irhamdz.notion.site/Tutorial-Get-Query-ID-f415621d4a9843d2a7a9ad2cfb9abeb4?pvs=74)

Once you have the Query ID, add it to the `query_ids.txt` file.</br>
If you're using multiple accounts, simply add each query ID on a new line, like this:

```bash
query_id=xxxxxxxxx-User1
query_id=xxxxxxxxx-User2
``` -->

## How to use existing telethon session

To use existing / logged in sessions, [read this guide.](https://irhamdz.notion.site/Use-existing-telethon-sessions-11f53e55353080bc968ee5ee446e7d2b?pvs=74)

## How to Use Proxy

To use proxy, [read this guide.](https://irhamdz.notion.site/Use-Proxy-11153e553530807aaa14fdfde425723c?pvs=74)

To buy cheap proxy, [buy cheap proxy here](https://proxy-seller.com/?partner=QJGZSHEU86WI9Y)

## Installation Guide

### Step 1: Clone the Repository to Your PC / VPS

Run the following command to clone the repository:

```shell
git clone https://github.com/dzuhri-auto/seed-coin.git
```

### Step 2: Navigate to the Project Folder

Once cloned, navigate to the project directory:

```shell
cd seed-coin
```

### Step 3: Install the Dependencies

Run the following commands based on your operating system:

**Windows (Using Powershell)** :

```powershell
py -m venv venv
.\venv\Scripts\Activate
pip3 install wheel
pip3 install -r requirements.txt
cp .env-example .env
```

**Mac / Linux** :

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
cp .env-example .env
```

***Note : dont forget to edit `.env` file***

## Using the License Key

After installation, you need to input your license key in the `.env` file.

If you don't have a license key yet, you can purchase one here: [Buy the license key](https://irhamdz.notion.site/Dzuhri-Auto-10f53e55353080f98fbae250bd7172d1)

Once you have it, add it to your `.env` file like this:

```note
LICENSE_KEY="Your License Key"
```

## Starting the Bot

Run the bot using the following commands, depending on your operating system:

**Windows (Using Powershell)** :

```powershell
.\venv\Scripts\Activate
py main.py
```

**Mac / Linux** :

```shell
source venv/bin/activate
python3 main.py
```
