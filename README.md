# status-pod

Сервис поддержки статуса информации и нотификаций
- анализ ленты инсты
- отправка уведомлений в тг
- напоминания
- анализ финансов

# TODO
**NOTE** модуль tg не должен ничего знать о модуле instagram и наоборот
то же самое касается вновь созданных модулей (приложений) - полная изоляция,
взаимодействие через интерфейсы

- внедрить fastapi
- добавить просмотр постов ленты в инсте
- описать тематические триггер-слова, которые будут искаться в постах
 (пока тематика одна - какие-либо встречи)
- организовать отправку уведомлений в телеграм
- запускать функционал через вызовы api
- настроить деплой
- создать шедулер (для напоминалок и подобной чухни)

# Алгоритм анализа описания постов
- открыть ленту
- dd = получить желаемую дату крайнего поста, который будет проанализирован
- пока: дата последнего найденного поста <= dd
    - собрать доступные посты
    - посчитать хэш каждого доступного поста (имя_профиля + дата_время_поста)
    - сравнить ранее посчитанные хэши и взять только новые
    - для каждого нового доступного поста:
        + (1) взять первый комментарий (описание поста на данный момент в html-коде это коммент)
        + (2) проверить, что он написан владельцем аккаунта, с которого размещен пост
        + если (шаг 2) == true:
            + (1) сделать анализ текста поста, на его основании отправить/не отправить уведомление в телеграм
    - сделать скрол даун
