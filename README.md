# schedule_app

Инструкция:
  1. Скачать и извлечь архив с приложением
  2. Перейти в католог с приложением
  3. Запустиь в нем командрую строку
  4. Прописать python -m pip install -r requirements.txt
  5. Создать или скопировать файл input.txt со списком сотрудников (каждый сотрудник с новой строки), указать дату начала и окончания в первых двух строках
  6. Запустить файл app.py
  7. Отрыть файл output.txt с отсортированным списком сотрудников

Пример файла input.txt:
  01.04.2023  
  30.04.2023  
  Василий  
  Глеб  
  Иван  
  ...

Зависимость:
 - numpy

Необходимые файлы:  
.  
|   app.py  
|   input.txt  
\\---requirements.txt  

Планы:
 - Исключение праздничных дней
