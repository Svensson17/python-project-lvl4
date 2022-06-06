### Hexlet tests and linter status:
[![Actions Status](https://github.com/Svensson17/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/Svensson17/python-project-lvl4/actions)
[![CI](https://github.com/Svensson17/python-project-lvl4/actions/workflows/CI.yml/badge.svg)](https://github.com/Svensson17/python-project-lvl4/actions/workflows/CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/59118e1b41455367e86d/maintainability)](https://codeclimate.com/github/Svensson17/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/59118e1b41455367e86d/test_coverage)](https://codeclimate.com/github/Svensson17/python-project-lvl4/test_coverage)

Приложение развернуто на Heroku: https://dashboard.heroku.com/apps/warm-temple-58793

## Функциональные возможности
приложение настроено на работу с базой данных PostgreSQL;
реализована авторизация пользователей;
в системе может быть зарегистрировано множество пользователей;
пользователь после авторизации может создавать себе задачу, указав для этого ее название, описание, статус, назначить исполнителя из списка зарегистрированных пользователей и при необходимости выбрать один или несколко тегов из списка;
пользователь может редактировать содержимое любой своей или чужой задачи;
пользователь может удалить любую из ранее созданных задач;
пользователь может вывести список задач с возможностью фильтрации по статусу, автору, исполнителю, а также по тегам;
пользователь может может добавлять, редактировать и изменять статусы, а также добавлять теги.

## Запуск приложения
Активируйте виртуальное окружение и установите необходимые зависимости, выполнив команду:

```console
poetry install
```

Замените название файла .env.example на .env и задайте свои значения переменных внутри этого файла.

После этого сделайте и примените миграции командой:

```console
make migrations
```