import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

"""
Todo:
    check all boxes - done
    time.sleep() - done 
    static dropdown - done
    dynamic dropdown
    all_inner_text
    all_text_contents
    checked or not 
    click
    count
    dbclick
    drag to
    highlight 
    hover 
    inner text
    inner html
    is visible 
    is checked
    is editable
    is hidden 
    nth
    press
    screenshot
    tap
    type
    uncheck 
    wait for 
    scroll into view
    select text
    copy to clipboard
    find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

drag and drop 
element = driver.find_element(By.NAME, "source")
target = driver.find_element(By.NAME, "target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()

alert = driver.switch_to.alert

hisory 
driver.forward()
driver.back()
"""
#################
# Types
#################

T_INPUT = 'input'
T_BUTTON = 'button'
T_CHECKBOX = 'checkbox'
T_DROPDOWN = 'dropdown'
T_RETURN = "return"

#################
# LOCATORS
#################

L_CSS = 'css'
L_XPATH = 'xpath'

#################
# ACTIONS
#################

A_CLICK = 'click'
A_TYPE = 'type'
A_TEXT = 'text'
A_HOVER = 'hover'
A_HOVER_CLICK = 'hover_click'
A_VALUE = 'value'
A_INDEX = 'index'
A_VISIBLE = 'visible'


#################
# ERRORS
#################

class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        results = f'{self.error_name}: {self.details} '
        return results


class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)


class NoSuchElementPresent(Error):
    def __init__(self, details):
        super().__init__('No such element', details)


