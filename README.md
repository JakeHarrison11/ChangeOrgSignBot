# Change.Org Infinite Signing Bot

This project is able to send a theoretically infinite number of petition signs to the website https://change.org

# Dependencies 
 
selenium (You will also need a webdriver binary for your platform for this to work, you can get one from https://chromedriver.chromium.org/

```
pip install selenium
```

pyautogui

```
pip install pyautogui
```

faker

```
pip install faker
```

# How to run

Place the webdriver binary in the project directory, then simply navigate to the project directory and run the script

```
python bot.py
```

When the script is launched the colsole will prompt you for a change.org link, after the link is inputted a web browser window will open. After that script should do the rest of the work.

# How it works

When you input your petition link into the console, the script will then load 2 JSON files. One filled with first names, and one filled with surnames. As the script runs it will randomly choose one first name, one surname, and it will randomly generate an email address with the Faker package. After that is done it finds the 3 text boxes on the sign page and fills them with the information it just generated, it unchecks the "Display my name and comment on this petition" checkbox and submits the information. When it's done with that, it clears the browser cache to remove any saved login information and reloads the page. This process repeats 1000 times or until you exit the script.
