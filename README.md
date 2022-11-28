# My bookstore app

---

> ***v1.1*** - This is an base project in a learning path; it includes topics as:

*Some features*

- The views in this project are function-based and class-based views.

- It uses templates with template inheritance based on jinja 2.

- It uses different types of forms (forms.Form and form.ModelForm) - to do.

- It doesn't uses media file management - to do.

- Model registrations on the admin site have basic customization.

- The project uses sqlite3 (currently) as the database.

## Requirements and versions

- ***Django=4.1.3***

## How to run locally?

```
python3 manage.py createsuperuser

i.e.
    admin
    admin1234.

python3 manage.py makemigrations

python3 manage.py migrate
```
```
python3 manage.py runserver
```

## Endpoints

| route | meaning |
| --- | --- |
| /admin/ | django admin site |
| / | book list |
| /book/{book_id}/detail/ | show a book |

---
---

# Bibliography

- [Curso Django Platzi 2022](https://platzi.com/cursos/django/)

- [My own note taking about python](https://github.com/dcarolinahdev/notes/blob/master/python.md)

- [My own note taking about django](https://github.com/dcarolinahdev/notes/blob/master/django.md)
