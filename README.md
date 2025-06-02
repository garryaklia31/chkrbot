
# Xfinity Gmail Checker Bot

This is a Heroku-deployable Telegram bot that:
- Accepts a `.txt` file of Gmail addresses
- Checks each one on Xfinity's login page using Selenium
- Returns which emails are registered or not

## Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/xfinity-checker-bot.git
cd xfinity-checker-bot
```

2. Create a bot with @BotFather and get your `BOT_TOKEN`.

3. Set up environment variable in Heroku:
```
BOT_TOKEN=your_token_here
```

4. Deploy to Heroku:
```bash
git init
heroku create
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver
git add .
git commit -m "initial"
git push heroku master
heroku config:set BOT_TOKEN=your_bot_token_here
```

5. Done! Use the bot on Telegram.
