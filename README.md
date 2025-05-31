# Django E-commerce Project

A full-featured e-commerce website built with Django, featuring a modern and responsive design.

## Features

- User authentication and authorization
- Product catalog with categories
- Shopping cart functionality
- Product search and filtering
- Responsive design for all devices
- Admin panel for managing products and orders
- Media handling for product images

## Tech Stack

- Python 3.x
- Django
- PostgreSQL (Database)
- HTML/CSS
- JavaScript
- Bootstrap (for responsive design)

## Project Structure

```
Ecom/
├── ecom/              # Main project directory
│   ├── cart/         # Shopping cart application
│   ├── Store/        # Store application
│   ├── static/       # Static files (CSS, JS, images)
│   ├── media/        # User-uploaded media files
│   ├── templates/    # HTML templates
│   └── ecom/         # Project settings
├── venv/             # Virtual environment
└── manage.py         # Django management script
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/akshaykarthicks/Django_Ecom.git
cd Django_Ecom
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=your-database-url
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

1. Access the admin panel at `http://127.0.0.1:8000/admin` to manage products, categories, and orders
2. Browse products on the homepage
3. Add products to cart
4. Complete the checkout process

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

For any queries or support, please open an issue in the repository. 