## :green_book: Проект по автоматизации UI тестирования на Python для сайта stellarburgers.nomoreparties.site

Данный проект подготовлен для Яндекс.Практикум в качестве учебного задания

## :computer: Использованный стек технологий

* Pytest

## :pushpin: Описание тестов

1. test_registration_user_correct_data - проверка успешной регистрации с корректными данными.
2. test_registration_user_incorrect_password - проверка сообщения об ошибке при вводе некорректного пароля.
3. test_enter_from_button_login_and_personal_page - параметризованный тест. В первом тесте проверяется вход с главной
   страницы по кнопке "Войти в аккаунт". Во втором тесте проверяется вход с главной страницы по кнопке "Личный кабинет".
4. test_enter_from_form_registration_and_password_recovery - параметризованный тест. В первом тесте проверяется вход
   через ссылку "Войти" в форме регистрации. Во втором тесте проверяется вход через ссылку "Войти" в форме
   восстановления пароля.
5. test_enter_in_personal_page - переход с главной страницы в личный кабинет по клику на кнопку «Личный кабинет».
6. test_enter_in_constructor_from_personal_page - параметризованный тест. В первом тесте проверяется переход из личного
   кабинета в конструтор по клику на кнопку "Конструктор". Во втором тесте проверяется переход из личного
   кабинета в конструтор по клику на логотип Stellar Burgers.
7. test_logout_button - проверка выхода по кнопке «Выйти» в личном кабинете.
8. test_switching_tab_sauces_and_stuffing - параметризованный тест. В первом тесте проверяется переход в конструкторе в
   раздел "Соусы". Во втором тесте проверяется переход в конструкторе в раздел "Начинки".
9. test_switching_tab_bun - проверяется переход в конструкторе в раздел "Булки".