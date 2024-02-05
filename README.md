# Warehouse Database

### Brief description
MongoDB database to store information about warehouse stock.<br>
Communication with database through API with [FastAPI](###Why-FastAPI?).<br>
Contenerized with Docker. <br>
Application has implemented CRUD features.

## Setup

1. Clone repository

```bash
git clone https://github.com/KonradBorowik/Warehouse-database.git
```

2. Build Docker image ([make sure Docker is installed on your system](https://docs.docker.com/desktop/wsl/))

```bash
docker build -t kb_warehouse_database .
```

3. Run container

```bash
docker run -d --name mycontainer -p 80:80 kb_warehouse_database
```

## Database

This db comes with preloaded sample data. Two collections:
- Categories: 1 base category and 3 subcategories
    ```json
    {
        "name": <str>,
        "parent_name": <str>
    }
    ```
- Parts:
    ```json
    {
        "serial_number": <str>,
        "name": <str>,
        "description": <str>,
        "category": <str>,
        "quantity": <int>,
        "price": <float>,
        "location": {
            "warehouse": <str>,
            "room": <int>,
            "bookcase": <int>,
            "shelf": <int>,
            "cuvette": <int>,
            "column": <int>,
            "row": <int>,
        }
    }
    ```

## Explore endpoints 
http://localhost/docs#

Endpoints for catategories:
- GET http://localhost/ - returns all categories in database
- POST http://localhost/ - uploads category (json format required)
- PUT http://localhost/{id} - updates specified record (by _id)
- DELETE http://localhost/{id} - deletes specified record (by _id)

Endpoints for Parts:
- GET http://localhost/ - returns all parts in database
- GET http://localhost/search/{key: value} - returns all parts with matching key and value pair
- GET http://localhost/search/value - returns all parts with matching value
- POST http://localhost/ - uploads category (json format required)
- PUT http://localhost/{id} - updates specified record (by _id)
- DELETE http://localhost/{id} - deletes specified record (by _id)


### Why FastAPI?
Easy prototyping, fast and realiable. Support for typehinting allows for faster development. Doesn't require much code.