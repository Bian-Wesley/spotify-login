from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.common.by import By
import requests
import random

playlists = ["fill with urls of playlists/albums"]

def humanType(string, element):
	for char in string:
		element.send_keys(char)
		randWait = random.randint(10, 500) / 1000
		sleep(randWait)

browser = webdriver.Edge(r"path to webdriver")
browser.maximize_window()
browser.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F")

email = browser.find_element(By.ID, "login-username")
humanType("your username", email)
sleep(2)

password = browser.find_element(By.ID, "login-password")
humanType("your password", password)
sleep(2)

loginButton = browser.find_element(By.ID, "login-button")
loginButton.click()

sleep(10)

browser.execute_script("window.open('about:blank', 'secondtab');")
browser.switch_to.window("secondtab")
choosePlaylist = playlists[random.randint(0, len(playlists) - 1)]
browser.get(choosePlaylist)
sleep(10)
	
close = browser.find_elements(By.XPATH, "//div[@id='onetrust-close-btn-container']")
if len(close) != 0:
	close[0].click()
	sleep(2)
sleep(5)
play = browser.find_elements(By.XPATH, "//button[@data-testid='play-button']")
play[1].click() #works!!!!!!!!
sleep(3)
