# data-visualisation-django
Consuming, storing and visualising data concerned with energy.

### Utilized Frameworks
- Django
- Rest Framework
- Chartjs
- Postgresql

### Brief Instructions
To run the localserver, first ensure postresql is activated. Then in `core/`  execute:

```
python manage.py runserver
```

You can modify the `core/settings.py` to match your postresql set up. Currently, the project utilises a database called `core`. 

Finally, it is also worth notinig that the application was split in to three main webapps:
- csvs (Data Integration)
- energy (HTML Table Visualisation)
- insight (Data visualisation with ChartJS)

You can find the code in each of their respective directories. Furthermore, for CSV a simple approach was taken for matching csv input to the appropriate model/datatable. This was done by simply pairing csv string names with the appropriate table. This solution is sufficient for internal use, but may cause issues for external as it is quite easy to rename a file inappropriately/different from the initial.

### Demonstrative endpoints
- Upload CSVs to database (http://127.0.0.1:8000/csvs/upload)
- Basic data visualisation (http://127.0.0.1:8000/energy/halfhourly)
- Data visualisation (http://127.0.0.1:8000/insight/)


