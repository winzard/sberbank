# sberbank
Парсер "интерактивного отчета" по картам Сбербанка

Вам понадобится пакет BeautifulSoup

Как пользоваться: 
python3 sberbank.py <Имя файла с отчетом>

На выходе получите в той же директории файл <Имя файла с отчетом>.csv примерно такого вида:

    MTS AVTO F19605894576 ; 24.03.2020 ; -200,00 ; Коммунальные платежи, связь, интернет
    STEAMGAMES.COM ; 24.03.2020 ; -839,00 ; Отдых и развлечения
    Автоплатёж "ДОМАШНИЙ ИНТЕРНЕТ И" ; 19.03.2020 ; -550,00 ; Прочие расходы
    YM*OVDINFO ; 06.05.2020 ; -282,00 ; Прочие расходы
    AUTOPLATEZH_P2P перевод 4276****3379 С. СЕРГЕЙ СЕРГЕЕВИЧ ; 16.04.2020 ; -404,00 ; Перевод с карты