# TODO: Function to make browser maximized
class Checker:
    """
    Base class for all checkers.
    """

    def __init__(self, url, driver):
        """
            Initialize the checker class

            Parameters
            ----------

            :param str url: input the url of the website
            :param driver: input the browser driverManager

        """
        self.time = None
        self.i = None
        self.func = None
        self.divpath = None
        self.m = None
        self.obj = None
        self.word = None
        self.ac2 = None
        self.lv2 = None
        self.locator2 = None
        self.ac_value = None
        self.lv = None
        self.locator = None
        self.ac = None
        self.tp = None
        self.url = url
        self.driver = driver
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        affirmative_url = self.valid_url(self.url)
        self.driver.get(f"{affirmative_url}")
        self.a = ActionChains(self.driver)

    def valid_url(self, url):
        try:
            req = requests.get(url)
            while req.status_code != requests.codes['ok']:
                assert False, f"Please enter a valid URL... {self.url} is not a valid URL."
        except Exception as ex:
            print(f'Something went wrong: {ex}')
            print('Try again!')
            assert False, f"Please enter a valid URL... {self.url} is not a valid URL."

        return url

    # TODO: check the functionality
    # working
    def display_url(self):
        """
                :return: Prints the url of the main url sent to the webdriver.
                :rtype: str
        """
        return print(f'Url is: {self.url}')

    # working
    def return_url(self):
        """
                :return: Returns the url of the main url sent to the webdriver.
                :rtype: str
        """
        return self.url

    def current_url(self):
        """
                        :return: Returns the url of the current website in the current selected tab
                        :rtype: str
                """
        return self.driver.getCurrentUrl()

    # working
    def input(self, tp, locator, locator_value, ac, ac_value):
        """
            Takes value from user and inputs in the field specified

            Parameters
            ----------

            :param str tp: Type of input eg. 'input'
            :param str locator: xpath/css
            :param str locator_value: input the value of the locator as xpath of css selector
            :param str ac: action to be performed e.g. 'type'
            :param str ac_value: value for the action

        """
        self.tp = tp
        self.locator = locator
        self.lv = locator_value
        self.ac = ac
        self.ac_value = ac_value
        if self.tp == T_INPUT:
            if self.locator == L_CSS:
                if self.ac == A_TYPE:
                    try:
                        self.driver.find_element(By.CSS_SELECTOR, f"{self.lv}").send_keys(f"{self.ac_value}")
                    except NoSuchElementException:
                        error = NoSuchElementPresent(
                            f"{self.tp} -> {self.locator} -> {self.lv} -> {self.ac} -> {self.ac_value}")
                        print(error.as_string())
                        assert False, f"{error.as_string()}"
                else:
                    error = IllegalCharError(f"{self.ac}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            elif self.locator == L_XPATH:
                if self.ac == A_TYPE:
                    try:
                        self.driver.find_element(By.XPATH, f"{self.lv}").send_keys(f"{self.ac_value}")
                    except NoSuchElementException:
                        error = NoSuchElementPresent(
                            f"{self.tp} -> {self.locator} -> {self.lv} -> {self.ac} -> {self.ac_value}")
                        print(error.as_string())
                        assert False, f"{error.as_string()}"
                else:
                    error = IllegalCharError(f"{self.ac}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            else:
                error = IllegalCharError(f"{self.locator}")
                print(error.as_string())
                assert False, f"{error.as_string()}"
        else:
            error = IllegalCharError(f"{self.tp}")
            print(error.as_string())
            assert False, f"{error.as_string()}"

    # working
    def button(self, tp, locator, locator_value, ac):
        """
            Clicks a button

            Parameters
            ----------

            :param str tp: Type of input eg. 'button'
            :param str locator: xpath/css
            :param str locator_value: input the value of the locator as xpath of css selector
            :param str ac: action to be performed eg. 'click', or 'hover'

        """
        self.tp = tp
        self.locator = locator
        self.lv = locator_value
        self.ac = ac
        if self.tp == T_BUTTON or self.tp == T_CHECKBOX:
            if self.locator == L_CSS:
                if self.ac == A_CLICK:
                    try:
                        self.driver.find_element(By.CSS_SELECTOR, f"{self.lv}").click()
                        self.driver.implicitly_wait(10)
                    except NoSuchElementException:
                        error = NoSuchElementPresent(f"{self.tp} -> {self.locator} -> {self.lv} -> {self.ac}")
                        print(error.as_string())
                        assert False, f"{error.as_string()}"
                elif self.ac == A_HOVER:
                    try:
                        self.m = self.driver.find_element(By.CSS_SELECTOR, f"{self.lv}")
                        self.driver.implicitly_wait(10)
                        self.a.move_to_element(self.m).perform()
                    except NoSuchElementException:
                        error = NoSuchElementPresent(f"{self.tp} -> {self.locator} -> {self.lv} -> {self.ac}")
                        print(error.as_string())
                        assert False, f"{error.as_string()}"
                elif self.ac == A_HOVER_CLICK:
                    try:
                        self.m = self.driver.find_element(By.CSS_SELECTOR, f"{self.lv}")
                        self.driver.implicitly_wait(10)
                        self.a.move_to_element(self.m).click(self.m).perform()
                    except NoSuchElementException:
                        error = NoSuchElementPresent(f"{self.tp} -> {self.locator} -> {self.lv} -> {self.ac}")
                        print(error.as_string())
                        assert False, f"{error.as_string()}"
                else:
                    error = IllegalCharError(f"{self.ac}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            elif self.locator == L_XPATH:
                if self.ac == A_CLICK:
                    try:
                        self.driver.find_element(By.XPATH, f"{self.lv}").click()
                        self.driver.implicitly_wait(10)
                    except NoSuchElementException:
                        error = NoSuchElementPresent(f"{self.tp} -> {self.locator} -> {self.lv} -> {self.ac}")
                        print(error.as_string())
                        assert False, f"{error.as_string()}"
                elif self.ac == A_HOVER:
                    try:
                        self.m = self.driver.find_element(By.XPATH, f"{self.lv}")
                        self.driver.implicitly_wait(10)
                        self.a.move_to_element(self.m).perform()
                    except NoSuchElementException:
                        error = NoSuchElementPresent(f"{self.tp} -> {self.locator} -> {self.lv} -> {self.ac}")
                        print(error.as_string())
                        assert False, f"{error.as_string()}"
                elif self.ac == A_HOVER_CLICK:
                    try:
                        self.m = self.driver.find_element(By.XPATH, f"{self.lv}")
                        self.driver.implicitly_wait(10)
                        self.a.move_to_element(self.m).click(self.m).perform()
                    except NoSuchElementException:
                        error = NoSuchElementPresent(f"{self.tp} -> {self.locator} -> {self.lv} -> {self.ac}")
                        print(error.as_string())
                        assert False, f"{error.as_string()}"
                else:
                    error = IllegalCharError(f"{self.ac}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            else:
                error = IllegalCharError(f"{self.locator}")
                print(error.as_string())
                assert False, f"{error.as_string()}"

        else:
            error = IllegalCharError(f"{self.tp}")
            print(error.as_string())
            assert False, f"{error.as_string()}"

    # working
    def static_dropdown(self, locator, locator_value, ac, ac_value):
        """
            Static dropdown -> Works with Select Tag

            Parameters
            ----------

            :param str locator: xpath/css
            :param str locator_value: input the value of the locator as xpath of css selector
            :param str ac: action to be performed eg. 'value','visible' or 'index'
            :param str ac_value: value for the action

        """
        self.locator = locator
        self.lv = locator_value
        self.ac = ac
        self.ac_value = ac_value
        if self.locator == L_CSS:
            if self.ac == A_VALUE:
                try:
                    s_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, f"{self.lv}"))
                    s_dropdown.select_by_value(self.ac_value)
                except NoSuchElementException:
                    error = NoSuchElementPresent(f"{self.locator} -> {self.lv} -> {self.ac} -> {self.ac_value}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            elif self.ac == A_INDEX:
                try:
                    s_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, f"{self.lv}"))
                    int(self.ac_value)
                    s_dropdown.select_by_index(self.ac_value)
                except NoSuchElementException:
                    error = NoSuchElementPresent(f"{self.locator} -> {self.lv} -> {self.ac} -> {self.ac_value}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            elif self.ac == A_VISIBLE:
                try:
                    s_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, f"{self.lv}"))
                    s_dropdown.select_by_visible_text(self.ac_value)
                except NoSuchElementException:
                    error = NoSuchElementPresent(f"{self.locator} -> {self.lv} -> {self.ac} -> {self.ac_value}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            else:
                error = IllegalCharError(f"{self.ac}")
                print(error.as_string())
                assert False, f"{error.as_string()}"
        elif self.locator == L_XPATH:
            if self.ac == A_VALUE:
                try:
                    s_dropdown = Select(self.driver.find_element(By.XPATH, f"{self.lv}"))
                    s_dropdown.select_by_value(self.ac_value)
                except NoSuchElementException:
                    error = NoSuchElementPresent(f"{self.locator} -> {self.lv} -> {self.ac} -> {self.ac_value}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            elif self.ac == A_INDEX:
                try:
                    s_dropdown = Select(self.driver.find_element(By.XPATH, f"{self.lv}"))
                    int(self.ac_value)
                    s_dropdown.select_by_index(self.ac_value)
                except NoSuchElementException:
                    error = NoSuchElementPresent(f"{self.locator} -> {self.lv} -> {self.ac} -> {self.ac_value}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            elif self.ac == A_VISIBLE:
                try:
                    s_dropdown = Select(self.driver.find_element(By.XPATH, f"{self.lv}"))
                    s_dropdown.select_by_visible_text(self.ac_value)
                except NoSuchElementException:
                    error = NoSuchElementPresent(f"{self.locator} -> {self.lv} -> {self.ac} -> {self.ac_value}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            else:
                error = IllegalCharError(f"{self.ac}")
                print(error.as_string())
                assert False, f"{error.as_string()}"
        else:
            error = IllegalCharError(f"{self.locator}")
            print(error.as_string())
            assert False, f"{error.as_string()}"

    # working
    def slowmo(self, t):
        """
                    Parameters
                    ----------
                    :param float t: Time to wait (in seconds)

                 """
        self.time = t
        time.sleep(self.time)

    def returner(self, tp, locator, locator_value, ac):
        """
            Parameters
            ----------

            :param str tp: Type of input eg. 'return'
            :param str locator: xpath/css
            :param str locator_value: input the value of the locator as xpath of css selector
            :param str ac: action to be performed e.g. 'text'
            :return: Returns the text of the element
            :rtype: str

        """
        self.tp = tp
        self.locator = locator
        self.lv = locator_value
        self.ac = ac
        if self.tp == T_RETURN:
            if self.locator == L_CSS:
                if self.ac == A_TEXT:
                    try:
                        input_obj = self.driver.find_element(By.CSS_SELECTOR, f"{self.lv}")
                    except NoSuchElementException:
                        return
                else:
                    error = IllegalCharError(f"{self.ac}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            elif self.locator == L_XPATH:
                if self.ac == A_TEXT:
                    try:
                        input_obj = self.driver.find_element(By.XPATH, f"{self.lv}")
                    except NoSuchElementException:
                        return
                else:
                    error = IllegalCharError(f"{self.ac}")
                    print(error.as_string())
                    assert False, f"{error.as_string()}"
            else:
                error = IllegalCharError(f"{self.locator}")
                print(error.as_string())
                assert False, f"{error.as_string()}"
        else:
            error = IllegalCharError(f"{self.tp}")
            print(error.as_string())
            assert False, f"{error.as_string()}"

        return input_obj.text

    def take_pic(self):
        """
            :return: Returns the screenshot of the current webpage
         """
        image = self.driver.save_screenshot()
        return image

    def word_assert(self, obj, word):
        """

        Parameters
        ----------
        :param str obj: First string
        :param str word: Second string
        :return: Asserts True if both match else False
        :rtype: bool

        """
        self.obj = obj
        self.word = word
        if self.obj == self.word:
            assert True
        else:
            assert False

    def goto(self, url):
        """
        Changes the url to the specified url

        Parameters
        ----------
        :param str url: Url to goto

        """
        self.url = url
        self.driver.implicitly_wait(10)
        self.driver.get(f"{self.url}")

    def count_div_el(self, locator, divpath):
        """
        counts the elements present in the specified div

        Parameters
        ----------
        :param str locator: xpath/css
        :param str divpath: xpath or css selector of the div element

        """
        self.divpath = divpath
        self.locator = locator
        if self.locator == L_CSS:
            count = len(self.driver.find_elements(By.CSS_SELECTOR, f"{self.divpath}"))
        elif self.locator == L_XPATH:
            count = len(self.driver.find_elements(By.XPATH, f"{self.divpath}"))
        else:
            error = IllegalCharError(f"{self.ac}")
            print(error.as_string())
            assert False, f"{error.as_string()}"
        return count

    def divcheck(self, divpath, ac, i=0):
        """
                clicks on the div elements in increasing order of xpath

                Parameters
                ----------
                :param str divpath: takes the xpath of the div
                :param str ac: action needed to be performed e.g: 'click'
                :param int i: xpath or css selector of the div element

        """
        self.divpath = divpath
        self.ac = ac
        self.i = i
        path = f"{self.divpath}"
        if ac == A_CLICK:
            self.driver.find_element(By.XPATH, f"({path})[{i + 1}]").click()

    def divtext(self, divpath, ac):
        """
                Parameters
                ----------
                :param str divpath: takes the xpath of the div
                :param str ac: action needed to be performed e.g: 'text'
                :return: Returns all the text inside the div element in increasing order of xpath
                :rtype: list


        """
        list_of_words = []
        self.divpath = divpath
        self.ac = ac
        count = len(self.driver.find_elements(By.XPATH, f"{self.divpath}"))
        # print(count)
        for a in range(count):
            path = f"{self.divpath}"
            if ac == A_TEXT:
                i = self.driver.find_element(By.XPATH, f"({path})[{a + 1}]")
                list_of_words += [i.text]
        return list_of_words

    def divtextcheck(self, divpath, ac, word):
        """
                Parameters
                ----------
                :param str divpath: takes the xpath of the div
                :param str ac: action needed to be performed e.g: 'text'
                :param str word: word that needs to be evaluated in the list of words
                :return: Returns the text of the element in increasing order of xpath and checks equality
                with the string provided.
                :rtype: bool


        """
        list_of_words = []
        self.divpath = divpath
        self.ac = ac
        self.word = word
        count = len(self.driver.find_elements(By.XPATH, f"{self.divpath}"))
        for a in range(count):
            path = f"{self.divpath}"
            if ac == A_TEXT:
                i = self.driver.find_element(By.XPATH, f"({path})[{a + 1}]")
                list_of_words += [i.text]
        if word in list_of_words:
            print("True")
        else:
            print("False")

    def homescreen(self):
        """
            Moves to the first tab and sets it as the main tab.

        """
        self.driver.implicitly_wait(10)
        parent = self.driver.window_handles[0]
        self.driver.switch_to.window(parent)
        self.driver.implicitly_wait(10)

    def childscreen(self, i=1):
        """
            Moves to the second tab and sets it as the main tab.

        """
        self.driver.implicitly_wait(10)
        self.i = i
        child = self.driver.window_handles[self.i]
        self.driver.switch_to.window(child)
        self.driver.implicitly_wait(10)

    def closewindow(self):
        """
            CLoses the tab

        """
        self.driver.close()

    def returndivtext(self, divpath, ac, i=0):
        """
                Parameters
                ----------
                :param str divpath: takes the xpath of the div
                :param str ac: action needed to be performed e.g: 'click'
                :param int i: xpath or css selector of the div element
                :return: Returns the text of the element, can be used with increasing order of xpath
                :rtype: str

        """
        self.divpath = divpath
        self.ac = ac
        self.i = i
        path = f"{self.divpath}"
        if ac == A_TEXT:
            i = self.driver.find_element(By.XPATH, f"({path})[{i + 1}]")
        return i.text

    def cookie_click(self, locator, locator_value):
        """
            Function to specify a cookie click.
            Replicates the button function.

            Parameters
            ----------
            :param str locator: xpath/css
            :param str locator_value: input the value of the locator as xpath of css selector
        """
        self.locator = locator
        self.lv = locator_value
        if self.locator == L_CSS:
            try:
                self.button("button", "css",
                            self.lv,
                            "click")
            except NoSuchElementException:
                pass
        if self.locator == L_XPATH:
            try:
                self.button("button", "xpath",
                            self.lv,
                            "click")
            except NoSuchElementException:
                pass

    def end(self):
        """
            Quit the whole browser session along with all the associated browser windows

        """
        self.driver.quit()

    def title_check(self, title):
        if self.driver.title == title:
            assert True
        else:
            assert False

    def title_present(self, title):
        if self.driver.title == title:
            return True
        else:
            return False

    # working
    def check_all(self, locator, locator_value):
        """
                    Checks all checkboxes

                    Parameters
                    ----------


                    :param str locator: xpath/css
                    :param str locator_value: input the value of the locator as xpath of css selector


                """
        self.locator = locator
        self.lv = locator_value
        if self.locator == L_CSS:

            try:
                checkboxes = self.driver.find_elements(By.CSS_SELECTOR, f"{self.lv}")
                if len(checkboxes) == 0:
                    print(f"There are 0 checkboxes to check, try checking the locator value. ")
                for checkbox in checkboxes:
                    checkbox.click()
            except NoSuchElementException:
                error = NoSuchElementPresent(f"{self.locator} -> {self.lv}")
                print(error.as_string())
                assert False, f"{error.as_string()}"

        elif self.locator == L_XPATH:

            try:
                checkboxes = self.driver.find_elements(By.XPATH, f"{self.lv}")
                if len(checkboxes) == 0:
                    print(f"There are 0 checkboxes to check, try checking the locator value. ")
                for checkbox in checkboxes:
                    checkbox.click()
            except NoSuchElementException:
                error = NoSuchElementPresent(f"{self.locator} -> {self.lv}")
                print(error.as_string())
                assert False, f"{error.as_string()}"

        else:
            error = IllegalCharError(f"{self.locator}")
            print(error.as_string())
            assert False, f"{error.as_string()}"

    # working
    def count_all_checkboxes(self, locator, locator_value):
        """
                    Checks all checkboxes

                    Parameters
                    ----------


                    :param str locator: xpath/css
                    :param str locator_value: input the value of the locator as xpath of css selector
                    :return: Returns the number of checkboxes
                    :rtype: int

                """
        self.locator = locator
        self.lv = locator_value
        if self.locator == L_CSS:

            try:
                checkboxes = self.driver.find_elements(By.CSS_SELECTOR, f"{self.lv}")
            except NoSuchElementException:
                error = NoSuchElementPresent(f"{self.locator} -> {self.lv}")
                print(error.as_string())
                assert False, f"{error.as_string()}"

        elif self.locator == L_XPATH:

            try:
                checkboxes = self.driver.find_elements(By.XPATH, f"{self.lv}")
            except NoSuchElementException:
                error = NoSuchElementPresent(f"{self.locator} -> {self.lv}")
                print(error.as_string())
                assert False, f"{error.as_string()}"

        else:
            error = IllegalCharError(f"{self.locator}")
            print(error.as_string())
            assert False, f"{error.as_string()}"
        if len(checkboxes) == 0:
            return f"0, (If it should not be 0, check the locator value."
        else:
            return len(checkboxes)
