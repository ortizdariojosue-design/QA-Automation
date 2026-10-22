import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCoffeeCart:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://coffee-cart.app/")
        yield
        self.driver.quit()
      

    #test 1: verifica el título de la página principal
    def test_titulo_pagina(self):
        assert "Coffee cart" in self.driver.title

    #test 2: agrega un espresso al carrito y verificar el valor $10.00
    def test_agregar_espresso_al_carrito(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']")
        assert "$10.00" in self.driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").text

    #test 3: abrir el modal de checkout para realizar la compra
    def test_abrir_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
        self.driver.find_element(By.CLASS_NAME, "modal-content")
        assert self.driver.find_element(By.CLASS_NAME, "modal-content").is_displayed()