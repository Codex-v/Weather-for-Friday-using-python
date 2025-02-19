from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\\Users\\LUCIFER\\Desktop\\weather\\chromedriver.exe")

city = str(input("enter you city"))


driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
driver.get("google.com/weather/jamnagar")

print(driver.VED("b-forecast__table-description-content")[0].text)
