import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

try:
    #abrir pagina
    driver=webdriver.Chrome()
    driver.get("https://buggy.justtestit.org/")
    driver.maximize_window()
    time.sleep(5)

    #actualizar el driver de selenium en la cmd
    #pip install --upgrade selenium

    userName = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.NAME,"login")))
    password = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.NAME,"password")))
    time.sleep(4)

    usuario = driver.find_element(By.NAME,"login")
    password = driver.find_element(By.NAME,"password")

    btn_login=driver.find_element(By.CSS_SELECTOR,"body > my-app > header > nav > div > my-login > div > form > button")
    imgPopularMake=driver.find_element(By.XPATH,"/html/body/my-app/div/main/my-home/div/div[1]/div/a")


    #comienzo de acciones
    #Intento de inicio de sesion
    usuario.send_keys("DANIELITA")
    password.send_keys("R44mYS.Z@d2TW8")
    time.sleep(3)

    #hacer clic en login btn
    btn_login.click()
    time.sleep(3)

    #hacer clic en Popular Make
    imgPopularMake.click()
    time.sleep(5)

    # Modelo Reventon
    imgReventon=driver.find_element(By.XPATH,"/html/body/my-app/div/main/my-make/div/div[2]/div/div/table/tbody/tr[2]/td[1]/a/img")
    #para que el testing automatico se dirija a un elemento en especifico y sea visible
    driver.execute_script("arguments[0].scrollIntoView();", imgReventon)
    time.sleep(3)

    #entrar en el modelo
    imgReventon.click()
    time.sleep(5)

    #bajar para ver los comentarios
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    #subir para ver el boton de Home
    driver.execute_script("window.scrollTo(0,0);")
    time.sleep(3)

    #clic en Home
    aHome=driver.find_element(By.XPATH,"/html/body/my-app/header/nav/div/a")
    aHome.click()
    time.sleep(5)

    #Clic en Popular model
    imgPopularModel=driver.find_element(By.XPATH,"/html/body/my-app/div/main/my-home/div/div[2]/div/a")
    imgPopularModel.click()
    time.sleep(5)
    #tiempo extra para ver el modelo
    time.sleep(2)

    #Bajar a los comentarios
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    #subir para ver la barra de navegacion
    driver.execute_script("window.scrollTo(0,0);")
    time.sleep(3)

    # clic en Home
    aHome.click()
    time.sleep(5)

    # Clic en Overall Rating
    imgOverallRating=driver.find_element(By.XPATH,"/html/body/my-app/div/main/my-home/div/div[3]/div/a")
    imgOverallRating.click()
    time.sleep(5)

    #Modelo Aventador
    imgAventador=driver.find_element(By.XPATH,"/html/body/my-app/div/main/my-overall/div/div/table/tbody/tr[4]/td[1]/a/img")

    #Baja para ver el modelo
    driver.execute_script("arguments[0].scrollIntoView();", imgAventador)
    time.sleep(3)

    # clic en el modelo
    imgAventador.click()
    time.sleep(5)

    # Bajamos para navegar mas
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    #subimos para ver la barra de navegacion
    driver.execute_script("window.scrollTo(0,0);")
    time.sleep(3)

    #Clic en el Home
    aHome.click()
    time.sleep(5)

    #cerrar sesion
    aLogout=driver.find_element(By.XPATH,"/html/body/my-app/header/nav/div/my-login/div/ul/li[3]/a")

    #La aserción es el análisis de la respuesta esperada, 
    #lo que va en  “” debe estar del todo exactamente igual a como figura en la página para que no falle.

    expected_text = "Logout"
    actual_text = aLogout.text
    assert expected_text == actual_text, "falló el logout"

    #Hacer clic en logout
    aLogout.click()

    #terminar el script
    print("el test ha terminado correctamente")
    driver.quit()
    
except NoSuchElementException as e:
    print(f"No se encontró el elemento: {e}")
    
finally:
    print("Esta es la finalización del script de prueba automatizada")
    driver.quit()
    



