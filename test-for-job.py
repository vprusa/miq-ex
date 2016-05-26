from pyvirtualdisplay import Display
from selenium import webdriver
 
display = Display(visible=0, size=(800, 600))
display.start()
 
browser = webdriver.Firefox()
browser.get('https://vprusa-docker-2.bc.jonqe.lab.eng.bos.redhat.com')
print browser.title
browser.quit()
 
display.stop()
