from data import BROWSER_NAME

if BROWSER_NAME == 'Chrome':
    self.wait.until_not(expected_conditions.visibility_of_element_located())