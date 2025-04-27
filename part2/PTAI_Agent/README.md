Установка и настройка PT AI Agent
=================================

Развертывание модуля PT AI Enterprise Agent

Этот раздел содержит инструкции по подготовке к развертыванию, установке и настройке
модуля PT AI Enterprise Agent. PT AI Enterprise Agent можно установить на Windows и Linux.
(Дальше будет выбран вариант с Linux)

Установка модуля PT AI Agent для Linux
--------------------------------------

   Внимание! Для работы PT AI Enterprise Agent в операционной системе должен быть
             установлен компонент Docker CE версии 20 или выше.

   Внимание! При установке PT AI Enterprise Agent в Astra Linux необходимо использовать ядро
             generic, так как ядро с усиленной защитой (hardened) не позволяет запускать
             непривилегированные контейнеры.

Чтобы установить PT AI Enterprise Agent:

1.  Сделайте файл инсталлятора исполняемым:
    `chmod +x <Версия сборки PT AI Enterprise Agent>.run`
2.  Запустите скрипт установки:
    `sudo ./<Версия сборки PT AI Enterprise Agent>.run`
    При запуске скрипта сформируется файл журнала `/var/log/ptaiagent/install/
    ptai-agent-install-<Дата и время>.log`, который содержит системные
    информационные сообщения, предупреждения и ошибки.
3.  Введите y, чтобы принять условия лицензионного соглашения.
4.  Введите y, чтобы подтвердить установку PT AI Enterprise Agent. Начнется установка
    PT AI Enterprise Agent.
5.  Выберите способ настройки подключения модуля PT AI Enterprise Agent к
    PT AI Enterprise Server:
    * если вы хотите настроить подключение к PT AI Enterprise Server в процессе установки,
      введите y;
    * если вы хотите настроить подключение к PT AI Enterprise Server позднее в
      конфигурационном файле в каталоге `/etc/ptai-agent.conf`, введите n.
6.  Если вы ввели y, укажите следующие параметры:
    * URL PT AI Enterprise Server.
    * Токен доступа [Инструкция по созданию токена](PTAI_Server/README.md#создание-токенов-доступа).
    * Уникальное имя PT AI Enterprise Agent.

      Примечание. Указанное имя будет отображаться в веб-интерфейсе на странице
                  Агенты сканирования. Имя Docker-контейнера останется прежним — ptai-agent.
    * Имя узла и IP-адрес PT AI Enterprise Server в виде <Имя узла:IP-адрес> (необязательно).

      Примечание. PT AI Enterprise Agent, запущенный в Docker-контейнере, обращается к
                  узлу, на котором развернут PT AI Enterprise Server, по его имени (hostname).
                  Если у вас не настроен DNS-сервер для разрешения имен узлов в IP-адреса, вы
                  можете установить соответствие имени узла и IP-адреса c помощью этого параметра.

PT AI Enterprise Agent установлен. Дистрибутив хранится в каталоге `/opt/ptai-agent`.

Настройка модуля PT AI Enterprise Agent
---------------------------------------

Чтобы настроить модуль PT AI Enterprise Agent для Linux:

1. Откройте файл `ptai-agent.conf` в каталоге `/etc`.
2. Измените нужные строки в файле:
   `SERVER_URL="<Адрес PT AI Enterprise Server>"`
   `HOSTS="<Имя узла PT AI Enterprise Server:IP-адрес PT AI Enterprise Server>"`
   `AGENT_TOKEN="<Токен доступа>"`
   `AGENT_NAME="<Уникальное имя PT AI Enterprise Agent>"`
   [Инструкция по созданию токена](PTAI_Server/README.md#создание-токенов-доступа)
3. Перезапустите Docker-котейнер PT AI Enterprise Agent:
   `sudo systemctl restart ptai-agent.`
   
Модуль PT AI Enterprise Agent настроен.