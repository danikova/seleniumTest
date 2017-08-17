from selenium import webdriver


def main():

    driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
    driver.get("https://10fastfingers.com/typing-test/english")
    assert "Typing" in driver.title

    inputfield = driver.find_element_by_id('inputfield')
    words_container = driver.find_element_by_id('row1')
    words = words_container.find_elements_by_tag_name("span")

    for word in words:
        inputfield.send_keys(word.text + ' ')

    driver.close()


if __name__ == '__main__':
    main()