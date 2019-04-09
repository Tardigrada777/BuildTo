# Приложение, с которого начался мой путь программиста

Автоматизация расчёта заказа продукции для ресторана Макдоналдс.  
Приложение считывает данные из файла __data.xls__ и формирует выходные бланки, сохраняя их в папке *Blanks*  

## Установка
В папке с ихсодниками программы создайте виртуальное окружение с помощью (либо любым удобным Вам способом создания вирт.окружения):
> `python3 -m venv env`  

или 

> `pip install virtualenv && virtualenv venv`  
  
Активируйте его (Linux)
> `source venv/bin/activate`

Установите зависимости
> `pip install -r requirements.txt`

## Использование
Для начала необходимо заполнить исходные данные в таблице **data.xls**  
Затем запустить приложение с помощью
> `python BuildTo_v0.4_Core.py`

Затем выбрать из меню в консоли нужное действие. 

*Created by Mylcev Vladimir (**tardigrada777**)*  
*May, 2018*