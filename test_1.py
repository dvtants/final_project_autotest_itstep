













# В терміналі PyCharm:
# pytest -s -v test_1.py
# pytest -s -v -m "smoke" test_1.py - виконується один тест тільки смоук, а саме: @pytest.mark.smoke
# pytest -s -v -m "regression" test_1.py - виконується два тести де є рігрешн, а саме: @pytest.mark.regression
# pytest -s -v -m " not regression" test_1.py - виконується все окрім рігрешн.
# pytest -s -v -m "not smoke" test_1.py - виконується все окрім смоук.
# pytest -s -v -m "regression or smoke" test_1.py - все виконується.
# pytest -s -v -m "regression and smoke" test_1.py - нічого не виконується.
# pytest -s -v -m "regression and chrome_117" test_1.py - проходить тест де є і regression і chrome_117, а саме: @pytest.mark.chrome_117 і @pytest.mark.regression
# pytest -s -v --browser_mode="gui" test_1.py
# pytest -s -v --browser_mode="gui" --browser_name="firefox" test_1.py
# дивись файл pytest.ini - зникає warnings - попередження.
# дивись файл conftest.py - назва цього файла саме така і не повинна змінюватися.



