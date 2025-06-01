# E-Commerce Website

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
- SQLite (Database)
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
git clone <repository-url>
cd Ecom
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

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
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

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or support, please open an issue in the repository. 
